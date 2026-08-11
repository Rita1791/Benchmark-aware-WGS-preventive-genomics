# 🧬 Benchmark-Aware Regional Validation of a Reproducible WGS Variant-Calling Workflow

<p align="center">

**GIAB HG001 · GRCh38 · chr22 · WGS · Variant Calling · Benchmarking · Reproducible Bioinformatics**

</p>

<p align="center">

[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Benchmark](https://img.shields.io/badge/Benchmark-GIAB%20HG001-blue.svg)](config/benchmark.yaml)
[![Reference](https://img.shields.io/badge/Reference-GRCh38-orange.svg)](config/benchmark.yaml)
[![Chromosome](https://img.shields.io/badge/Chromosome-chr22-purple.svg)](config/benchmark.yaml)
[![Python](https://img.shields.io/badge/Python-3.11-blue.svg)](environment.yml)
[![Status](https://img.shields.io/badge/Status-Active%20Research-success.svg)](#-project-status)

</p>

<p align="center">

> **A benchmark-aware computational genomics framework for evaluating WGS variant-calling performance across progressively expanded GIAB HG001 high-confidence regions of GRCh38 chromosome 22.**

</p>

---

## 🧭 Navigation

- [🔬 About This Research](#-about-this-research)
- [🎯 Research Question](#-research-question)
- [🧬 Research Objectives](#-research-objectives)
- [🧪 Study Design](#-study-design)
- [🔬 Computational Workflow](#-computational-workflow)
- [📏 Benchmark-Scale Evaluation](#-benchmark-scale-evaluation)
- [📊 Key Results](#-key-results)
- [🧪 Formal RTG Benchmark](#-formal-rtg-vcfeval-benchmark)
- [⚖️ Benchmark Method Comparison](#️-normalized-comparison-vs-formal-benchmarking)
- [🔎 Missed-Variant Analysis](#-missed-variant-analysis)
- [📍 Low-Recall Analysis](#-low-recall-regional-analysis)
- [🧩 Error Characterization](#-error-and-discrepancy-analysis)
- [📈 Publication Outputs](#-publication-ready-outputs)
- [🧰 Software](#-software-and-tools)
- [♻️ Reproducibility](#️-reproducibility)
- [🗂️ Repository Structure](#️-repository-structure)
- [👩‍🔬 Researcher](#-about-the-researcher)
- [🧭 Research Perspective](#-research-perspective)
- [⚠️ Limitations](#️-scope-and-limitations)
- [🚀 Future Research](#-future-research)
- [🏢 Acknowledgement](#-acknowledgement)
- [📚 Documentation](#-documentation)
- [📖 Citation](#-citation)
- [📄 License](#-license)

---

# 🧭 Project at a Glance

| Category | Details |
|---|---|
| **Research area** | Computational Genomics |
| **Primary application** | WGS Variant Calling and Benchmarking |
| **Benchmark resource** | Genome in a Bottle (GIAB) |
| **Benchmark sample** | HG001 |
| **Alternate identifier** | NA12878 |
| **Reference genome** | GRCh38 |
| **Primary chromosome** | chr22 |
| **Benchmark release** | GIAB v4.2.1 |
| **Validation scales** | 5, 25, and 50 regions |
| **Normalized comparison** | `bcftools isec` |
| **Formal benchmark** | RTG `vcfeval` |
| **Low-recall threshold** | 92% |
| **Primary analysis** | Regional benchmark validation |
| **Research status** | Active computational research |

---

# 🔬 About This Research

Whole-genome sequencing (WGS) variant calling is a fundamental component of modern computational genomics. However, generating a VCF file is not sufficient to establish that the detected variants are reliable.

A variant-calling workflow should be evaluated against an independent benchmark to determine:

- how many expected variants are recovered;
- how many additional variants are reported;
- whether performance changes across genomic regions;
- which variant classes contribute to residual errors;
- whether difficult genomic contexts affect sensitivity;
- whether simple VCF concordance agrees with formal benchmark evaluation.

This project was developed as a **benchmark-aware regional validation framework** for evaluating WGS variant-calling performance.

The study uses:

- **Genome in a Bottle (GIAB) HG001**
- **GRCh38**
- **chromosome 22**
- selected GIAB high-confidence benchmark regions.

Rather than reporting only a single aggregate accuracy value, the project progressively evaluates the workflow across increasingly larger regional benchmark scopes.

## 🔎 Analytical Strategy

```text
                    WGS DATA
                       │
                       ▼
                Quality Control
                       │
                       ▼
                Read Processing
                       │
                       ▼
                  Alignment
                       │
                       ▼
                Variant Calling
                       │
                       ▼
              VCF Normalization
                       │
                       ▼
              GIAB HG001 Truth Set
                       │
          ┌────────────┴────────────┐
          ▼                         ▼
    5-region                  25-region
    validation                validation
          │                         │
          └────────────┬────────────┘
                       ▼
                  50-region
                  validation
                       │
             ┌─────────┴─────────┐
             ▼                   ▼
      bcftools isec         RTG vcfeval
       comparison             formal
                              benchmark
             │                   │
             └─────────┬─────────┘
                       ▼
             Error Characterization
                       │
          ┌────────────┼────────────┐
          ▼            ▼            ▼
     Missed         Low-recall   Method
     variants        regions    discrepancy
          │            │            │
          └────────────┼────────────┘
                       ▼
             Publication Outputs
