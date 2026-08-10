#!/usr/bin/env bash
set -euo pipefail

SAMPLE="SRR2052337_1M_chr22"

R1="data/human_wgs_fastq_1M/SRR2052337_1.fastq.gz"
R2="data/human_wgs_fastq_1M/SRR2052337_2.fastq.gz"

REF="reference/GRCh38_chr22/chr22.fa"

OUTDIR="results/human_wgs_alignment_1M_chr22"
LOGDIR="logs/human_wgs_alignment_1M_chr22"

THREADS=1
SORT_MEM="128M"

mkdir -p "$OUTDIR" "$LOGDIR" "$OUTDIR/tmp"

echo "[INFO] Sample: $SAMPLE"
echo "[INFO] R1: $R1"
echo "[INFO] R2: $R2"
echo "[INFO] Reference: $REF"
echo "[INFO] Threads: $THREADS"
echo "[INFO] Sort memory: $SORT_MEM"

bwa-mem2 mem \
  -t "$THREADS" \
  -K 1000000 \
  "$REF" \
  "$R1" \
  "$R2" \
  2> "$LOGDIR/${SAMPLE}.bwa.log" \
| /usr/bin/samtools sort \
  -@ "$THREADS" \
  -m "$SORT_MEM" \
  -T "$OUTDIR/tmp/${SAMPLE}" \
  -o "$OUTDIR/${SAMPLE}.sorted.bam" \
  2> "$LOGDIR/${SAMPLE}.samtools_sort.log"

/usr/bin/samtools index "$OUTDIR/${SAMPLE}.sorted.bam"

/usr/bin/samtools flagstat \
  "$OUTDIR/${SAMPLE}.sorted.bam" \
  > "$OUTDIR/${SAMPLE}.flagstat.txt"

/usr/bin/samtools stats \
  "$OUTDIR/${SAMPLE}.sorted.bam" \
  > "$OUTDIR/${SAMPLE}.samtools_stats.txt"

/usr/bin/samtools idxstats \
  "$OUTDIR/${SAMPLE}.sorted.bam" \
  > "$OUTDIR/${SAMPLE}.idxstats.txt"

echo "[DONE] Alignment completed."
echo "[DONE] Output BAM: $OUTDIR/${SAMPLE}.sorted.bam"
