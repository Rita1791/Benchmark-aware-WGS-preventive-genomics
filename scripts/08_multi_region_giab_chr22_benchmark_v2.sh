#!/usr/bin/env bash
set -u
set -o pipefail

cd ~/NAINFIT_NGS_RESEARCH_PIPELINE

BAM_URL="https://ftp-trace.ncbi.nlm.nih.gov/ReferenceSamples/giab/data/NA12878/NIST_NA12878_HG001_HiSeq_300x/NHGRI_Illumina300X_novoalign_bams/HG001.GRCh38_full_plus_hs38d1_analysis_set_minus_alts.300x.bam"

REF="reference/GRCh38_chr22/chr22.fa"
TRUTH_CHR22="reference_datasets/giab_truth/HG001_GRCh38_chr22/HG001_GRCh38_chr22_v4.2.1_benchmark_CONFIDENT.vcf.gz"
BED_CHR22="reference_datasets/giab_truth/HG001_GRCh38_chr22/HG001_GRCh38_chr22_v4.2.1_benchmark.bed"

OUTDIR="results/benchmark_valid_multi_region_v2"
REGION_DIR="$OUTDIR/regions"
BAM_DIR="$OUTDIR/bam"
VCF_DIR="$OUTDIR/vcf"
NORM_DIR="$OUTDIR/normalized"
ISEC_DIR="$OUTDIR/isec"
LOG_DIR="$OUTDIR/logs"
REPORT_DIR="$OUTDIR/reports"

mkdir -p "$REGION_DIR" "$BAM_DIR" "$VCF_DIR" "$NORM_DIR" "$ISEC_DIR" "$LOG_DIR" "$REPORT_DIR"

SUMMARY="$REPORT_DIR/multi_region_benchmark_summary.tsv"

count_vcf_records() {
    local file="$1"
    awk 'BEGIN{c=0} !/^#/{c++} END{print c}' "$file"
}

count_vcfgz_records() {
    local file="$1"
    bcftools view -H "$file" 2>/dev/null | awk 'BEGIN{c=0} {c++} END{print c}'
}

echo "region_id	region	length_bp	truth_variants	bam_reads	mapped_pct	properly_paired_pct	raw_calls	filtered_calls	norm_truth	norm_project	truth_only	project_only	shared	recall_pct	precision_pct	f1_pct" > "$SUMMARY"

echo "Selecting regions..."

python3 - <<'PY'
from pathlib import Path
import gzip, bisect

bed_file = Path("reference_datasets/giab_truth/HG001_GRCh38_chr22/HG001_GRCh38_chr22_v4.2.1_benchmark.bed")
vcf_file = Path("reference_datasets/giab_truth/HG001_GRCh38_chr22/HG001_GRCh38_chr22_v4.2.1_benchmark_CONFIDENT.vcf.gz")
out_file = Path("results/benchmark_valid_multi_region_v2/regions/selected_chr22_regions.tsv")

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
        if length < 5000 or length > 25000:
            continue

        left = bisect.bisect_left(positions, start)
        right = bisect.bisect_right(positions, end)
        count = right - left

        if count >= 20:
            regions.append((count, length, chrom, start, end))

regions.sort(key=lambda x: (x[0], -x[1]), reverse=True)
selected = regions[:5]

with out_file.open("w") as out:
    out.write("region_id\tchrom\tstart\tend\tlength_bp\ttruth_variant_count\n")
    for i, (count, length, chrom, start, end) in enumerate(selected, start=1):
        out.write(f"region_{i}\t{chrom}\t{start}\t{end}\t{length}\t{count}\n")

print(out_file.read_text())
PY

tail -n +2 "$REGION_DIR/selected_chr22_regions.tsv" | while IFS=$'\t' read -r REGION_ID CHROM START END LENGTH TRUTH_COUNT
do
    REGION="${CHROM}:${START}-${END}"
    BED_ONE="$REGION_DIR/${REGION_ID}.bed"

    echo "=================================================="
    echo "Processing $REGION_ID $REGION"

    echo -e "${CHROM}\t${START}\t${END}" > "$BED_ONE"

    samtools view -bh "$BAM_URL" "$REGION" 2>"$LOG_DIR/${REGION_ID}.samtools_view.log" \
      | samtools sort -o "$BAM_DIR/${REGION_ID}.sorted.bam" 2>"$LOG_DIR/${REGION_ID}.samtools_sort.log"

    samtools index "$BAM_DIR/${REGION_ID}.sorted.bam"

    samtools flagstat "$BAM_DIR/${REGION_ID}.sorted.bam" > "$LOG_DIR/${REGION_ID}.flagstat.txt"

    BAM_READS=$(awk '/in total/{print $1; exit}' "$LOG_DIR/${REGION_ID}.flagstat.txt")
    MAPPED_PCT=$(awk '/mapped \(/ && !/mate/ {gsub(/[()%]/,""); print $5; exit}' "$LOG_DIR/${REGION_ID}.flagstat.txt")
    PROPER_PCT=$(awk '/properly paired/ {gsub(/[()%]/,""); print $7; exit}' "$LOG_DIR/${REGION_ID}.flagstat.txt")

    bcftools view -R "$BED_ONE" -Oz -o "$VCF_DIR/${REGION_ID}.truth.vcf.gz" "$TRUTH_CHR22"
    bcftools index "$VCF_DIR/${REGION_ID}.truth.vcf.gz"

    bcftools mpileup \
      -f "$REF" \
      -r "$REGION" \
      -d 1000 \
      -Ou \
      "$BAM_DIR/${REGION_ID}.sorted.bam" \
    | bcftools call -mv -Oz -o "$VCF_DIR/${REGION_ID}.raw.vcf.gz"

    bcftools index "$VCF_DIR/${REGION_ID}.raw.vcf.gz"

    bcftools filter \
      -i 'QUAL>=30 && DP>=10' \
      -Oz \
      -o "$VCF_DIR/${REGION_ID}.filtered_QUAL30_DP10.vcf.gz" \
      "$VCF_DIR/${REGION_ID}.raw.vcf.gz"

    bcftools index "$VCF_DIR/${REGION_ID}.filtered_QUAL30_DP10.vcf.gz"

    bcftools norm \
      -f "$REF" \
      -m -both \
      -Oz \
      -o "$NORM_DIR/${REGION_ID}.truth.norm.vcf.gz" \
      "$VCF_DIR/${REGION_ID}.truth.vcf.gz"

    bcftools index "$NORM_DIR/${REGION_ID}.truth.norm.vcf.gz"

    bcftools norm \
      -f "$REF" \
      -m -both \
      -Oz \
      -o "$NORM_DIR/${REGION_ID}.filtered.norm.vcf.gz" \
      "$VCF_DIR/${REGION_ID}.filtered_QUAL30_DP10.vcf.gz"

    bcftools index "$NORM_DIR/${REGION_ID}.filtered.norm.vcf.gz"

    RAW_CALLS=$(count_vcfgz_records "$VCF_DIR/${REGION_ID}.raw.vcf.gz")
    FILTERED_CALLS=$(count_vcfgz_records "$VCF_DIR/${REGION_ID}.filtered_QUAL30_DP10.vcf.gz")
    NORM_TRUTH=$(count_vcfgz_records "$NORM_DIR/${REGION_ID}.truth.norm.vcf.gz")
    NORM_PROJECT=$(count_vcfgz_records "$NORM_DIR/${REGION_ID}.filtered.norm.vcf.gz")

    rm -rf "$ISEC_DIR/${REGION_ID}"
    mkdir -p "$ISEC_DIR/${REGION_ID}"

    bcftools isec \
      -p "$ISEC_DIR/${REGION_ID}" \
      "$NORM_DIR/${REGION_ID}.truth.norm.vcf.gz" \
      "$NORM_DIR/${REGION_ID}.filtered.norm.vcf.gz"

    TRUTH_ONLY=$(count_vcf_records "$ISEC_DIR/${REGION_ID}/0000.vcf")
    PROJECT_ONLY=$(count_vcf_records "$ISEC_DIR/${REGION_ID}/0001.vcf")
    SHARED=$(count_vcf_records "$ISEC_DIR/${REGION_ID}/0002.vcf")

    read RECALL PRECISION F1 <<< $(python3 - <<PY
truth_only = int("$TRUTH_ONLY")
project_only = int("$PROJECT_ONLY")
shared = int("$SHARED")

recall = shared / (shared + truth_only) * 100 if (shared + truth_only) else 0
precision = shared / (shared + project_only) * 100 if (shared + project_only) else 0
f1 = 2 * precision * recall / (precision + recall) if (precision + recall) else 0

print(f"{recall:.2f} {precision:.2f} {f1:.2f}")
PY
)

    echo -e "${REGION_ID}\t${REGION}\t${LENGTH}\t${TRUTH_COUNT}\t${BAM_READS}\t${MAPPED_PCT}\t${PROPER_PCT}\t${RAW_CALLS}\t${FILTERED_CALLS}\t${NORM_TRUTH}\t${NORM_PROJECT}\t${TRUTH_ONLY}\t${PROJECT_ONLY}\t${SHARED}\t${RECALL}\t${PRECISION}\t${F1}" >> "$SUMMARY"

    echo "Finished $REGION_ID"
done

echo "=================================================="
echo "Finished multi-region benchmark"
cat "$SUMMARY"
