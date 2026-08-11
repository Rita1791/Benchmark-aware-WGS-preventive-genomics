#!/usr/bin/env bash
set -euo pipefail

# ============================================================
# Benchmark-aware WGS Preventive Genomics
# 25-region GIAB HG001 chr22 benchmark
# ============================================================

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "${ROOT_DIR}"

BAM_URL="https://ftp-trace.ncbi.nlm.nih.gov/ReferenceSamples/giab/data/NA12878/NIST_NA12878_HiSeq_300x/NHGRI_Illumina300X_novoalign_bams/HG001.GRCh38_full_plus_hs38d1_analysis_set_minus_alts.300x.bam"

REF="reference/GRCh38_chr22/chr22.fa"

TRUTH_CHR22="reference_datasets/giab_truth/HG001_GRCh38_chr22/HG001_GRCh38_chr22_v4.2.1_benchmark_CONFIDENT.vcf.gz"

BED_CHR22="reference_datasets/giab_truth/HG001_GRCh38_chr22/HG001_GRCh38_chr22_v4.2.1_benchmark.bed"

OUTDIR="results/benchmark_valid_chr22_25_region"

REGION_DIR="${OUTDIR}/regions"
BAM_DIR="${OUTDIR}/bam"
VCF_DIR="${OUTDIR}/vcf"
NORM_DIR="${OUTDIR}/normalized"
ISEC_DIR="${OUTDIR}/isec"
LOG_DIR="${OUTDIR}/logs"
REPORT_DIR="${OUTDIR}/reports"

SUMMARY="${REPORT_DIR}/multi_region_benchmark_summary.tsv"

THREADS="${THREADS:-1}"

mkdir -p \
    "${REGION_DIR}" \
    "${BAM_DIR}" \
    "${VCF_DIR}" \
    "${NORM_DIR}" \
    "${ISEC_DIR}" \
    "${LOG_DIR}" \
    "${REPORT_DIR}"

for tool in samtools bcftools python3; do
    command -v "${tool}" >/dev/null 2>&1 || {
        echo "[ERROR] Required executable not found: ${tool}"
        exit 1
    }
done

for file in "${REF}" "${TRUTH_CHR22}" "${BED_CHR22}"; do
    [[ -f "${file}" ]] || {
        echo "[ERROR] Required file not found: ${file}"
        exit 1
    }
done

echo -e \
"region_id\tregion\tlength_bp\ttruth_variants\tbam_reads\tmapped_pct\tproperly_paired_pct\traw_calls\tfiltered_calls\tnorm_truth\tnorm_project\ttruth_only\tproject_only\tshared\trecall_pct\tprecision_pct\tf1_pct" \
> "${SUMMARY}"

echo "[INFO] Selecting 25 benchmark regions..."

python3 - <<'PY'
from pathlib import Path
import gzip
import bisect

bed_file = Path(
    "reference_datasets/giab_truth/"
    "HG001_GRCh38_chr22/"
    "HG001_GRCh38_chr22_v4.2.1_benchmark.bed"
)

vcf_file = Path(
    "reference_datasets/giab_truth/"
    "HG001_GRCh38_chr22/"
    "HG001_GRCh38_chr22_v4.2.1_benchmark_CONFIDENT.vcf.gz"
)

out_file = Path(
    "results/benchmark_valid_chr22_25_region/"
    "regions/selected_chr22_regions.tsv"
)

positions = []

with gzip.open(vcf_file, "rt") as handle:

    for line in handle:

        if line.startswith("#"):
            continue

        fields = line.rstrip("\n").split("\t")

        if fields[0] == "chr22":
            positions.append(int(fields[1]))

positions.sort()

regions = []

with bed_file.open() as handle:

    for line in handle:

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
            regions.append(
                (count, length, chrom, start, end)
            )

regions.sort(
    key=lambda x: (x[0], -x[1]),
    reverse=True,
)

selected = regions[:25]

if len(selected) < 25:
    raise RuntimeError(
        f"Only {len(selected)} suitable regions were found; "
        "25 are required."
    )

with out_file.open("w") as handle:

    handle.write(
        "region_id\tchrom\tstart\tend\tlength_bp\t"
        "truth_variant_count\n"
    )

    for i, (
        count,
        length,
        chrom,
        start,
        end,
    ) in enumerate(selected, start=1):

        handle.write(
            f"region_{i}\t{chrom}\t{start}\t{end}\t"
            f"{length}\t{count}\n"
        )

print(out_file)
PY

tail -n +2 "${REGION_DIR}/selected_chr22_regions.tsv" |
while IFS=$'\t' read -r \
    REGION_ID CHROM START END LENGTH TRUTH_COUNT
do

    REGION="${CHROM}:${START}-${END}"

    BED_ONE="${REGION_DIR}/${REGION_ID}.bed"

    echo "============================================================"
    echo "[INFO] ${REGION_ID}: ${REGION}"

    printf "%s\t%s\t%s\n" \
        "${CHROM}" \
        "${START}" \
        "${END}" \
        > "${BED_ONE}"

    samtools view \
        -bh \
        "${BAM_URL}" \
        "${REGION}" \
        2> "${LOG_DIR}/${REGION_ID}.samtools_view.log" |
    samtools sort \
        -o "${BAM_DIR}/${REGION_ID}.sorted.bam" \
        2> "${LOG_DIR}/${REGION_ID}.samtools_sort.log"

    samtools index \
        "${BAM_DIR}/${REGION_ID}.sorted.bam"

    samtools flagstat \
        "${BAM_DIR}/${REGION_ID}.sorted.bam" \
        > "${LOG_DIR}/${REGION_ID}.flagstat.txt"

    BAM_READS=$(
        awk '/in total/{print $1; exit}' \
        "${LOG_DIR}/${REGION_ID}.flagstat.txt"
    )

    MAPPED_PCT=$(
        awk '/mapped \(/ && !/mate/ {
            gsub(/[()%]/,"",$5);
            print $5;
            exit
        }' "${LOG_DIR}/${REGION_ID}.flagstat.txt"
    )

    PROPER_PCT=$(
        awk '/properly paired/ {
            gsub(/[()%]/,"",$7);
            print $7;
            exit
        }' "${LOG_DIR}/${REGION_ID}.flagstat.txt"
    )

    bcftools view \
        -R "${BED_ONE}" \
        -Oz \
        -o "${VCF_DIR}/${REGION_ID}.truth.vcf.gz" \
        "${TRUTH_CHR22}"

    bcftools index \
        "${VCF_DIR}/${REGION_ID}.truth.vcf.gz"

    bcftools mpileup \
        -f "${REF}" \
        -r "${REGION}" \
        -d 1000 \
        -Ou \
        "${BAM_DIR}/${REGION_ID}.sorted.bam" |
    bcftools call \
        -mv \
        -Oz \
        -o "${VCF_DIR}/${REGION_ID}.raw.vcf.gz"

    bcftools index \
        "${VCF_DIR}/${REGION_ID}.raw.vcf.gz"

    bcftools filter \
        -i 'QUAL>=30 && DP>=10' \
        -Oz \
        -o "${VCF_DIR}/${REGION_ID}.filtered_QUAL30_DP10.vcf.gz" \
        "${VCF_DIR}/${REGION_ID}.raw.vcf.gz"

    bcftools index \
        "${VCF_DIR}/${REGION_ID}.filtered_QUAL30_DP10.vcf.gz"

    bcftools norm \
        -f "${REF}" \
        -m -both \
        -Oz \
        -o "${NORM_DIR}/${REGION_ID}.truth.norm.vcf.gz" \
        "${VCF_DIR}/${REGION_ID}.truth.vcf.gz"

    bcftools index \
        "${NORM_DIR}/${REGION_ID}.truth.norm.vcf.gz"

    bcftools norm \
        -f "${REF}" \
        -m -both \
        -Oz \
        -o "${NORM_DIR}/${REGION_ID}.filtered.norm.vcf.gz" \
        "${VCF_DIR}/${REGION_ID}.filtered_QUAL30_DP10.vcf.gz"

    bcftools index \
        "${NORM_DIR}/${REGION_ID}.filtered.norm.vcf.gz"

    RAW_CALLS=$(
        bcftools view -H \
        "${VCF_DIR}/${REGION_ID}.raw.vcf.gz" |
        wc -l
    )

    FILTERED_CALLS=$(
        bcftools view -H \
        "${VCF_DIR}/${REGION_ID}.filtered_QUAL30_DP10.vcf.gz" |
        wc -l
    )

    NORM_TRUTH=$(
        bcftools view -H \
        "${NORM_DIR}/${REGION_ID}.truth.norm.vcf.gz" |
        wc -l
    )

    NORM_PROJECT=$(
        bcftools view -H \
        "${NORM_DIR}/${REGION_ID}.filtered.norm.vcf.gz" |
        wc -l
    )

    rm -rf "${ISEC_DIR}/${REGION_ID}"

    mkdir -p "${ISEC_DIR}/${REGION_ID}"

    bcftools isec \
        -p "${ISEC_DIR}/${REGION_ID}" \
        "${NORM_DIR}/${REGION_ID}.truth.norm.vcf.gz" \
        "${NORM_DIR}/${REGION_ID}.filtered.norm.vcf.gz"

    TRUTH_ONLY=$(
        grep -vc '^#' \
        "${ISEC_DIR}/${REGION_ID}/0000.vcf"
    )

    PROJECT_ONLY=$(
        grep -vc '^#' \
        "${ISEC_DIR}/${REGION_ID}/0001.vcf"
    )

    SHARED=$(
        grep -vc '^#' \
        "${ISEC_DIR}/${REGION_ID}/0002.vcf"
    )

    read RECALL PRECISION F1 <<< "$(
        python3 - <<PY
truth_only = int("${TRUTH_ONLY}")
project_only = int("${PROJECT_ONLY}")
shared = int("${SHARED}")

recall = (
    shared / (shared + truth_only) * 100
    if shared + truth_only else 0
)

precision = (
    shared / (shared + project_only) * 100
    if shared + project_only else 0
)

f1 = (
    2 * precision * recall / (precision + recall)
    if precision + recall else 0
)

print(f"{recall:.2f} {precision:.2f} {f1:.2f}")
PY
)"

    echo -e \
"${REGION_ID}\t${REGION}\t${LENGTH}\t${TRUTH_COUNT}\t${BAM_READS}\t${MAPPED_PCT}\t${PROPER_PCT}\t${RAW_CALLS}\t${FILTERED_CALLS}\t${NORM_TRUTH}\t${NORM_PROJECT}\t${TRUTH_ONLY}\t${PROJECT_ONLY}\t${SHARED}\t${RECALL}\t${PRECISION}\t${F1}" \
        >> "${SUMMARY}"

done

echo "============================================================"
echo "[DONE] 25-region benchmark completed."
echo "============================================================"

cat "${SUMMARY}"
