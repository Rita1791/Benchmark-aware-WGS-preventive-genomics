# Dataset Validation Decision: ERR6090673

Date: 2026-08-07
Reviewer: Ritika
Project: Nainfit NGS/WGS Research Pipeline

## Dataset Checked
Run accession: ERR6090673

## Metadata Result
- Scientific name: marine metagenome
- Library strategy: AMPLICON
- Library source: METAGENOMIC
- Library selection: PCR
- Library layout: PAIRED
- Instrument platform: ILLUMINA
- Instrument model: Illumina HiSeq 2500

## Decision
ERR6090673 is rejected for the final Nainfit human WGS research pipeline.

## Reason
The dataset is not Homo sapiens, not WGS, and not human genomic DNA sequencing. It is a marine metagenomic amplicon sequencing dataset. Therefore, it is not scientifically suitable for human WGS variant calling, GIAB benchmarking, diabetes/metabolic-health interpretation, or Nainfit preventive genomics output generation.

## Correct Next Strategy
Switch to GIAB HG001 / NA12878 benchmark-compatible data.

Preferred next route:
Controlled GIAB/HG001 BAM-derived regional FASTQ validation.

## Scientific Rationale
The controlled GIAB/HG001 regional FASTQ route allows us to test the FASTQ-to-BAM-to-VCF execution path while keeping the sample identity and benchmark truth consistent with the existing GIAB HG001 chr22 validation study.

## Publication Note
ERR6090673 must not be used in final analysis. It can be mentioned only in the lab notebook as an excluded dataset after metadata validation.
