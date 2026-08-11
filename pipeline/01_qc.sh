#!/usr/bin/env bash

set -euo pipefail

RAW_DIR="${RAW_DIR:-data/raw_fastq}"
QC_DIR="${QC_DIR:-results/qc}"

FASTQC_DIR="${QC_DIR}/fastqc"
MULTIQC_DIR="${QC_DIR}/multiqc"

mkdir -p "${FASTQC_DIR}" "${MULTIQC_DIR}"

shopt -s nullglob
FASTQ_FILES=("${RAW_DIR}"/*.fastq.gz)

if [ "${#FASTQ_FILES[@]}" -eq 0 ]; then
    echo "ERROR: No FASTQ files found in ${RAW_DIR}" >&2
    exit 1
fi

fastqc \
    "${FASTQ_FILES[@]}" \
    --outdir "${FASTQC_DIR}"

multiqc \
    "${FASTQC_DIR}" \
    --outdir "${MULTIQC_DIR}"

echo "QC completed successfully."
