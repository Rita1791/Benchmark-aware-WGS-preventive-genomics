#!/usr/bin/env bash
set -euo pipefail

# ============================================================
# Benchmark-aware WGS Preventive Genomics
# Step 03: Full-reference paired-end alignment
#
# FASTQ -> bwa-mem2 -> coordinate-sorted BAM -> BAM index
# -> alignment QC
# ============================================================

SAMPLE="SRR4420293"

R1="data/real_trimmed_fastq/SRR4420293_1.trimmed.fastq.gz"
R2="data/real_trimmed_fastq/SRR4420293_2.trimmed.fastq.gz"

REF="reference/GRCh38/Homo_sapiens_assembly38.fasta"

OUTDIR="results/alignment"
LOGDIR="logs/alignment"

THREADS="${THREADS:-1}"
SORT_MEM="${SORT_MEM:-128M}"

BWA="${BWA:-bwa-mem2}"
SAMTOOLS="${SAMTOOLS:-samtools}"

mkdir -p "${OUTDIR}" "${LOGDIR}"

echo "============================================================"
echo "Full-reference alignment"
echo "============================================================"
echo "[INFO] Sample: ${SAMPLE}"
echo "[INFO] R1: ${R1}"
echo "[INFO] R2: ${R2}"
echo "[INFO] Reference: ${REF}"
echo "[INFO] Threads: ${THREADS}"
echo "[INFO] Sort memory/thread: ${SORT_MEM}"

# ------------------------------------------------------------
# Dependency checks
# ------------------------------------------------------------

if ! command -v "${BWA}" >/dev/null 2>&1; then
    echo "[ERROR] bwa-mem2 not found: ${BWA}"
    exit 1
fi

if ! command -v "${SAMTOOLS}" >/dev/null 2>&1; then
    echo "[ERROR] samtools not found: ${SAMTOOLS}"
    exit 1
fi

# ------------------------------------------------------------
# Input validation
# ------------------------------------------------------------

for file in "${R1}" "${R2}" "${REF}"; do
    if [[ ! -f "${file}" ]]; then
        echo "[ERROR] Required input not found: ${file}"
        exit 1
    fi
done

# ------------------------------------------------------------
# Reference index
# ------------------------------------------------------------

if [[ ! -f "${REF}.0123" ]]; then
    echo "[INFO] bwa-mem2 index not found."
    echo "[INFO] Creating index..."

    "${BWA}" index "${REF}" \
        > "${LOGDIR}/${SAMPLE}_bwa_index.log" 2>&1
else
    echo "[INFO] bwa-mem2 index detected."
fi

# ------------------------------------------------------------
# Output paths
# ------------------------------------------------------------

BAM="${OUTDIR}/${SAMPLE}.sorted.bam"
BAI="${BAM}.bai"

FLAGSTAT="${OUTDIR}/${SAMPLE}.flagstat.txt"
STATS="${OUTDIR}/${SAMPLE}.samtools_stats.txt"
IDXSTATS="${OUTDIR}/${SAMPLE}.idxstats.txt"

# ------------------------------------------------------------
# Alignment
# ------------------------------------------------------------

echo "[INFO] Running bwa-mem2..."

"${BWA}" mem \
    -t "${THREADS}" \
    -K 1000000 \
    "${REF}" \
    "${R1}" \
    "${R2}" \
    2> "${LOGDIR}/${SAMPLE}_bwa_mem.log" \
|
"${SAMTOOLS}" sort \
    -@ "${THREADS}" \
    -m "${SORT_MEM}" \
    -T "${OUTDIR}/${SAMPLE}.tmp" \
    -o "${BAM}" -

# ------------------------------------------------------------
# BAM indexing
# ------------------------------------------------------------

echo "[INFO] Indexing BAM..."

"${SAMTOOLS}" index "${BAM}"

# ------------------------------------------------------------
# Alignment QC
# ------------------------------------------------------------

echo "[INFO] Generating flagstat..."

"${SAMTOOLS}" flagstat \
    "${BAM}" \
    > "${FLAGSTAT}"

echo "[INFO] Generating samtools stats..."

"${SAMTOOLS}" stats \
    "${BAM}" \
    > "${STATS}"

echo "[INFO] Generating idxstats..."

"${SAMTOOLS}" idxstats \
    "${BAM}" \
    > "${IDXSTATS}"

# ------------------------------------------------------------
# Completion
# ------------------------------------------------------------

echo "============================================================"
echo "[DONE] Full-reference alignment completed."
echo "============================================================"

echo "[OUTPUT] ${BAM}"
echo "[OUTPUT] ${BAI}"
echo "[OUTPUT] ${FLAGSTAT}"
echo "[OUTPUT] ${STATS}"
echo "[OUTPUT] ${IDXSTATS}"
