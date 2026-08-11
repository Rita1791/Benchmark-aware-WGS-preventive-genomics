# WGS/NGS Pipeline Methodology

## Project Aim

This project develops and evaluates a reproducible whole-genome sequencing (WGS) variant-calling workflow using regional benchmarking against the Genome in a Bottle (GIAB) HG001 truth set.

The primary methodological objective is to determine how reliably the workflow identifies benchmark variants across selected GRCh38 chromosome 22 regions and to characterize the sources and patterns of remaining discrepancies.

The project focuses on:

- reproducible WGS preprocessing,
- read alignment,
- variant calling,
- VCF normalization,
- benchmark-aware variant comparison,
- formal benchmarking,
- regional performance evaluation,
- missed-variant analysis,
- low-recall region analysis,
- and comparison of record-level and formal benchmarking approaches.

---

## 1. Pipeline Overview

The principal workflow is:

```text
FASTQ
  |
  v
Raw Read Quality Control
  |
  v
Read Trimming / Preprocessing
  |
  v
Post-processing Quality Control
  |
  v
Reference Genome Preparation
  |
  v
Read Alignment
  |
  v
BAM Sorting and Indexing
  |
  v
Alignment Quality Assessment
  |
  v
Variant Calling
  |
  v
VCF Normalization
  |
  +-----------------------------+
  |                             |
  v                             v
bcftools isec              RTG vcfeval
  |                             |
  +-------------+---------------+
                |
                v
        Benchmark Comparison
                |
                v
   Missed-Variant Analysis
                |
                v
    Low-Recall Region Analysis
                |
                v
    Benchmark-Scale Comparison
                |
                v
       Publication-Ready
       Tables and Figures
