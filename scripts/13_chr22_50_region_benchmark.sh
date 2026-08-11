#!/usr/bin/env bash
set -euo pipefail

# ============================================================
# Benchmark-aware WGS Preventive Genomics
# 50-region GIAB HG001 chr22 benchmark
# ============================================================

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "${ROOT_DIR}"

BAM_URL="https://ftp-trace.ncbi.nlm.nih.gov/ReferenceSamples/giab/data/NA12878/NIST_NA12878_HiSeq_300x/NHGRI_Illumina300X_novoalign_bams/HG001.GRCh38_full_plus_hs38d1_analysis_set_minus_alts.300x.bam"

REF="reference/GRCh38_chr22/chr22.fa"

TRUTH_CHR22="reference_datasets/giab_truth/HG001_GRCh38_chr22/HG001_GRCh38_chr22_v4.2.1_benchmark_CONFIDENT.vcf.gz"

BED_CHR22="reference_datasets/giab_truth/HG001_GRCh38_chr22/HG001_GRCh38_chr22_v4.2.1_benchmark.bed"

OUTDIR="results/benchmark_valid_chr22_50_region"

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
