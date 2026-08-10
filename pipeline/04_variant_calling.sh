#!/bin/bash

set -e

mkdir -p data/vcf logs

REF="data/reference/test_ref.fa"
BAM_DIR="data/bam"
VCF_DIR="data/vcf"

for BAM in ${BAM_DIR}/*.sorted.bam
do
    SAMPLE=$(basename "$BAM" .sorted.bam)

    bcftools mpileup -Ou -f ${REF} ${BAM} 2> logs/${SAMPLE}_mpileup.log | \
    bcftools call -mv -Oz -o ${VCF_DIR}/${SAMPLE}.raw.vcf.gz 2> logs/${SAMPLE}_bcftools_call.log

    tabix -p vcf ${VCF_DIR}/${SAMPLE}.raw.vcf.gz

    bcftools view ${VCF_DIR}/${SAMPLE}.raw.vcf.gz > ${VCF_DIR}/${SAMPLE}.raw.vcf
done

echo "Variant calling completed successfully."
