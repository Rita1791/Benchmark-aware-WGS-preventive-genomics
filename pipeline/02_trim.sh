#!/bin/bash

set -e

mkdir -p data/trimmed_fastq reports/fastp logs

RAW_DIR="data/raw_fastq"
TRIM_DIR="data/trimmed_fastq"

for R1 in ${RAW_DIR}/*_R1.fastq.gz
do
    SAMPLE=$(basename "$R1" _R1.fastq.gz)

    fastp \
        -i ${RAW_DIR}/${SAMPLE}_R1.fastq.gz \
        -o ${TRIM_DIR}/${SAMPLE}_R1.trimmed.fastq.gz \
        -h reports/fastp/${SAMPLE}_fastp.html \
        -j reports/fastp/${SAMPLE}_fastp.json \
        2>&1 | tee logs/${SAMPLE}_fastp.log
done

echo "Trimming completed successfully."
