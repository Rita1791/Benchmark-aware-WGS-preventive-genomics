# WGS/NGS Pipeline Methodology

## Project Aim
To build a reproducible computational genomics workflow for processing raw sequencing reads into variant-level outputs suitable for downstream SNP interpretation and precision health research.

## Pipeline Overview

FASTQ
↓
Quality Control
↓
Read Trimming
↓
Post-Trimming QC
↓
Reference Genome Preparation
↓
Alignment
↓
BAM Sorting and Indexing
↓
Alignment Quality Assessment
↓
Variant Calling
↓
VCF Filtering
↓
Variant Annotation
↓
SNP Extraction
↓
Evidence-Graded Interpretation

## Core Tools

| Stage | Tool |
|---|---|
| Raw FASTQ Quality Control | FastQC |
| QC Aggregation | MultiQC |
| Read Trimming | fastp |
| Alignment | bwa-mem2 |
| BAM Processing | samtools |
| Variant Calling | bcftools / GATK / DeepVariant |
| Annotation | SnpEff / VEP |
| Benchmarking | GIAB / hap.py later |

## Research Design Principle
The pipeline will be developed in stages:

1. Small controlled test
2. Subsampled dataset
3. Full reference alignment
4. Variant calling
5. Annotation
6. Validation

This staged strategy reduces computational failure and improves reproducibility.

## Current Development Stage
The chr22 alignment test has confirmed that the alignment module can generate a sorted BAM, BAM index, flagstat, and samtools statistics under low-memory local conditions.

## Next Stage
Controlled subsampling followed by full-reference alignment strategy.

---

## Human WGS Benchmark Dataset Requirement

After metadata verification, SRR4420293 was excluded from the human WGS workflow because it was Arabidopsis thaliana RNA-seq.

The main WGS/NGS variant discovery workflow will now use a verified human benchmark dataset.

Preferred benchmark resource:
- Genome in a Bottle (GIAB)

Preferred first sample:
- HG001 / NA12878

Reason:
GIAB datasets are designed for benchmarking human genome sequencing workflows and allow future comparison against high-confidence variant truth sets.
