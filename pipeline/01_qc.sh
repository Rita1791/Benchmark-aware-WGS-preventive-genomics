#!/bin/bash

set -e

mkdir -p reports/fastqc reports/multiqc logs

FASTQ_DIR="data/raw_fastq"

fastqc ${FASTQ_DIR}/*.fastq.gz -o reports/fastqc 2>&1 | tee logs/fastqc.log

multiqc reports/fastqc -o reports/multiqc 2>&1 | tee logs/multiqc.log

echo "QC completed successfully."
