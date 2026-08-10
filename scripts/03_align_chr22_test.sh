#!/usr/bin/env bash
set -euo pipefail

# =========================================================
# Nainfit Swiss-Level WGS/NGS Research Pipeline
# Step 03: Resource-Controlled chr22 Alignment Test
#
# Purpose:
# FASTQ -> aligned SAM stream -> sorted BAM -> BAM index -> QC metrics
#
# Why:
# This tests whether the alignment pipeline is technically stable
# before full GRCh38 alignment.
# =========================================================

SAMPLE="SRR4420293_chr22_test"

R1="data/real_trimmed_fastq/SRR4420293_1.trimmed.fastq.gz"
R2="data/real_trimmed_fastq/SRR4420293_2.trimmed.fastq.gz"

REF="reference/GRCh38_chr22/chr22.fa"

OUTDIR="results/alignment"
LOGDIR="logs"

THREADS=1
SORT_MEM="128M"

BWA="bwa-mem2"
SAMTOOLS="/usr/bin/samtools"

mkdir -p "${OUTDIR}" "${LOGDIR}"

echo "[INFO] Starting resource-controlled chr22 alignment"
echo "[INFO] Sample: ${SAMPLE}"
echo "[INFO] R1: ${R1}"
echo "[INFO] R2: ${R2}"
echo "[INFO] REF: ${REF}"
echo "[INFO] Threads: ${THREADS}"
echo "[INFO] Samtools sort memory per thread: ${SORT_MEM}"
echo "[INFO] bwa-mem2 path: $(which ${BWA})"
echo "[INFO] samtools path: ${SAMTOOLS}"

if [[ ! -f "${R1}" ]]; then
  echo "[ERROR] R1 not found: ${R1}"
  exit 1
fi

if [[ ! -f "${R2}" ]]; then
  echo "[ERROR] R2 not found: ${R2}"
  exit 1
fi

if [[ ! -f "${REF}" ]]; then
  echo "[ERROR] Reference not found: ${REF}"
  exit 1
fi

if [[ ! -x "${SAMTOOLS}" ]]; then
  echo "[ERROR] /usr/bin/samtools not executable"
  exit 1
fi

echo "[INFO] Tool versions:"
${BWA} version 2>&1 | head -5
${SAMTOOLS} --version | head -3

if [[ ! -f "${REF}.0123" ]]; then
  echo "[INFO] bwa-mem2 index not found. Creating index..."
  ${BWA} index "${REF}" 2>&1 | tee "${LOGDIR}/${SAMPLE}_bwa_index.log"
else
  echo "[INFO] bwa-mem2 index already exists."
fi

echo "[INFO] Removing old incomplete output if present..."
rm -f "${OUTDIR}/${SAMPLE}.sorted.bam" \
      "${OUTDIR}/${SAMPLE}.sorted.bam.bai" \
      "${OUTDIR}/${SAMPLE}.flagstat.txt" \
      "${OUTDIR}/${SAMPLE}.samtools_stats.txt"

echo "[INFO] Running alignment with strict low-memory settings..."

${BWA} mem \
  -t "${THREADS}" \
  -K 1000000 \
  "${REF}" "${R1}" "${R2}" \
  2> "${LOGDIR}/${SAMPLE}_bwa_mem.log" \
  | ${SAMTOOLS} sort \
      -@ "${THREADS}" \
      -m "${SORT_MEM}" \
      -T "${OUTDIR}/${SAMPLE}.tmp" \
      -o "${OUTDIR}/${SAMPLE}.sorted.bam" -

echo "[INFO] Indexing BAM..."
${SAMTOOLS} index "${OUTDIR}/${SAMPLE}.sorted.bam"

echo "[INFO] Generating alignment QC reports..."
${SAMTOOLS} flagstat "${OUTDIR}/${SAMPLE}.sorted.bam" > "${OUTDIR}/${SAMPLE}.flagstat.txt"
${SAMTOOLS} stats "${OUTDIR}/${SAMPLE}.sorted.bam" > "${OUTDIR}/${SAMPLE}.samtools_stats.txt"

echo "[DONE] chr22 test alignment completed successfully."
echo "[OUTPUT] ${OUTDIR}/${SAMPLE}.sorted.bam"
echo "[OUTPUT] ${OUTDIR}/${SAMPLE}.sorted.bam.bai"
echo "[OUTPUT] ${OUTDIR}/${SAMPLE}.flagstat.txt"
echo "[OUTPUT] ${OUTDIR}/${SAMPLE}.samtools_stats.txt"
