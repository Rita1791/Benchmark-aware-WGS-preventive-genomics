#!/bin/bash

set -e

mkdir -p data/bam logs

REF="data/reference/test_ref.fa"
TRIM_DIR="data/trimmed_fastq"
BAM_DIR="data/bam"

for R1 in ${TRIM_DIR}/*_R1.trimmed.fastq.gz
do
    SAMPLE=$(basename "$R1" _R1.trimmed.fastq.gz)

    bwa-mem2 mem ${REF} ${R1} \
        2> logs/${SAMPLE}_bwa.log | \
        samtools sort -o ${BAM_DIR}/${SAMPLE}.sorted.bam

    samtools index ${BAM_DIR}/${SAMPLE}.sorted.bam

    samtools flagstat ${BAM_DIR}/${SAMPLE}.sorted.bam > logs/${SAMPLE}_flagstat.txt
done

echo "Alignment completed successfully."
