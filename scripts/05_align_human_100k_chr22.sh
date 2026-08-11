#!/usr/bin/env bash
set -euo pipefail

# ============================================================
# Benchmark-aware WGS Preventive Genomics
# Step 05: 100k-read chr22 alignment
# ============================================================

SAMPLE="SRR2052337_100k_chr22"

R1="data/human_wgs_fastq_test/SRR2052337_1.fastq.gz"
R2="data/human_wgs_fastq_test/SRR2052337_2.fastq.gz"

REF="reference/GRCh38_chr22/chr22.fa"

OUTDIR="results/human_wgs_alignment_100k"
LOGDIR="logs/human_wgs_alignment_100k"

THREADS="${THREADS:-1}"
SORT_MEM="${SORT_MEM:-128M}"

BWA="${BWA:-bwa-mem2}"
SAMTOOLS="${SAMTOOLS:-samtools}"

mkdir -p "${OUTDIR}" "${LOGDIR}" "${OUTDIR}/tmp"

echo "============================================================"
echo "100k-read chr22 alignment"
echo "============================================================"

for tool in "${BWA}" "${SAMTOOLS}"; do
    if ! command -v "${tool}" >/dev/null 2>&1; then
        echo "[ERROR] Required tool not found: ${tool}"
        exit 1
    fi
done

for file in "${R1}" "${R2}" "${REF}"; do
    if [[ ! -f "${file}" ]]; then
        echo "[ERROR] Required input not found: ${file}"
        exit 1
    fi
done

BAM="${OUTDIR}/${SAMPLE}.sorted.bam"

"${BWA}" mem \
    -t "${THREADS}" \
    -K 1000000 \
    "${REF}" \
    "${R1}" \
    "${R2}" \
    2> "${LOGDIR}/${SAMPLE}.bwa.log" |
"${SAMTOOLS}" sort \
    -@ "${THREADS}" \
    -m "${SORT_MEM}" \
    -T "${OUTDIR}/tmp/${SAMPLE}" \
    -o "${BAM}" -

"${SAMTOOLS}" index "${BAM}"

"${SAMTOOLS}" flagstat \
    "${BAM}" \
    > "${OUTDIR}/${SAMPLE}.flagstat.txt"

"${SAMTOOLS}" stats \
    "${BAM}" \
    > "${OUTDIR}/${SAMPLE}.samtools_stats.txt"

"${SAMTOOLS}" idxstats \
    "${BAM}" \
    > "${OUTDIR}/${SAMPLE}.idxstats.txt"

echo "[DONE] chr22 100k-read alignment completed."
echo "[OUTPUT] ${BAM}"
