#!/bin/bash

set -e

mkdir -p data/real_trimmed_fastq reports/real_fastp logs

fastp \
  -i data/public_dataset/SRR4420293_1.fastq.gz \
  -I data/public_dataset/SRR4420293_2.fastq.gz \
  -o data/real_trimmed_fastq/SRR4420293_1.trimmed.fastq.gz \
  -O data/real_trimmed_fastq/SRR4420293_2.trimmed.fastq.gz \
  -h reports/real_fastp/SRR4420293_fastp.html \
  -j reports/real_fastp/SRR4420293_fastp.json \
  2>&1 | tee logs/SRR4420293_fastp.log

echo "Real paired-end trimming completed."
