Yes. The problem is that I was still giving you explanatory text **outside** the Markdown code block.

From this point, **everything I provide for the README is Markdown source**. No prose before it, no prose after it, and no sections rendered outside the code block.

````markdown
# 🧬 Benchmark-Aware Regional Validation of a Reproducible WGS Variant-Calling Workflow

<p align="center">

**GIAB HG001 • GRCh38 • chr22 • Whole-Genome Sequencing • Variant Calling • Benchmarking • Reproducible Bioinformatics**

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

**A benchmark-aware regional validation framework for reproducible WGS variant-calling analysis**

</p>

---

## 🧭 Table of Contents

- [🔬 About This Research](#-about-this-research)
- [🎯 Research Question](#-research-question)
- [🧬 Research Objectives](#-research-objectives)
- [🧪 Study Design](#-study-design)
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
- [♻️ Reproducibility](#️-reproducibility)
- [🗂️ Repository Structure](#️-repository-structure)
- [👩‍🔬 About the Researcher](#-about-the-researcher)
- [🧭 Research Perspective](#-research-perspective)
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
| **Primary Application** | WGS Variant Calling and Benchmarking |
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

# 🔬 About This Research

Whole-genome sequencing (WGS) variant calling is a fundamental component of modern computational genomics. However, successfully generating a VCF file does not establish that the detected variants are reliable.

A variant-calling workflow needs to be evaluated against an independent benchmark to determine:

- how many expected variants are recovered;
- how many incorrect variants are introduced;
- whether performance changes across genomic regions;
- which variant classes contribute to residual errors;
- whether difficult genomic contexts affect sensitivity;
- and whether simple VCF concordance agrees with formal benchmark evaluation.

This project was developed as a **benchmark-aware regional validation framework** for evaluating WGS variant-calling performance.

The study uses:

- **Genome in a Bottle (GIAB) HG001**
- **GRCh38**
- **chromosome 22**
- selected GIAB high-confidence benchmark regions.

Rather than reporting only a single aggregate accuracy value, the analysis progressively evaluates the workflow across increasingly expanded regional benchmark scopes.

```text
5-region validation
        │
        ▼
25-region validation
        │
        ▼
50-region validation
        │
        ▼
Formal RTG vcfeval benchmarking
        │
        ▼
Missed-variant analysis
        │
        ▼
Low-recall regional analysis
        │
        ▼
bcftools vs RTG discrepancy analysis
        │
        ▼
Publication-ready tables and figures
````

The central idea is to move beyond:

> **"How accurate is the variant-calling workflow?"**

toward:

> **"Where does the workflow disagree with the benchmark, how does that disagreement change with benchmark scope, and what characteristics explain the residual errors?"**

---

# 🎯 Research Question

## Primary Research Question

> **How does WGS variant-calling performance change as benchmark evaluation expands across genomic regions, and what explains the remaining discrepancies between the project callset and the GIAB truth set?**

## Supporting Questions

1. Does benchmark performance remain stable when the number of evaluated regions increases?
2. How does normalized VCF comparison compare with formal RTG benchmarking?
3. Which variant classes account for missed truth variants?
4. Which genomic regions show reduced recall?
5. Are discrepancies concentrated in difficult genomic contexts?
6. Can regional benchmark analysis reveal limitations that are hidden by aggregate performance metrics?

---

# 🧬 Research Objectives

The project was designed around five major objectives.

## Objective 1 — Build a Reproducible WGS Workflow

Develop a documented computational workflow covering:

* sequencing-read quality control;
* read preprocessing;
* alignment;
* BAM processing;
* variant calling;
* VCF processing;
* benchmark comparison.

## Objective 2 — Establish Benchmark-Aware Validation

Use **GIAB HG001** as an independent truth benchmark rather than evaluating the workflow only through internal pipeline metrics.

## Objective 3 — Evaluate Multiple Benchmark Scales

Compare performance across:

* **5 selected regions**
* **25 selected regions**
* **50 selected regions**

## Objective 4 — Compare Benchmarking Methodologies

Evaluate the relationship between:

* normalized `bcftools isec` comparison;
* formal RTG `vcfeval` benchmarking.

## Objective 5 — Characterize Residual Errors

Investigate:

* missed variants;
* variant classes;
* low-recall regions;
* difficult genomic contexts;
* discrepancies between benchmark methods.

---

# 🧪 Study Design

| Component                 | Configuration             |
| ------------------------- | ------------------------- |
| **Benchmark Resource**    | Genome in a Bottle (GIAB) |
| **Benchmark Sample**      | HG001                     |
| **Alternate Identifier**  | NA12878                   |
| **Reference Build**       | GRCh38                    |
| **Primary Chromosome**    | chr22                     |
| **Benchmark Release**     | GIAB v4.2.1               |
| **Regional Validation**   | 5, 25, 50 regions         |
| **Normalized Comparison** | `bcftools isec`           |
| **Formal Benchmark**      | RTG `vcfeval`             |
| **Low-Recall Threshold**  | 92%                       |

> **Important:** The 5-, 25-, and 50-region analyses represent progressively expanded regional validation scopes and should not be interpreted as independent biological replicates.

---

# 🔬 Computational Workflow

## Workflow Overview

```text
                         WGS SEQUENCING DATA
                                  │
                                  ▼
                       ┌────────────────────┐
                       │  QUALITY CONTROL   │
                       │    FastQC/MultiQC  │
                       └──────────┬─────────┘
                                  │
                                  ▼
                       ┌────────────────────┐
                       │ READ PREPROCESSING │
                       │       fastp         │
                       └──────────┬─────────┘
                                  │
                                  ▼
                       ┌────────────────────┐
                       │     ALIGNMENT      │
                       │      BWA-MEM2      │
                       └──────────┬─────────┘
                                  │
                                  ▼
                       ┌────────────────────┐
                       │   BAM PROCESSING   │
                       │ sort + index       │
                       │     samtools       │
                       └──────────┬─────────┘
                                  │
                                  ▼
                       ┌────────────────────┐
                       │   VARIANT CALLING  │
                       │      bcftools      │
                       └──────────┬─────────┘
                                  │
                                  ▼
                       ┌────────────────────┐
                       │   VCF PROCESSING   │
                       │  & NORMALIZATION   │
                       └──────────┬─────────┘
                                  │
                                  ▼
                    ┌───────────────────────────┐
                    │    GIAB HG001 TRUTH SET  │
                    └─────────────┬─────────────┘
                                  │
                    ┌─────────────┴─────────────┐
                    │                           │
                    ▼                           ▼
          ┌──────────────────┐        ┌──────────────────┐
          │   bcftools isec  │        │   RTG vcfeval    │
          │    Normalized    │        │      Formal      │
          │    Comparison    │        │    Benchmark     │
          └─────────┬────────┘        └─────────┬────────┘
                    │                           │
                    └─────────────┬─────────────┘
                                  │
                                  ▼
                    ┌───────────────────────────┐
                    │ ERROR & REGIONAL ANALYSIS │
                    └─────────────┬─────────────┘
                                  │
                 ┌────────────────┼────────────────┐
                 │                │                │
                 ▼                ▼                ▼
          Missed Variants    Low-Recall       Method
                              Regions       Discrepancies
                 │                │                │
                 └────────────────┼────────────────┘
                                  │
                                  ▼
                    ┌───────────────────────────┐
                    │ PUBLICATION-READY OUTPUTS │
                    │      Tables + Figures     │
                    └───────────────────────────┘
```

---

# 📏 Benchmark-Scale Evaluation

The project evaluates the same general benchmarking framework at three regional scales.

| Benchmark Scale | Number of Regions | Purpose                              |
| --------------- | ----------------: | ------------------------------------ |
| **5-region**    |                 5 | Controlled initial validation        |
| **25-region**   |                25 | Expanded validation                  |
| **50-region**   |                50 | Primary expanded regional validation |

The progressive design allows performance to be examined as the validation scope increases.

```text
              VALIDATION SCOPE
                    │
                    ▼
             ┌─────────────┐
             │ 5 REGIONS   │
             └──────┬──────┘
                    │
                    ▼
             ┌─────────────┐
             │ 25 REGIONS  │
             └──────┬──────┘
                    │
                    ▼
             ┌─────────────┐
             │ 50 REGIONS  │
             └──────┬──────┘
                    │
                    ▼
          FORMAL BENCHMARKING
                    │
                    ▼
             ERROR ANALYSIS
```

---

# 📊 Key Results

## Normalized Benchmark Comparison

| Benchmark           | Truth Variants | Project Variants | Shared | Missed Truth | Extra Project | Recall | Precision |     F1 |
| ------------------- | -------------: | ---------------: | -----: | -----------: | ------------: | -----: | --------: | -----: |
| **5-region chr22**  |            444 |              428 |    428 |           16 |             0 | 96.40% |   100.00% | 98.17% |
| **25-region chr22** |          1,504 |            1,421 |  1,421 |           83 |             0 | 94.48% |   100.00% | 97.16% |
| **50-region chr22** |          2,592 |            2,469 |  2,469 |          123 |             0 | 95.25% |   100.00% | 97.57% |

---

## 🏆 Primary Expanded Benchmark

The 50-region normalized comparison produced:

| Metric                    |      Result |
| ------------------------- | ----------: |
| **Truth Variants**        |   **2,592** |
| **Project Variants**      |   **2,469** |
| **Shared Variants**       |   **2,469** |
| **Missed Truth Variants** |     **123** |
| **Project-Only Variants** |       **0** |
| **Recall**                |  **95.25%** |
| **Precision**             | **100.00%** |
| **F1 Score**              |  **97.57%** |

The 50-region benchmark provides the broadest regional validation within the current study design.

---

# 🧪 Formal RTG vcfeval Benchmark

The 50-region analysis was additionally evaluated using RTG `vcfeval`.

| Metric              |     Result |
| ------------------- | ---------: |
| **TP baseline**     |      2,465 |
| **TP call**         |      2,465 |
| **False positives** |          4 |
| **False negatives** |        127 |
| **Precision**       | **99.84%** |
| **Sensitivity**     | **95.10%** |
| **F-measure**       | **97.41%** |

### Formal Benchmark Summary

> **95.10% sensitivity · 99.84% precision · 97.41% F-measure**

---

# ⚖️ Normalized Comparison vs Formal Benchmarking

The two approaches showed strong agreement but were not identical.

| Metric                      | `bcftools isec` | RTG `vcfeval` |
| --------------------------- | --------------: | ------------: |
| **True / Shared Positives** |           2,469 |         2,465 |
| **False Positives**         |               0 |             4 |
| **False Negatives**         |             123 |           127 |
| **Recall / Sensitivity**    |          95.25% |        95.10% |
| **Precision**               |         100.00% |        99.84% |
| **F1 / F-measure**          |          97.57% |        97.41% |

The formal benchmark was slightly stricter than the normalized record-level comparison.

### 🔬 Methodological Interpretation

> **Simple record-level VCF concordance should not automatically be interpreted as equivalent to formal benchmark performance.**

The small numerical discrepancy between the methods demonstrates why benchmark methodology matters when evaluating variant-calling performance.

---

# 🔎 Missed-Variant Analysis

The 50-region normalized comparison identified **123 truth variants that were not recovered by the project callset**.

## Missed Variant Composition

| Variant Class  | Missed Variants |
| -------------- | --------------: |
| **Deletions**  |              66 |
| **Insertions** |              56 |
| **SNVs**       |               1 |
| **Total**      |         **123** |

The residual missed variants were therefore overwhelmingly **indel events**.

### 🔍 Areas Requiring Further Investigation

The observed pattern motivates investigation of:

* indel representation;
* alignment complexity;
* local sequence context;
* difficult genomic regions;
* variant-calling sensitivity;
* normalization behavior;
* and benchmark representation differences.

---

# 📍 Low-Recall Regional Analysis

Aggregate performance can conceal localized weaknesses.

A dedicated regional analysis was therefore implemented using a configured low-recall threshold of:

> **92% recall**

Regions below this threshold are examined independently to determine whether reduced performance is associated with particular genomic contexts.

## Analytical Hierarchy

```text
Global Benchmark Performance
             │
             ▼
Regional Performance
             │
             ▼
Low-Recall Regions
             │
             ▼
Potential Difficult Genomic Contexts
             │
             ▼
Targeted Error Interpretation
```

This approach allows the analysis to move beyond an overall recall value and investigate **where performance decreases**.

---

# 🧩 Error and Discrepancy Analysis

The project does not stop at reporting recall and precision.

It explicitly examines discrepancies through four analytical layers.

## 1. Missed-Variant Analysis

Identifies variants present in the benchmark but absent from the project callset.

## 2. Variant-Class Analysis

Determines whether residual errors are dominated by:

* SNVs;
* insertions;
* deletions;
* or other variant classes.

## 3. Low-Recall Analysis

Identifies genomic regions where performance falls below the predefined threshold.

## 4. Benchmark-Method Comparison

Compares:

```text
bcftools isec
      │
      │ normalized record-level comparison
      ▼
Benchmark Concordance
      ▲
      │ formal benchmark evaluation
      │
RTG vcfeval
```

The resulting framework therefore moves from:

> **Performance Measurement**

to:

> **Performance Diagnosis**

---

# 📈 Publication-Ready Outputs

The final structured outputs are organized under:

[`results/publication_ready/`](results/publication_ready/)

## 📋 Tables

1. Benchmark-scale comparison
2. Formal RTG `vcfeval` result
3. Missed-variant summary
4. Low-recall regions
5. `bcftools` vs RTG discrepancy regions

## 📊 Figures

1. Benchmark-scale performance
2. `bcftools isec` vs RTG `vcfeval`
3. Missed-variant composition
4. Low-recall regional analysis
5. Benchmark-aware workflow overview

## Expected Output Organization

```text
results/
└── publication_ready/
    │
    ├── tables/
    │   ├── benchmark_scale_comparison.tsv
    │   ├── benchmark_scale_comparison.md
    │   ├── formal_rtg_vcfeval_result.tsv
    │   ├── formal_rtg_vcfeval_result.md
    │   ├── missed_variant_summary.tsv
    │   ├── missed_variant_summary.md
    │   ├── low_recall_regions.tsv
    │   ├── low_recall_regions.md
    │   ├── bcftools_vs_rtg_discrepancy.tsv
    │   └── bcftools_vs_rtg_discrepancy.md
    │
    └── figures/
        ├── benchmark_scale_performance.png
        ├── bcftools_vs_rtg_vcfeval.png
        ├── missed_variant_composition.png
        ├── low_recall_regions.png
        └── workflow_overview.png
```

---

# 🧰 Software and Tools

| Analysis Stage          | Software          |
| ----------------------- | ----------------- |
| **Programming**         | Python            |
| **Quality Control**     | FastQC            |
| **QC Aggregation**      | MultiQC           |
| **Read Preprocessing**  | fastp             |
| **Alignment**           | BWA-MEM2          |
| **BAM Processing**      | samtools          |
| **Variant Processing**  | bcftools / HTSlib |
| **Formal Benchmarking** | RTG Tools         |
| **Data Analysis**       | pandas / NumPy    |
| **Visualization**       | matplotlib        |
| **Configuration**       | YAML              |

## Computational Environment

The computational environment is specified in:

[`environment.yml`](environment.yml)

## Benchmark Configuration

The benchmark configuration is specified in:

[`config/benchmark.yaml`](config/benchmark.yaml)

---

# ♻️ Reproducibility

Reproducibility is treated as a core research requirement.

The repository contains:

* workflow scripts;
* analysis scripts;
* benchmark configuration;
* software environment specification;
* provenance documentation;
* analytical reports;
* research records;
* compact derived results;
* publication-ready tables;
* figures.

## Large Data Policy

Large external sequencing and reference files are intentionally excluded from version control.

Excluded resources include:

* `FASTQ`
* `FASTQ.GZ`
* `BAM`
* `BAI`
* `CRAM`
* `CRAI`
* large `VCF`
* large `BCF`
* reference `FASTA`
* genome indexes
* large intermediate outputs

## Reproducibility Resources

* [`environment.yml`](environment.yml)
* [`config/benchmark.yaml`](config/benchmark.yaml)
* [`docs/`](docs/)
* [`scripts/`](scripts/)
* [`results/`](results/)
* [`.gitignore`](.gitignore)

---

# 🗂️ Repository Structure

```text
Benchmark-aware-WGS-preventive-genomics/
│
├── config/
│   └── benchmark.yaml
│
├── data/
│   └── External / excluded sequencing data
│
├── docs/
│   ├── lab_notebook/
│   ├── metadata/
│   ├── methodology/
│   ├── phd_positioning/
│   └── research_tracking/
│
├── figures/
│
├── logs/
│
├── manuscript/
│
├── pipeline/
│
├── reference/
│
├── reference_datasets/
│
├── reports/
│
├── results/
│   ├── benchmark analyses
│   ├── formal benchmarking
│   ├── discrepancy analysis
│   └── publication_ready/
│       ├── tables/
│       └── figures/
│
├── scripts/
│
├── tests/
│
├── CITATION.cff
├── LICENSE
├── README.md
├── environment.yml
└── .gitignore
```

---

# 👩‍🔬 About the Researcher

## Ritika Rajendra Rawat

**Bioinformatics Researcher | Computational Genomics | WGS Variant Benchmarking**

I am an MSc Bioinformatics graduate and early-career bioinformatics researcher working at the intersection of:

* **Computational Genomics**
* **NGS Analysis**
* **Variant Benchmarking**
* **Reproducible Bioinformatics**
* **Translational Health Research**

### Research Interests

* Whole-genome sequencing
* Variant discovery and validation
* Genomic benchmarking
* Computational genomics
* Reproducible analysis workflows
* Variant interpretation
* Precision genomics
* Preventive genomics
* Computational approaches to biological and health research

This project represents an effort to develop a research workflow that goes beyond executing standard bioinformatics tools and instead emphasizes:

> **Benchmark Design → Reproducibility → Quantitative Validation → Error Analysis → Scientific Interpretation**

The broader research goal is to develop rigorous computational approaches that can connect genomic data analysis with meaningful biological and translational questions while maintaining appropriate scientific and clinical boundaries.

---

# 🔗 Connect With the Researcher

| Platform        | Link                                                                         |
| --------------- | ---------------------------------------------------------------------------- |
| 📧 **Email**    | [ritika.rawat27@outlook.com](mailto:ritika.rawat27@outlook.com)              |
| 💼 **LinkedIn** | [Ritika Rajendra Rawat](https://www.linkedin.com/in/ritika-rawat-551107219/) |
| 💻 **GitHub**   | [Rita1791](https://github.com/Rita1791)                                      |

---

# 🧭 Research Perspective

I approach computational genomics through four principles.

## ♻️ Reproducibility

A computational result should be traceable to the:

```text
Data
  ↓
Parameters
  ↓
Software
  ↓
Workflow
  ↓
Analysis
  ↓
Result
```

## 🧪 Benchmarking

Performance should be evaluated against an appropriate independent reference rather than assumed from successful pipeline execution.

## 🔎 Error Characterization

A single accuracy number is insufficient.

Understanding:

* **where** a workflow fails;
* **what type** of variants are missed;
* **how frequently** they are missed;
* and **which genomic contexts** contribute to the error

is equally important.

## ⚠️ Scientific Restraint

Computational benchmark performance should not automatically be translated into clinical claims without appropriate validation.

These principles guide the design and interpretation of this repository.

---

# ⚠️ Scope and Limitations

This repository represents a **computational regional validation study**, not a clinical validation study.

## Current Scope

The current analysis is limited to:

* **HG001**
* **GRCh38**
* **chromosome 22**
* selected GIAB high-confidence regions
* the evaluated sequencing dataset
* the implemented workflow configuration

## What the Results Do Not Establish

The current results should **not** be interpreted as evidence of:

* clinical diagnostic accuracy;
* clinical sensitivity or specificity;
* genome-wide performance;
* population-wide generalizability;
* universal variant-caller performance;
* direct clinical decision-making capability.

## Requirements for Broader Generalization

Broader conclusions would require validation across additional:

* samples;
* chromosomes;
* benchmark regions;
* sequencing technologies;
* variant classes;
* independent datasets.

---

# 🚀 Future Research

Potential extensions include:

1. **Expansion to additional chromosomes**
2. **Genome-wide GIAB benchmarking**
3. **Validation across additional GIAB samples**
4. **Comparison of multiple variant callers**
5. **Variant-class-specific benchmarking**
6. **Systematic difficult-region stratification**
7. **Platform-aware benchmarking**
8. **Reproducibility testing across computational environments**
9. **Larger and more diverse benchmark datasets**
10. **Extension toward population-scale and translational genomics research**

## Long-Term Direction

```text
Regional Validation
        ↓
Multi-Chromosome Validation
        ↓
Genome-Wide Benchmarking
        ↓
Multi-Sample Validation
        ↓
Multi-Caller Comparison
        ↓
Variant-Class Stratification
        ↓
Platform-Aware Benchmarking
        ↓
Population-Scale Genomics
```

---

# 🏢 Acknowledgement

I acknowledge **Nainsense Labs Private Limited** for the professional environment and practical exposure that supported the development of this research work.

| Information      | Details                                           |
| ---------------- | ------------------------------------------------- |
| **Organization** | Nainsense Labs Private Limited                    |
| **Website**      | [nainsense.com](https://nainsense.com/)           |
| **Email**        | [admin@nainsense.com](mailto:admin@nainsense.com) |

> This acknowledgement recognizes the professional environment and exposure associated with the development of the work and does **not** imply institutional endorsement of the scientific methodology, results, conclusions, or interpretations presented in this repository.

---

# 📚 Documentation

| Resource                                                   | Description                       |
| ---------------------------------------------------------- | --------------------------------- |
| [`config/benchmark.yaml`](config/benchmark.yaml)           | Benchmark configuration           |
| [`environment.yml`](environment.yml)                       | Computational environment         |
| [`docs/`](docs/)                                           | Research documentation            |
| [`pipeline/`](pipeline/)                                   | Core workflow                     |
| [`scripts/`](scripts/)                                     | Analysis and benchmarking scripts |
| [`reports/`](reports/)                                     | Detailed analytical reports       |
| [`results/`](results/)                                     | Computational results             |
| [`results/publication_ready/`](results/publication_ready/) | Final tables and figures          |
| [`manuscript/`](manuscript/)                               | Manuscript development            |
| [`tests/`](tests/)                                         | Test resources                    |
| [`CITATION.cff`](CITATION.cff)                             | Citation information              |

---

# 📖 Citation

If you use this repository, its computational workflow, derived analyses, or methodological framework, please cite the project using the information provided in:

[`CITATION.cff`](CITATION.cff)

```text
Benchmark-Aware Regional Validation of a Reproducible WGS Variant-Calling Workflow

Author:
Ritika Rajendra Rawat

Research Area:
Computational Genomics

Primary Benchmark:
GIAB HG001

Reference:
GRCh38

Primary Chromosome:
chr22
```

---

# 📄 License

This project is released under the **MIT License**.

See [`LICENSE`](LICENSE).

---

# 📊 Project Status

| Parameter                 | Current Status                                                                 |
| ------------------------- | ------------------------------------------------------------------------------ |
| **Status**                | Active research / benchmark validation                                         |
| **Primary Benchmark**     | GIAB HG001                                                                     |
| **Reference**             | GRCh38                                                                         |
| **Primary Chromosome**    | chr22                                                                          |
| **Regional Scales**       | 5, 25, 50 regions                                                              |
| **Normalized Comparison** | `bcftools isec`                                                                |
| **Formal Benchmark**      | RTG `vcfeval`                                                                  |
| **Research Focus**        | Reproducible computational genomics and benchmark-aware WGS variant validation |

## Current Research Milestones

```text
✓ WGS workflow development
✓ Dataset evaluation
✓ GIAB HG001 benchmark selection
✓ GRCh38 chr22 benchmark preparation
✓ 5-region validation
✓ 25-region validation
✓ 50-region validation
✓ Normalized bcftools isec comparison
✓ Formal RTG vcfeval benchmarking
✓ Missed-variant analysis
✓ Low-recall regional analysis
✓ Benchmark-method discrepancy analysis
✓ Publication-ready tables
✓ Publication-ready figures
✓ Reproducibility documentation
✓ Research documentation
✓ Citation metadata
✓ Repository structure
```

---

# 👩‍🔬 Researcher

## Ritika Rajendra Rawat

**MSc Bioinformatics | Bioinformatics Researcher**

**Computational Genomics • WGS • Variant Benchmarking • Reproducible Bioinformatics**

### Contact

* 📧 **Email:** [ritika.rawat27@outlook.com](mailto:ritika.rawat27@outlook.com)
* 💼 **LinkedIn:** [Ritika Rajendra Rawat](https://www.linkedin.com/in/ritika-rawat-551107219/)
* 💻 **GitHub:** [Rita1791](https://github.com/Rita1791)

---

## 🧬 Core Contribution

> **A benchmark-aware and reproducible framework for evaluating WGS variant-calling performance through progressively expanded regional validation, formal benchmarking, and systematic error characterization.**

---

<p align="center">

### 🧬 Benchmark → Validate → Diagnose → Reproduce

</p>

<p align="center">

**Computational Genomics • WGS • Variant Benchmarking • Reproducible Bioinformatics**

</p>
```
