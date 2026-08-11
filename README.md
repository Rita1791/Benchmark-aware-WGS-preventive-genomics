# Benchmark-Aware Regional Validation of a Reproducible WGS Variant-Calling Workflow

### GIAB HG001 • GRCh38 • chr22 • WGS • Variant Calling • Benchmarking • Reproducible Bioinformatics

[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Benchmark: GIAB HG001](https://img.shields.io/badge/Benchmark-GIAB%20HG001-blue.svg)](config/benchmark.yaml)
[![Reference: GRCh38](https://img.shields.io/badge/Reference-GRCh38-orange.svg)](config/benchmark.yaml)
[![Python: 3.11](https://img.shields.io/badge/Python-3.11-blue.svg)](environment.yml)

> A reproducible computational genomics study evaluating WGS variant-calling performance against the Genome in a Bottle (GIAB) HG001 benchmark across progressively expanded high-confidence regions of GRCh38 chromosome 22.

---

## 🔬 About This Research

Whole-genome sequencing (WGS) variant calling is a fundamental component of modern computational genomics. However, generating a VCF file is not sufficient to establish that the detected variants are reliable.

A variant-calling workflow must be evaluated against an independent benchmark to determine:

- how many expected variants are recovered,
- how many incorrect variants are introduced,
- whether performance changes across genomic regions,
- which variant classes contribute to residual errors,
- and whether simple VCF concordance agrees with formal benchmark evaluation.

This project was developed to investigate these questions through a **benchmark-aware, regional validation framework**.

The study uses the **Genome in a Bottle (GIAB) HG001 benchmark**, the **GRCh38 reference genome**, and selected high-confidence regions of **chromosome 22**.

Rather than reporting only one aggregate accuracy value, the analysis progressively evaluates:

```text
5 benchmark regions
        ↓
25 benchmark regions
        ↓
50 benchmark regions
        ↓
Formal RTG benchmarking
        ↓
Missed-variant analysis
        ↓
Low-recall regional analysis
        ↓
Benchmark-method discrepancy analysis
