#!/usr/bin/env bash

set -euo pipefail

REFERENCE="${REFERENCE:-references/GRCh38.fa}"
BAM_DIR="${BAM_DIR:-data/bam}"
VCF_DIR="${VCF_DIR:-data/vcf}"
REGION="${REGION:-chr22}"

mkdir -p "${VCF_DIR}"

if [ ! -f "${REFERENCE}" ]; then
    echo "ERROR: Reference genome not found: ${REFERENCE}" >&2
    exit 1
fi

shopt -s nullglob
BAM_FILES=("${BAM_DIR}"/*.sorted.bam)

if [ "${#BAM_FILES[@]}" -eq 0 ]; then
    echo "ERROR: No BAM files found in ${BAM_DIR}" >&2
    exit 1
fi

for BAM in "${BAM_FILES[@]}"; do

    SAMPLE="$(basename "${BAM}" .sorted.bam)"

    bcftools mpileup \
        --fasta-ref "${REFERENCE}" \
        --regions "${REGION}" \
        --output-type u \
        "${BAM}" \
    | bcftools call \
        --multiallelic-caller \
        --variants-only \
        --output-type z \
        --output "${VCF_DIR}/${SAMPLE}.${REGION}.vcf.gz"

    bcftools index \
        "${VCF_DIR}/${SAMPLE}.${REGION}.vcf.gz"

done

echo "Variant calling completed successfully."
