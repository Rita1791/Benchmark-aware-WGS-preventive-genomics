#!/usr/bin/env bash
set -euo pipefail

cd ~/NAINFIT_NGS_RESEARCH_PIPELINE

BAM_URL="https://ftp-trace.ncbi.nlm.nih.gov/ReferenceSamples/giab/data/NA12878/NIST_NA12878_HG001_HiSeq_300x/NHGRI_Illumina300X_novoalign_bams/HG001.GRCh38_full_plus_hs38d1_analysis_set_minus_alts.300x.bam"

LOCAL_BAI="HG001.GRCh38_full_plus_hs38d1_analysis_set_minus_alts.300x.bam.bai"

REF="reference/GRCh38_chr22/chr22.fa"

TRUTH_CHR22="reference_datasets/giab_truth/HG001_GRCh38_chr22/HG001_GRCh38_chr22_v4.2.1_benchmark_CONFIDENT.vcf.gz"

BED_CHR22="reference_datasets/giab_truth/HG001_GRCh38_chr22/HG001_GRCh38_chr22_v4.2.1_benchmark.bed"

OUTDIR="results/benchmark_valid_multi_region"
REGION_DIR="$OUTDIR/regions"
BAM_DIR="$OUTDIR/bam"
VCF_DIR="$OUTDIR/vcf"
NORM_DIR="$OUTDIR/normalized"
ISEC_DIR="$OUTDIR/isec"
LOG_DIR="$OUTDIR/logs"
REPORT_DIR="$OUTDIR/reports"

mkdir -p "$REGION_DIR" "$BAM_DIR" "$VCF_DIR" "$NORM_DIR" "$ISEC_DIR" "$LOG_DIR" "$REPORT_DIR"

echo "Checking required files..."

test -f "$LOCAL_BAI" || { echo "Missing local BAM index: $LOCAL_BAI"; exit 1; }
test -f "$REF" || { echo "Missing reference FASTA: $REF"; exit 1; }
test -f "$REF.fai" || samtools faidx "$REF"
test -f "$TRUTH_CHR22" || { echo "Missing truth VCF: $TRUTH_CHR22"; exit 1; }
test -f "$BED_CHR22" || { echo "Missing BED file: $BED_CHR22"; exit 1; }

echo "Selecting 5 variant-rich chr22 high-confidence regions..."

python3 - <<'PY'
from pathlib import Path
import gzip
import bisect

bed_file = Path("reference_datasets/giab_truth/HG001_GRCh38_chr22/HG001_GRCh38_chr22_v4.2.1_benchmark.bed")
vcf_file = Path("reference_datasets/giab_truth/HG001_GRCh38_chr22/HG001_GRCh38_chr22_v4.2.1_benchmark_CONFIDENT.vcf.gz")
out_file = Path("results/benchmark_valid_multi_region/regions/selected_chr22_regions.tsv")

positions = []
with gzip.open(vcf_file, "rt") as f:
    for line in f:
        if line.startswith("#"):
            continue
        fields = line.split("\t")
        if fields[0] == "chr22":
            positions.append(int(fields[1]))

positions.sort()
regions = []

with bed_file.open() as f:
    for line in f:
        if not line.strip():
            continue

        chrom, start, end = line.strip().split()[:3]
        start = int(start)
        end = int(end)
        length = end - start

        if chrom != "chr22":
            continue

        # Keep regions manageable for local testing
        if length < 5000 or length > 25000:
            continue

        left = bisect.bisect_left(positions, start)
        right = bisect.bisect_right(positions, end)
        count = right - left

        # Need enough truth variants for useful benchmarking
        if count >= 20:
            regions.append((count, length, chrom, start, end))

# Select top 5 by truth-variant density/count
regions.sort(key=lambda x: (x[0], -x[1]), reverse=True)
selected = regions[:5]

with out_file.open("w") as out:
    out.write("region_id\tchrom\tstart\tend\tlength_bp\ttruth_variant_count\n")
    for i, (count, length, chrom, start, end) in enumerate(selected, start=1):
        out.write(f"region_{i}\t{chrom}\t{start}\t{end}\t{length}\t{count}\n")

print(out_file.read_text())
PY

SUMMARY="$REPORT_DIR/multi_region_benchmark_summary.tsv"

echo -e "region_id\tregion\tlength_bp\ttruth_variants\tbam_reads\tmapped_pct\tproperly_paired_pct\traw_calls\tfiltered_calls\tnorm_truth\tnorm_project\ttruth_only\tproject_only\tshared\trecall_pct\tprecision_pct\tf1_pct" > "$SUMMARY"

tail -n +2 "$REGION_DIR/selected_chr22_regions.tsv" | while IFS=$'\t' read -r REGION_ID CHROM START END LENGTH TRUTH_COUNT
do
    REGION="${CHROM}:${START}-${END}"
    BED_ONE="$REGION_DIR/${REGION_ID}.bed"

    echo -e "${CHROM}\t${START}\t${END}" > "$BED_ONE"

    echo "=================================================="
    echo "Processing $REGION_ID: $REGION"
    echo "Truth variants expected: $TRUTH_COUNT"

    # Extract and sort BAM
    samtools view -bh "$BAM_URL" "$REGION" \
      | samtools sort -o "$BAM_DIR/${REGION_ID}.sorted.bam"

    samtools index "$BAM_DIR/${REGION_ID}.sorted.bam"

    samtools flagstat "$BAM_DIR/${REGION_ID}.sorted.bam" \
      > "$LOG_DIR/${REGION_ID}.flagstat.txt"

    BAM_READS=$(grep "in total" "$LOG_DIR/${REGION_ID}.flagstat.txt" | awk '{print $1}')
    MAPPED_PCT=$(grep "mapped (" "$LOG_DIR/${REGION_ID}.flagstat.txt" | head -1 | sed -E 's/.*\(([0-9.]+)% .*/\1/')
    PROPER_PCT=$(grep "properly paired" "$LOG_DIR/${REGION_ID}.flagstat.txt" | sed -E 's/.*\(([0-9.]+)% .*/\1/')

    # Extract truth for region
    bcftools view \
      -R "$BED_ONE" \
      -Oz \
      -o "$VCF_DIR/${REGION_ID}.truth.vcf.gz" \
      "$TRUTH_CHR22"

    bcftools index "$VCF_DIR/${REGION_ID}.truth.vcf.gz"

    # Variant calling
    bcftools mpileup \
      -f "$REF" \
      -r "$REGION" \
      -d 1000 \
      -Ou \
      "$BAM_DIR/${REGION_ID}.sorted.bam" \
    | bcftools call \
      -mv \
      -Oz \
      -o "$VCF_DIR/${REGION_ID}.raw.vcf.gz"

    bcftools index "$VCF_DIR/${REGION_ID}.raw.vcf.gz"

    RAW_CALLS=$(bcftools view -H "$VCF_DIR/${REGION_ID}.raw.vcf.gz" | wc -l)

    # Filter
    bcftools filter \
      -i 'QUAL>=30 && DP>=10' \
      -Oz \
      -o "$VCF_DIR/${REGION_ID}.filtered_QUAL30_DP10.vcf.gz" \
      "$VCF_DIR/${REGION_ID}.raw.vcf.gz"

    bcftools index "$VCF_DIR/${REGION_ID}.filtered_QUAL30_DP10.vcf.gz"

    FILTERED_CALLS=$(bcftools view -H "$VCF_DIR/${REGION_ID}.filtered_QUAL30_DP10.vcf.gz" | wc -l)

    # Normalize truth
    bcftools norm \
      -f "$REF" \
      -m -both \
      -Oz \
      -o "$NORM_DIR/${REGION_ID}.truth.norm.vcf.gz" \
      "$VCF_DIR/${REGION_ID}.truth.vcf.gz"

    bcftools index "$NORM_DIR/${REGION_ID}.truth.norm.vcf.gz"

    # Normalize project
    bcftools norm \
      -f "$REF" \
      -m -both \
      -Oz \
      -o "$NORM_DIR/${REGION_ID}.filtered.norm.vcf.gz" \
      "$VCF_DIR/${REGION_ID}.filtered_QUAL30_DP10.vcf.gz"

    bcftools index "$NORM_DIR/${REGION_ID}.filtered.norm.vcf.gz"

    NORM_TRUTH=$(bcftools view -H "$NORM_DIR/${REGION_ID}.truth.norm.vcf.gz" | wc -l)
    NORM_PROJECT=$(bcftools view -H "$NORM_DIR/${REGION_ID}.filtered.norm.vcf.gz" | wc -l)

    # isec
    rm -rf "$ISEC_DIR/${REGION_ID}"
    mkdir -p "$ISEC_DIR/${REGION_ID}"

    bcftools isec \
      -p "$ISEC_DIR/${REGION_ID}" \
      "$NORM_DIR/${REGION_ID}.truth.norm.vcf.gz" \
      "$NORM_DIR/${REGION_ID}.filtered.norm.vcf.gz"

    TRUTH_ONLY=$(grep -v "^#" "$ISEC_DIR/${REGION_ID}/0000.vcf" | wc -l)
    PROJECT_ONLY=$(grep -v "^#" "$ISEC_DIR/${REGION_ID}/0001.vcf" | wc -l)
    SHARED=$(grep -v "^#" "$ISEC_DIR/${REGION_ID}/0002.vcf" | wc -l)

    METRICS=$(python3 - <<PY
truth_only = int("$TRUTH_ONLY")
project_only = int("$PROJECT_ONLY")
shared = int("$SHARED")

recall = shared / (shared + truth_only) * 100 if (shared + truth_only) else 0
precision = shared / (shared + project_only) * 100 if (shared + project_only) else 0
f1 = 2 * precision * recall / (precision + recall) if (precision + recall) else 0

print(f"{recall:.2f}\t{precision:.2f}\t{f1:.2f}")
PY
)

    echo -e "${REGION_ID}\t${REGION}\t${LENGTH}\t${TRUTH_COUNT}\t${BAM_READS}\t${MAPPED_PCT}\t${PROPER_PCT}\t${RAW_CALLS}\t${FILTERED_CALLS}\t${NORM_TRUTH}\t${NORM_PROJECT}\t${TRUTH_ONLY}\t${PROJECT_ONLY}\t${SHARED}\t${METRICS}" >> "$SUMMARY"

    echo "Finished $REGION_ID"
done

echo "=================================================="
echo "Multi-region benchmark complete."
echo "Summary file:"
echo "$SUMMARY"
cat "$SUMMARY"
