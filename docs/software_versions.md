# Software Versions

## Purpose

This document records the software environment used for the WGS benchmarking workflow.

Software versions are intentionally reported only when verified from the computational environment used for the analysis. Versions are not inferred from package-manager defaults or documentation.

---

## Core tools

| Software | Role | Version | Status |
|---|---|---|---|
| Python | Workflow scripting and analysis | TBD | To be verified |
| FastQC | Read quality control | TBD | To be verified |
| fastp | Read preprocessing and trimming | TBD | To be verified |
| MultiQC | Aggregated QC reporting | TBD | To be verified |
| BWA-MEM2 | Short-read alignment | TBD | To be verified |
| samtools | BAM/SAM processing and QC | TBD | To be verified |
| bcftools | Variant calling, normalization, and comparison | TBD | To be verified |
| HTSlib | Variant/alignment file support | TBD | To be verified |
| RTG Tools | Formal variant benchmarking | TBD | To be verified |

---

## Python packages

| Package | Role | Version | Status |
|---|---|---|---|
| pandas | Tabular data processing | TBD | To be verified |
| numpy | Numerical analysis | TBD | To be verified |
| matplotlib | Figure generation | TBD | To be verified |
| PyYAML | YAML configuration parsing | TBD | To be verified |

---

## Environment definition

The repository provides a Conda environment specification in:

```text
environment.yml
