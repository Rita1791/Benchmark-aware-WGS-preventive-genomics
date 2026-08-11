#!/usr/bin/env bash

set -euo pipefail

REFERENCE="${REFERENCE:-references/GRCh38.fa}"
TRIM_DIR="${TRIM_DIR:-data/trimmed_fastq}"
BAM_DIR="${BAM_DIR:-data/bam}"
QC_DIR="${QC_DIR:-results/alignment_qc}"

mkdir -p "${BAM_DIR}" "${QC_DIR}"

if [ ! -f "${REFERENCE}" ]; then
    echo "ERROR: Reference genome not found: ${REFERENCE}" >&2
    exit 1
fi

shopt -s nullglob
R1_FILES=("${TRIM_DIR}"/*_R1.trimmed.fastq.gz)

if [ "${#R1_FILES[@]}" -eq 0 ]; then
    echo "ERROR: No trimmed R1 FASTQ files found in ${TRIM_DIR}" >&2
    exit 1
fi

for R1 in "${R1_FILES[@]}"; do

    SAMPLE="$(basename "${R1}" _R1.trimmed.fastq.gz)"
    R2="${TRIM_DIR}/${SAMPLE}_R2.trimmed.fastq.gz"

    if [ ! -f "${R2}" ]; then
        echo "ERROR: Missing paired R2 file for ${SAMPLE}" >&2
        exit 1
    fi

    bwa-mem2 mem \
        "${REFERENCE}" \
        "${R1}" \
        "${R2}" \
        | samtools sort \
            -o "${BAM_DIR}/${SAMPLE}.sorted.bam" -

    samtools index \
        "${BAM_DIR}/${SAMPLE}.sorted.bam"

    samtools flagstat \
        "${BAM_DIR}/${SAMPLE}.sorted.bam" \
        > "${QC_DIR}/${SAMPLE}.flagstat.txt"

done

echo "Paired-end alignment completed successfully."
