# 🧬 Benchmark-Aware Regional Validation of a Reproducible WGS Variant-Calling Workflow

<p align="center">

**GIAB HG001 · GRCh38 · chr22 · Whole-Genome Sequencing · Variant Calling · Benchmarking · Reproducible Bioinformatics**

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

### A benchmark-aware regional validation framework for reproducible WGS variant-calling analysis.

</p>

---

## 🧭 Table of Contents

- [🔬 About This Research](#-about-this-research)
- [🎯 Research Question](#-research-question)
- [🧬 Research Objectives](#-research-objectives)
- [🧪 Study Design](#-study-design)
- [🧬 Benchmark Framework](#-benchmark-framework)
- [🔬 Computational Workflow](#-computational-workflow)
- [📏 Benchmark-Scale Evaluation](#-benchmark-scale-evaluation)
- [📊 Key Results](#-key-results)
- [🧪 Formal RTG vcfeval Benchmark](#-formal-rtg-vcfeval-benchmark)
- [⚖️ Normalized Comparison vs Formal Benchmarking](#️-normalized-comparison-vs-formal-benchmarking)
- [🔎 Missed-Variant Analysis](#-missed-variant-analysis)
- [📍 Low-Recall Regional Analysis](#-low-recall-regional-analysis)
- [🧩 Error and Discrepancy Analysis](#-error-and-discrepancy-analysis)
- [📈 Publication-Ready Outputs](#-publication-ready-outputs)
- [🧰 Software and Tools](#-software-and-tools)
- [♻️ Reproducibility](#-reproducibility)
- [🗂️ Repository Structure](#️-repository-structure)
- [👥 Contributors](#-contributors)
- [👩‍🔬 About the Researcher](#-about-the-researcher)
- [🧭 Research Perspective](#-research-perspective)
- [🔬 Research Lifecycle](#-research-lifecycle)
- [⚠️ Scope and Limitations](#️-scope-and-limitations)
- [🚀 Future Research](#-future-research)
- [🏢 Acknowledgement](#-acknowledgement)
- [📚 Documentation](#-documentation)
- [📖 Citation](#-citation)
- [📄 License](#-license)
- [📊 Project Status](#-project-status)

---

## 🧭 Project at a Glance

| Category | Details |
|---|---|
| **Research Area** | Computational Genomics |
| **Primary Application** | WGS Variant Calling & Benchmarking |
| **Benchmark Resource** | Genome in a Bottle (GIAB) |
| **Benchmark Sample** | HG001 |
| **Alternate Identifier** | NA12878 |
| **Reference Genome** | GRCh38 |
| **Primary Chromosome** | chr22 |
| **Benchmark Release** | GIAB v4.2.1 |
| **Validation Scales** | 5, 25, and 50 regions |
| **Normalized Comparison** | `bcftools isec` |
| **Formal Benchmark** | RTG `vcfeval` |
| **Low-Recall Threshold** | 92% |
| **Primary Analysis** | Regional Benchmark Validation |
| **Research Status** | Active Computational Research |

---

## 🔬 About This Research

This project evaluates the performance and reproducibility of a whole-genome sequencing (WGS) variant-calling workflow using the **Genome in a Bottle (GIAB) HG001 benchmark sample** and high-confidence regions on **GRCh38 chromosome 22**.

Rather than treating variant calling as a single end-to-end score, the project investigates how workflow performance varies across genomic regions and how different benchmarking approaches influence the interpretation of sensitivity, precision, and overall variant-calling performance.

The analysis therefore combines:

- reproducible WGS preprocessing,
- quality control,
- sequence alignment,
- BAM processing,
- variant calling,
- VCF normalization and filtering,
- regional benchmarking,
- formal benchmarking with RTG `vcfeval`,
- variant-set comparison,
- missed-variant investigation,
- regional recall analysis,
- and scientific interpretation.

### 🔍 Core Principle

> **A benchmark is not just a score. It is a way to interrogate a workflow.**

The objective is therefore to understand **where, how, and why** a workflow succeeds or fails rather than reporting a single performance metric in isolation.

---

## 🎯 Research Question

### Primary Question

**How does a reproducible WGS variant-calling workflow perform across different high-confidence genomic regions, and what can regional benchmarking reveal that aggregate performance metrics may hide?**

### Secondary Questions

1. How consistent is workflow performance across genomic regions?
2. How do normalized variant-set comparisons differ from formal benchmarking?
3. Which regions contribute disproportionately to reduced recall?
4. What types of discrepancies account for missed or discordant variants?
5. How reproducible is the benchmarking process across defined evaluation scales?

---

## 🧬 Research Objectives

### Objective 01 — Workflow Development

Develop a reproducible computational workflow from raw sequencing data through variant calling.

### Objective 02 — Benchmark Configuration

Establish a benchmark using:

**GIAB HG001 → GRCh38 → chr22 → High-confidence regions**

### Objective 03 — Regional Evaluation

Evaluate workflow performance across multiple genomic regions rather than relying solely on chromosome-level aggregates.

### Objective 04 — Method Comparison

Compare normalized variant-set overlap with formal benchmarking using RTG `vcfeval`.

### Objective 05 — Error Investigation

Identify missed variants, regional performance differences, and discrepancies between the called and benchmark truth sets.

### Objective 06 — Reproducibility

Organize computational configurations, scripts, results, reports, and documentation into a reproducible research repository.

---

## 🧪 Study Design

The study follows a multi-scale regional validation strategy.

| Evaluation Scale | Purpose |
|---|---|
| **5 regions** | Initial workflow validation |
| **25 regions** | Intermediate regional evaluation |
| **50 regions** | Expanded benchmark-scale assessment |
| **Formal RTG evaluation** | Benchmark-aware performance assessment |
| **Regional error analysis** | Investigation of low-recall regions |

### Experimental Logic

```text
                ┌───────────────────────┐
                │   GIAB HG001 Sample   │
                └───────────┬───────────┘
                            │
                            ▼
                ┌───────────────────────┐
                │      GRCh38 / chr22   │
                └───────────┬───────────┘
                            │
                            ▼
                ┌───────────────────────┐
                │ High-Confidence       │
                │ Benchmark Regions     │
                └───────────┬───────────┘
                            │
                            ▼
             ┌─────────────────────────────┐
             │ Reproducible WGS Workflow  │
             └──────────────┬──────────────┘
                            │
                            ▼
                ┌───────────────────────┐
                │   Variant Callset      │
                └───────────┬───────────┘
                            │
              ┌─────────────┴─────────────┐
              ▼                           ▼
    ┌──────────────────┐       ┌──────────────────┐
    │ Regional Compare │       │ RTG vcfeval      │
    │ bcftools isec    │       │ Formal Benchmark │
    └────────┬─────────┘       └────────┬─────────┘
             │                          │
             └────────────┬─────────────┘
                          ▼
                ┌───────────────────────┐
                │ Performance Profile   │
                └───────────┬───────────┘
                            │
                            ▼
                ┌───────────────────────┐
                │ Regional Investigation│
                └───────────┬───────────┘
                            │
                            ▼
                ┌───────────────────────┐
                │ Scientific Interpretation │
                └───────────────────────┘

GIAB HG001
    │
    ▼
GRCh38 Reference
    │
    ▼
chr22 High-Confidence Regions
    │
    ▼
Regional Truth Sets
    │
    ▼
Variant-Call Comparison
    │
    ├──────────────► bcftools isec
    │
    └──────────────► RTG vcfeval
                         │
                         ▼
                  Benchmark Metrics
                         │
                         ▼
              Regional Performance Profile

┌───────────────┐
│   FASTQ Data  │
└───────┬───────┘
        │
        ▼
┌────────────────────┐
│  Quality Control   │
│    FastQC/MultiQC  │
└────────┬───────────┘
         │
         ▼
┌────────────────────┐
│ Read Alignment     │
│       BWA          │
└────────┬───────────┘
         │
         ▼
┌────────────────────┐
│ BAM Processing     │
│ Sorting / Indexing │
└────────┬───────────┘
         │
         ▼
┌────────────────────┐
│ Variant Calling    │
└────────┬───────────┘
         │
         ▼
┌────────────────────────────┐
│ VCF Normalization          │
│ + Filtering                │
└────────────┬───────────────┘
             │
             ▼
┌────────────────────────────┐
│ Regional Benchmarking      │
│ 5 / 25 / 50 Regions        │
└────────────┬───────────────┘
             │
       ┌─────┴─────┐
       ▼           ▼
┌────────────┐ ┌────────────┐
│ bcftools   │ │ RTG        │
│ isec       │ │ vcfeval    │
└─────┬──────┘ └─────┬──────┘
      │              │
      └──────┬───────┘
             ▼
┌────────────────────────────┐
│ Result Integration         │
└────────────┬───────────────┘
             │
             ▼
┌────────────────────────────┐
│ Regional & Statistical     │
│ Analysis                   │
└────────────────────────────┘
