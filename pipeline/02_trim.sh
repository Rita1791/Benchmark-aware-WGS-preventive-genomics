#!/usr/bin/env bash

set -euo pipefail

RAW_DIR="${RAW_DIR:-data/raw_fastq}"
TRIM_DIR="${TRIM_DIR:-data/trimmed_fastq}"
REPORT_DIR="${REPORT_DIR:-results/fastp}"

mkdir -p "${TRIM_DIR}" "${REPORT_DIR}"

shopt -s nullglob
R1_FILES=("${RAW_DIR}"/*_R1.fastq.gz)

if [ "${#R1_FILES[@]}" -eq 0 ]; then
    echo "ERROR: No *_R1.fastq.gz files found in ${RAW_DIR}" >&2
    exit 1
fi

for R1 in "${R1_FILES[@]}"; do

    SAMPLE="$(basename "${R1}" _R1.fastq.gz)"
    R2="${RAW_DIR}/${SAMPLE}_R2.fastq.gz"

    if [ ! -f "${R2}" ]; then
        echo "ERROR: Missing paired R2 file for ${SAMPLE}" >&2
        exit 1
    fi

    fastp \
        --in1 "${R1}" \
        --in2 "${R2}" \
        --out1 "${TRIM_DIR}/${SAMPLE}_R1.trimmed.fastq.gz" \
        --out2 "${TRIM_DIR}/${SAMPLE}_R2.trimmed.fastq.gz" \
        --html "${REPORT_DIR}/${SAMPLE}_fastp.html" \
        --json "${REPORT_DIR}/${SAMPLE}_fastp.json"

done

echo "Paired-end trimming completed successfully."
