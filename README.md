# 🧬 Benchmark-Aware Regional Validation of a Reproducible WGS Variant-Calling Workflow

<p align="center">

**GIAB HG001 · GRCh38 · chr22 · Whole-Genome Sequencing · Variant Calling · Benchmarking · Reproducible Bioinformatics**

</p>

<p align="center">

<a href="https://www.nist.gov/programs-projects/genome-bottle">
<img src="https://img.shields.io/badge/Benchmark-GIAB%20HG001-2F80ED?style=for-the-badge" alt="GIAB HG001">
</a>

<a href="config/benchmark.yaml">
<img src="https://img.shields.io/badge/Reference-GRCh38-F2994A?style=for-the-badge" alt="GRCh38">
</a>

<a href="config/benchmark.yaml">
<img src="https://img.shields.io/badge/Chromosome-chr22-8E44AD?style=for-the-badge" alt="Chromosome 22">
</a>

<a href="environment.yml">
<img src="https://img.shields.io/badge/Python-3.11-3776AB?style=for-the-badge" alt="Python 3.11">
</a>

<a href="#-project-status">
<img src="https://img.shields.io/badge/Status-Active%20Research-27AE60?style=for-the-badge" alt="Active Research">
</a>

</p>

<p align="center">

### 🔬 A benchmark-aware framework for evaluating WGS variant-calling performance across genomic regions

</p>

<p align="center">

<a href="#-research-question">Research Question</a> ·
<a href="#-computational-workflow">Workflow</a> ·
<a href="#-key-results">Results</a> ·
<a href="#-formal-rtg-vcfeval-benchmark">Benchmarking</a> ·
<a href="#-reproducibility">Reproducibility</a>

</p>

---

> 🧭 **Research in one line:**  
> A reproducible WGS variant-calling workflow is evaluated against GIAB HG001 using regional validation, normalized VCF comparison, formal `RTG vcfeval` benchmarking, and targeted discrepancy analysis.

---

## 🧭 Table of Contents

### 🔬 Research Overview

- [🔬 About This Research](#-about-this-research)
- [🎯 Research Question](#-research-question)
- [🧬 Research Objectives](#-research-objectives)
- [🧪 Study Design](#-study-design)

### 🧬 Computational & Benchmarking Workflow

- [🔬 Computational Workflow](#-computational-workflow)
- [📏 Benchmark-Scale Evaluation](#-benchmark-scale-evaluation)
- [🧪 Formal RTG vcfeval Benchmark](#-formal-rtg-vcfeval-benchmark)
- [⚖️ Normalized Comparison vs Formal Benchmarking](#-normalized-comparison-vs-formal-benchmarking)

### 📊 Results & Interpretation

- [📊 Key Results](#-key-results)
- [🔎 Missed-Variant Analysis](#-missed-variant-analysis)
- [📍 Low-Recall Regional Analysis](#-low-recall-regional-analysis)
- [🧩 Error and Discrepancy Analysis](#-error-and-discrepancy-analysis)

### 📈 Research Outputs & Reproducibility

- [📈 Publication-Ready Outputs](#-publication-ready-outputs)
- [🧰 Software and Tools](#-software-and-tools)
- [♻️ Reproducibility](#-reproducibility)
- [🗂️ Repository Structure](#-repository-structure)
- [📚 Documentation](#-documentation)

### 👩‍🔬 Researcher & Scientific Context

- [👩‍🔬 About the Researcher](#-about-the-researcher)
- [🧭 Research Perspective](#-research-perspective)
- [⚠️ Scope and Limitations](#-scope-and-limitations)
- [🚀 Future Research](#-future-research)

### 📚 Project Information

- [🏢 Acknowledgement](#-acknowledgement)
- [📖 Citation](#-citation)
- [📄 License](#-license)
- [📊 Project Status](#-project-status)

---

## 🧭 Project at a Glance

> **A reproducible regional benchmarking study designed to evaluate not only whether variants are detected, but where and why workflow performance changes across genomic regions.**

| 🧩 Category | 🔬 Details |
|:---|:---|
| **Research Area** | Computational Genomics |
| **Primary Application** | WGS Variant Calling & Benchmarking |
| **Benchmark Resource** | Genome in a Bottle (GIAB) |
| **Benchmark Sample** | HG001 |
| **Alternate Identifier** | NA12878 |
| **Reference Genome** | GRCh38 |
| **Primary Chromosome** | chr22 |
| **Benchmark Release** | GIAB v4.2.1 |
| **Validation Scales** | 5, 25 & 50 regions |
| **Normalized Comparison** | `bcftools isec` |
| **Formal Benchmark** | RTG `vcfeval` |
| **Low-Recall Threshold** | 92% |
| **Primary Analysis** | Regional Benchmark Validation |
| **Research Status** | Active Computational Research |

### 🧭 Research Journey

``
⚙️ Configure
     ↓
🧬 Process
     ↓
🔬 Benchmark
     ↓
📊 Compare
     ↓
📍 Localize
     ↓
🧩 Investigate
     ↓
📈 Interpret
     ↓
♻️ Reproduce

---

`
## 🔬 About This Research

Variant calling does not end when a VCF file is produced.

A workflow can generate apparently plausible variants while still missing benchmark-supported variants or producing discordant calls.

This project therefore approaches WGS variant calling as a **benchmarking and validation problem**.

Instead of asking only:

> **"How many variants did the pipeline call?"**

the project asks:

> **"How reliably did the workflow recover benchmark-supported variants, and where does its performance change across genomic regions?"**

The analysis uses **GIAB HG001**, **GRCh38**, and **chromosome 22 high-confidence benchmark regions** to evaluate regional variant-calling performance using complementary benchmarking strategies.

### 🔬 Core Scientific Principle

``
Variant Calling
      ↓
Benchmarking
      ↓
Performance Measurement
      ↓
Regional Investigation
      ↓
Discrepancy Analysis
      ↓
Scientific Interpretation

---

# 🧩 Research Objectives + Study Design

``
## 🧬 Research Objectives

### 01 · Benchmark

Evaluate variant-calling performance against the GIAB HG001 benchmark.

### 02 · Compare

Compare normalized VCF overlap with formal benchmark evaluation.

### 03 · Localize

Identify genomic regions showing reduced recall or increased discrepancies.

### 04 · Investigate

Characterize missed variants and benchmark discordances.

### 05 · Reproduce

Document the computational environment, configuration, workflow, scripts, and outputs required to reproduce the analysis.

---

## 🧪 Study Design

The project uses a **multi-scale regional validation strategy**.

### 📏 Validation Scales

| Scale | Purpose |
|:---:|:---|
| **5 regions** | Broad regional screening |
| **25 regions** | Intermediate-resolution evaluation |
| **50 regions** | Fine regional characterization |

### 🧬 Benchmark Framework

``
GIAB HG001
     +
GRCh38
     +
chr22 high-confidence regions
     ↓
Regional truth sets
     ↓
Variant-call comparison
     ↓
Benchmark metrics
     ↓
Regional performance profile

---

# 🧩 Computational Workflow

``
## 🔬 Computational Workflow

The workflow follows a structured FASTQ-to-benchmark analysis pathway.

``
┌──────────────────────┐
│      FASTQ Data      │
└──────────┬───────────┘
           │
           ▼
┌──────────────────────┐
│   Quality Control    │
└──────────┬───────────┘
           │
           ▼
┌──────────────────────┐
│    Read Alignment    │
└──────────┬───────────┘
           │
           ▼
┌──────────────────────┐
│    BAM Processing    │
└──────────┬───────────┘
           │
           ▼
┌──────────────────────┐
│    Variant Calling   │
└──────────┬───────────┘
           │
           ▼
┌──────────────────────┐
│ VCF Normalization &  │
│      Filtering       │
└──────────┬───────────┘
           │
           ▼
┌──────────────────────┐
│ Regional Benchmarking│
└──────────┬───────────┘
           │
      ┌────┴────┐
      ▼         ▼
┌──────────┐ ┌────────────┐
│ bcftools │ │    RTG     │
│   isec   │ │  vcfeval   │
└────┬─────┘ └─────┬──────┘
     │             │
     └──────┬──────┘
            ▼
┌──────────────────────┐
│ Result Integration   │
└──────────┬───────────┘
           │
           ▼
┌──────────────────────┐
│ Statistical &        │
│ Regional Analysis    │
└──────────────────────┘

---

## 🧪 Study Design

The project uses a **multi-scale regional validation strategy**.

### 📏 Validation Scales

| Scale | Purpose |
|:---:|:---|
| **5 regions** | Broad regional screening |
| **25 regions** | Intermediate-resolution evaluation |
| **50 regions** | Fine regional characterization |

### 🧬 Benchmark Framework

``
GIAB HG001
     +
GRCh38
     +
chr22 high-confidence regions
     ↓
Regional truth sets
     ↓
Variant-call comparison
     ↓
Benchmark metrics
     ↓
Regional performance profile

---

# 🧩 Benchmark Evaluation

``
## 📏 Benchmark-Scale Evaluation

The workflow evaluates performance at multiple regional scales rather than relying exclusively on whole-region aggregate metrics.

### Why Regional Evaluation?

An aggregate metric can hide localized failures.

Two workflows may produce similar overall recall while behaving very differently across individual genomic regions.

Regional analysis therefore helps answer:

> **Where does the workflow perform well — and where does it struggle?**

### 📊 Evaluation Dimensions

| Metric | Purpose |
|:---|:---|
| **Precision** | Proportion of called variants supported by the benchmark |
| **Recall / Sensitivity** | Recovery of benchmark-supported variants |
| **F1 Score** | Balance between precision and recall |
| **TP** | Correctly identified benchmark variants |
| **FP** | Calls not supported by the benchmark |
| **FN** | Benchmark variants missed by the workflow |

### 🔎 Regional Evaluation Logic

``
Aggregate Performance
        ↓
Regional Breakdown
        ↓
Low-Recall Regions
        ↓
Variant-Level Investigation
        ↓
Potential Cause
        ↓
Scientific Interpretation

---

# 🧩 Comparison + Results

``
## ⚖️ Normalized Comparison vs Formal Benchmarking

Two complementary comparison strategies are used.

### ① Normalized VCF Comparison

**Tool:** `bcftools isec`

Used to examine normalized variant-set overlap.

### ② Formal Benchmarking

**Tool:** RTG `vcfeval`

Used to perform benchmark-aware variant comparison.

### 🔬 Why Use Both?

> **Normalized comparison tells us what differs at the VCF level. Formal benchmarking helps determine whether those differences represent genuine variant discrepancies.**

This distinction is important when interpreting false positives, false negatives, and discordant calls.

---

## 📊 Key Results

> ### 🎯 The central result of this project is not a single accuracy number.
>
> **It is the regional performance profile of the workflow.**

The analysis evaluates performance across:

- **5-region validation**
- **25-region validation**
- **50-region validation**
- **Formal RTG `vcfeval` benchmarking**
- **Normalized VCF comparison**

### 📌 Benchmark Configuration

| Indicator | Value |
|:---|:---:|
| **Reference Sample** | HG001 |
| **Reference Genome** | GRCh38 |
| **Chromosome** | chr22 |
| **Benchmark Release** | GIAB v4.2.1 |
| **Regional Scales** | 5 / 25 / 50 |
| **Low-Recall Threshold** | 92% |

> 📌 **Detailed numerical results, regional summaries, and publication-ready figures are available in [`results/`](results/).**

---

## 🔎 Missed-Variant Analysis

Variants contributing to reduced recall are investigated rather than treated as unexplained failures.

The analysis examines:

- Variant representation
- Genomic location
- Variant type
- Benchmark membership
- Caller output
- Filtering behaviour
- Normalization
- Regional context

### 🔬 Research Question

> **What explains the variants that the workflow did not recover?**

The objective is to distinguish between:

``
True workflow misses
        vs.
Apparent misses caused by
representation / comparison differences

## 🔎 Missed-Variant Analysis

Variants contributing to reduced recall are investigated rather than treated as unexplained failures.

The analysis examines:

- Variant representation
- Genomic location
- Variant type
- Benchmark membership
- Caller output
- Filtering behaviour
- Normalization
- Regional context

### 🔬 Research Question

> **What explains the variants that the workflow did not recover?**

The objective is to distinguish between:

``
True workflow misses
        vs.
Apparent misses caused by
representation / comparison differences

---

# 🧩 Error + Outputs

``
## 🧩 Error and Discrepancy Analysis

Benchmark discrepancies are categorized to distinguish different sources of apparent error.

| Category | Question |
|:---|:---|
| 🧬 **Representation** | Are equivalent variants represented differently? |
| 🎯 **Filtering** | Was the variant removed during downstream filtering? |
| 📍 **Regional Context** | Does the genomic region show unusual behaviour? |
| 🔬 **Variant Type** | Does performance differ by variant class? |
| ⚙️ **Workflow** | Could a computational step contribute to the discrepancy? |
| 📊 **Benchmarking** | Does the comparison method affect classification? |

> **The objective is not simply to count errors, but to understand them.**

---

## 📈 Publication-Ready Outputs

The repository contains publication-oriented outputs generated from the computational analysis.

### 📊 Figures

[`results/publication_ready/`](results/publication_ready/)

Finalized figures prepared for scientific communication.

### 📋 Tables

[`results/publication_ready/`](results/publication_ready/)

Finalized summary tables and benchmark outputs.

### 📝 Reports

[`reports/`](reports/)

Detailed analytical reports documenting intermediate and final evaluations.

### 🧬 Manuscript

[`manuscript/`](manuscript/)

Manuscript development, scientific interpretation, and associated research material.

---

## 🧰 Software and Tools

The project integrates tools commonly used in reproducible genomic variant analysis.

| Category | Tools / Technologies |
|:---|:---|
| 🐍 **Programming** | Python |
| 💻 **Scripting** | Bash / Shell |
| 🧬 **Sequence Data** | FASTQ |
| 🧫 **Alignment Data** | BAM |
| 🧬 **Variant Data** | VCF |
| 📏 **Formal Benchmarking** | RTG `vcfeval` |
| 🔀 **VCF Comparison** | `bcftools isec` |
| 🧪 **Benchmark Resource** | GIAB HG001 |
| 🧬 **Reference Genome** | GRCh38 |
| 📊 **Analysis** | Statistical analysis & visualization |
| ⚙️ **Environment** | Conda / `environment.yml` |

> Exact software versions and configurations should be recorded within the repository to support reproducibility.

---

## ♻️ Reproducibility

Reproducibility is a core component of this project.

The repository documents:

- Benchmark configuration
- Computational environment
- Workflow structure
- Analysis scripts
- Benchmarking procedures
- Intermediate outputs
- Final results
- Publication-ready figures and tables
- Manuscript development

### 🔁 Reproducibility Pathway

``
Configuration
      ↓
Environment
      ↓
Pipeline
      ↓
Benchmark
      ↓
Analysis
      ↓
Results
      ↓
Publication Output

---

# 🧩 Repository Structure + Documentation

``
## 🗂️ Repository Structure

``
.
├── config/
│   └── benchmark.yaml
│
├── pipeline/
│   └── Core computational workflow
│
├── scripts/
│   └── Analysis and benchmarking scripts
│
├── benchmarking/
│   └── Formal and regional benchmarking resources
│
├── reports/
│   └── Detailed analytical reports
│
├── results/
│   ├── publication_ready/
│   └── Computational results
│
├── manuscript/
│   └── Manuscript development
│
├── docs/
│   └── Research documentation
│
├── tests/
│   └── Test resources
│
├── environment.yml
├── CITATION.cff
├── CONTRIBUTORS.md
├── LICENSE
└── README.md

---

# 🧩 Researcher + Perspective

``
## 👩‍🔬 About the Researcher

### Ritika Rajendra Rawat

**Bioinformatics Research Associate · Bioinformatics Lead**

**MSc Bioinformatics**

My research interests sit at the intersection of:

> **Computational Genomics · Variant Analysis · Reproducible Bioinformatics · Benchmarking · Precision Genomics**

This project reflects an interest in developing computational workflows that are not only capable of producing results, but can also be:

**benchmarked → challenged → interpreted → reproduced**

---

## 🧭 Research Perspective

> ### **A benchmark is not just a score. It is a way to interrogate a workflow.**

The objective of this project is therefore not to treat the computational pipeline as a black box.

Instead, the analysis follows a critical research cycle:

``
BUILD
  ↓
BENCHMARK
  ↓
COMPARE
  ↓
INVESTIGATE
  ↓
EXPLAIN
  ↓
REPRODUCE

---

# 🧩 Limitations + Future Research

``
## ⚠️ Scope and Limitations

This project should be interpreted within the scope of the evaluated dataset, genomic region, and benchmarking framework.

### Current Scope

- Benchmark sample: **GIAB HG001**
- Reference genome: **GRCh38**
- Primary genomic region: **chromosome 22**
- Benchmark release: **GIAB v4.2.1**
- Regional evaluation: **5, 25, and 50 regions**

### Important Considerations

- Performance may vary across genomic regions.
- Benchmark behaviour can differ across variant classes.
- Results depend on workflow configuration and filtering parameters.
- Regional benchmarking does not establish universal variant-calling performance.
- Formal benchmarking and normalized VCF comparison answer related but different questions.

> These limitations define the scope of interpretation and provide natural directions for future validation.

---

## 🚀 Future Research

Future extensions may include:

### 🧬 Dataset Expansion

- Additional GIAB benchmark samples
- Additional chromosomes
- Broader genomic regions

### 🔬 Variant-Level Investigation

- Variant-type-specific benchmarking
- False-negative characterization
- Structural and representation-aware analysis

### ⚙️ Workflow Evaluation

- Alternative variant callers
- Alternative filtering strategies
- Different sequencing depths
- Parameter sensitivity analysis

### ♻️ Reproducibility Engineering

- Workflow containerization
- Nextflow implementation
- Snakemake implementation
- Automated benchmark reporting
- Continuous workflow validation

### 📊 Long-Term Direction

> **From a regional benchmarking workflow toward a reusable framework for systematic evaluation of WGS variant-calling pipelines.**

---

## 🏢 Acknowledgement

This project was developed within the research and computational environment of:

### **Nainsense Labs Private Limited**

The project acknowledges the **Genome in a Bottle (GIAB)** resources used for benchmark evaluation.

We also acknowledge the publicly available genomic resources and software tools that support reproducible variant analysis.

---

## 👥 Contributors

This project was developed collaboratively within the research and computational environment of **Nainsense Labs Private Limited**.

### 👩‍🔬 Project Lead

**Ritika Rajendra Rawat**  
*Bioinformatics Research Assistant · Bioinformatics Lead*

Ritika led the scientific, computational, and analytical development of the benchmarking study.

**Primary contributions:**

- Designed the overall benchmarking strategy
- Developed and configured the WGS variant-calling workflow
- Implemented computational preprocessing and quality-control analysis
- Developed workflow components for alignment, variant calling, VCF processing, normalization, and filtering
- Designed and performed GIAB-based benchmarking
- Conducted performance evaluation and statistical analysis
- Investigated regional performance and benchmarking discrepancies
- Generated analytical figures, tables, and performance summaries
- Structured the repository for reproducibility
- Prepared research documentation and scientific interpretation
- Led preparation of the associated research output

### 🧑‍💻 Contributor

**Farheena Azim Faridi**  
*Bioinformatics Research Intern · MSc Bioinformatics*

Farheena contributed to computational workflow development and benchmarking activities under the direction of the Bioinformatics Lead.

**Contributions:**

- Assisted with WGS workflow execution
- Supported computational analysis tasks
- Assisted with GIAB benchmarking
- Supported organization and documentation of computational outputs
- Participated in review and interpretation of intermediate results
- Contributed to workflow testing and refinement

### 🏢 Organizational Context

**Nainsense Labs Private Limited**

The project was conducted within the organization's research and computational environment.

The organization provided the professional environment in which the contributors collaborated on the WGS benchmarking study.

### 📋 Contribution Transparency

For the detailed contribution and attribution statement, see:

👉 **[CONTRIBUTORS.md](CONTRIBUTORS.md)**

> Contributions are documented according to the work actually performed by each contributor.

---

## 📖 Citation

If you use this workflow, analysis, or repository in your research, please cite the associated research output:

> **Rawat, R. R., et al.**  
> *Benchmark-aware validation of a reproducible WGS variant-calling workflow using GIAB HG001 chromosome 22 reference regions.*

For machine-readable citation metadata, see:

[`CITATION.cff`](CITATION.cff)

---

## 📄 License

This project is distributed under the **MIT License**.

See [`LICENSE`](LICENSE) for the complete license text.

---

## 📊 Project Status

### 🟢 Active Computational Research

The repository is maintained as a reproducible research record of the WGS benchmarking study.

### Current Focus

- ✅ Regional benchmark validation
- ✅ Formal `RTG vcfeval` evaluation
- ✅ Normalized VCF comparison
- ✅ Missed-variant investigation
- ✅ Regional recall analysis
- ✅ Error and discrepancy analysis
- 🔄 Scientific refinement
- 🔄 Publication / dissemination

### 🔬 Research Lifecycle

``
✓ Workflow Development
      ↓
✓ Benchmark Configuration
      ↓
✓ Regional Evaluation
      ↓
✓ Formal Benchmarking
      ↓
✓ Result Analysis
      ↓
→ Scientific Refinement
      ↓
→ Publication / Dissemination
