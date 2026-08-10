#!/usr/bin/env bash
set -euo pipefail

# ==============================
# Nainfit WGS Research Pipeline
# Step 03: Alignment
# FASTQ -> sorted BAM -> BAM index -> alignment stats
# ==============================

SAMPLE="SRR4420293"

# Edit these paths if your files are in different folders
R1="data/trimmed/SRR4420293_1.trimmed.fastq.gz"
R2="data/trimmed/SRR4420293_2.trimmed.fastq.gz"

# Edit this path according to your reference genome file
REF="reference/GRCh38/Homo_sapiens_assembly38.fasta"

OUTDIR="results/alignment"
LOGDIR="logs"

THREADS=8

mkdir -p "${OUTDIR}" "${LOGDIR}"

echo "[INFO] Starting alignment for ${SAMPLE}"
echo "[INFO] R1: ${R1}"
echo "[INFO] R2: ${R2}"
echo "[INFO] REF: ${REF}"
echo "[INFO] THREADS: ${THREADS}"

# Check input files
if [[ ! -f "${R1}" ]]; then
  echo "[ERROR] R1 file not found: ${R1}"
  exit 1
fi

if [[ ! -f "${R2}" ]]; then
  echo "[ERROR] R2 file not found: ${R2}"
  exit 1
fi

if [[ ! -f "${REF}" ]]; then
  echo "[ERROR] Reference genome not found: ${REF}"
  exit 1
fi

# Check reference index
if [[ ! -f "${REF}.0123" && ! -f "${REF}.bwt.2bit.64" ]]; then
  echo "[INFO] bwa-mem2 index not found. Creating index..."
  bwa-mem2 index "${REF}" 2>&1 | tee "${LOGDIR}/${SAMPLE}_bwa_index.log"
else
  echo "[INFO] bwa-mem2 index found."
fi

# Alignment + BAM sorting
echo "[INFO] Running bwa-mem2 alignment and samtools sorting..."

bwa-mem2 mem -t "${THREADS}" "${REF}" "${R1}" "${R2}" \
  2> "${LOGDIR}/${SAMPLE}_bwa_mem.log" \
  | samtools sort -@ "${THREADS}" -o "${OUTDIR}/${SAMPLE}.sorted.bam" -

# BAM index
echo "[INFO] Indexing BAM..."
samtools index "${OUTDIR}/${SAMPLE}.sorted.bam"

# Alignment statistics
echo "[INFO] Generating flagstat..."
samtools flagstat "${OUTDIR}/${SAMPLE}.sorted.bam" > "${OUTDIR}/${SAMPLE}.flagstat.txt"

echo "[INFO] Generating samtools stats..."
samtools stats "${OUTDIR}/${SAMPLE}.sorted.bam" > "${OUTDIR}/${SAMPLE}.samtools_stats.txt"

echo "[INFO] Alignment completed successfully."
echo "[OUTPUT] ${OUTDIR}/${SAMPLE}.sorted.bam"
echo "[OUTPUT] ${OUTDIR}/${SAMPLE}.sorted.bam.bai"
echo "[OUTPUT] ${OUTDIR}/${SAMPLE}.flagstat.txt"
echo "[OUTPUT] ${OUTDIR}/${SAMPLE}.samtools_stats.txt"
