# Benchmark-Aware Regional Validation of a Reproducible WGS Variant-Calling Workflow

### GIAB HG001 • GRCh38 • chr22 • WGS • Variant Calling • Benchmarking • Reproducible Bioinformatics

[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Benchmark](https://img.shields.io/badge/Benchmark-GIAB%20HG001-blue.svg)](config/benchmark.yaml)
[![Reference](https://img.shields.io/badge/Reference-GRCh38-orange.svg)](config/benchmark.yaml)
[![Python](https://img.shields.io/badge/Python-3.11-blue.svg)](environment.yml)

> A reproducible computational genomics study evaluating WGS variant-calling performance against the Genome in a Bottle (GIAB) HG001 benchmark across progressively expanded high-confidence regions of GRCh38 chromosome 22.

---

## 🔬 About This Research

Whole-genome sequencing (WGS) variant calling is a fundamental component of modern computational genomics. However, generating a VCF file is not sufficient to establish that the detected variants are reliable.

A variant-calling workflow must be evaluated against an independent benchmark to determine:

* how many expected variants are recovered,
* how many incorrect variants are introduced,
* whether performance changes across genomic regions,
* which variant classes contribute to residual errors,
* and whether simple VCF concordance agrees with formal benchmark evaluation.

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
```

The central idea is to move beyond:

> **"How accurate is the variant-calling workflow?"**

toward:

> **"Where does the workflow disagree with the benchmark, how does that disagreement change with benchmark scope, and what characteristics explain the residual errors?"**

---

# 🎯 Research Question

### Primary research question

> **How does WGS variant-calling performance change as benchmark evaluation expands across genomic regions, and what explains the remaining discrepancies between the project callset and the GIAB truth set?**

### Supporting questions

1. Does benchmark performance remain stable when the number of evaluated regions increases?
2. How does normalized VCF comparison compare with formal RTG benchmarking?
3. Which variant classes account for missed truth variants?
4. Which genomic regions show reduced recall?
5. Are discrepancies concentrated in difficult genomic contexts?
6. Can regional benchmark analysis reveal limitations that are hidden by aggregate performance metrics?

---

# 🧬 Research Objectives

The project was designed around five major objectives:

### Objective 1 — Build a reproducible WGS workflow

Develop a documented computational workflow covering:

* sequencing-read quality control,
* read preprocessing,
* alignment,
* BAM processing,
* variant calling,
* VCF processing,
* and benchmark comparison.

### Objective 2 — Establish benchmark-aware validation

Use GIAB HG001 as an independent truth benchmark rather than evaluating the workflow only through internal pipeline metrics.

### Objective 3 — Evaluate multiple benchmark scales

Compare performance across:

* 5 selected regions,
* 25 selected regions,
* 50 selected regions.

### Objective 4 — Compare benchmarking methodologies

Evaluate the relationship between:

* normalized `bcftools isec` comparison, and
* formal RTG `vcfeval` benchmarking.

### Objective 5 — Characterize residual errors

Investigate:

* missed variants,
* variant classes,
* low-recall regions,
* difficult genomic contexts,
* and discrepancies between benchmark methods.

---

# 🧪 Study Design

| Component             | Configuration             |
| --------------------- | ------------------------- |
| Benchmark resource    | Genome in a Bottle (GIAB) |
| Benchmark sample      | HG001                     |
| Alternate identifier  | NA12878                   |
| Reference build       | GRCh38                    |
| Primary chromosome    | chr22                     |
| Benchmark release     | GIAB v4.2.1               |
| Regional validation   | 5, 25, 50 regions         |
| Normalized comparison | `bcftools isec`           |
| Formal benchmark      | RTG `vcfeval`             |
| Low-recall threshold  | 92%                       |

The 5-, 25-, and 50-region analyses represent **progressively expanded regional validation scopes** and should not be interpreted as independent biological replicates.

---

# 🔬 Computational Workflow

```text
                    WGS SEQUENCING DATA
                            │
                            ▼
                    ┌───────────────┐
                    │ Quality       │
                    │ Control       │
                    │ FastQC/MultiQC│
                    └───────┬───────┘
                            │
                            ▼
                    ┌───────────────┐
                    │ Read          │
                    │ preprocessing │
                    │ fastp         │
                    └───────┬───────┘
                            │
                            ▼
                    ┌───────────────┐
                    │ Alignment     │
                    │ BWA-MEM2      │
                    └───────┬───────┘
                            │
                            ▼
                    ┌───────────────┐
                    │ BAM sorting    │
                    │ + indexing     │
                    │ samtools       │
                    └───────┬───────┘
                            │
                            ▼
                    ┌───────────────┐
                    │ Variant       │
                    │ calling       │
                    │ bcftools      │
                    └───────┬───────┘
                            │
                            ▼
                    ┌───────────────┐
                    │ VCF processing │
                    │ & normalization│
                    └───────┬───────┘
                            │
                            ▼
                 ┌──────────────────────┐
                 │ GIAB HG001 Truth Set │
                 └──────────┬───────────┘
                            │
              ┌─────────────┴─────────────┐
              ▼                           ▼
       ┌──────────────┐            ┌──────────────┐
       │ bcftools     │            │ RTG          │
       │ isec         │            │ vcfeval      │
       │ normalized   │            │ formal       │
       │ comparison   │            │ benchmark    │
       └──────┬───────┘            └──────┬───────┘
              │                           │
              └─────────────┬─────────────┘
                            ▼
                 ┌────────────────────┐
                 │ Error & Regional   │
                 │ Characterization   │
                 └─────────┬──────────┘
                           │
             ┌─────────────┼─────────────┐
             ▼             ▼             ▼
        Missed variants  Low recall   Method
                         regions      discrepancies
             │             │             │
             └─────────────┼─────────────┘
                           ▼
                 Publication-ready
                  tables and figures
```

---

# 📏 Benchmark-Scale Evaluation

The project evaluates the same general benchmarking framework at three regional scales.

| Benchmark | Regions | Purpose                              |
| --------- | ------: | ------------------------------------ |
| 5-region  |       5 | Controlled initial validation        |
| 25-region |      25 | Expanded validation                  |
| 50-region |      50 | Primary expanded regional validation |

This progressive design allows performance to be examined as the validation scope increases.

---

# 📊 Key Results

## Normalized benchmark comparison

| Benchmark       | Truth Variants | Project Variants | Shared | Missed Truth | Extra Project | Recall | Precision |     F1 |
| --------------- | -------------: | ---------------: | -----: | -----------: | ------------: | -----: | --------: | -----: |
| 5-region chr22  |            444 |              428 |    428 |           16 |             0 | 96.40% |   100.00% | 98.17% |
| 25-region chr22 |          1,504 |            1,421 |  1,421 |           83 |             0 | 94.48% |   100.00% | 97.16% |
| 50-region chr22 |          2,592 |            2,469 |  2,469 |          123 |             0 | 95.25% |   100.00% | 97.57% |

### Primary expanded benchmark

The 50-region normalized comparison produced:

* **2,592 truth variants**
* **2,469 project variants**
* **2,469 shared variants**
* **123 missed truth variants**
* **0 project-only variants**
* **95.25% recall**
* **100.00% precision**
* **97.57% F1**

The 50-region benchmark provides the broadest regional validation within the current study design.

---

# 🧪 Formal RTG vcfeval Benchmark

The 50-region analysis was additionally evaluated using RTG `vcfeval`.

| Metric          |     Result |
| --------------- | ---------: |
| TP baseline     |      2,465 |
| TP call         |      2,465 |
| False positives |          4 |
| False negatives |        127 |
| Precision       | **99.84%** |
| Sensitivity     | **95.10%** |
| F-measure       | **97.41%** |

The formal RTG benchmark therefore produced:

> **95.10% sensitivity · 99.84% precision · 97.41% F-measure**

---

# ⚖️ Normalized Comparison vs Formal Benchmarking

The two approaches showed strong agreement but were not identical.

| Metric                | `bcftools isec` | RTG `vcfeval` |
| --------------------- | --------------: | ------------: |
| True/shared positives |           2,469 |         2,465 |
| False positives       |               0 |             4 |
| False negatives       |             123 |           127 |
| Recall / sensitivity  |          95.25% |        95.10% |
| Precision             |         100.00% |        99.84% |
| F1 / F-measure        |          97.57% |        97.41% |

The formal benchmark was slightly stricter than the normalized record-level comparison.

This difference demonstrates an important methodological point:

> **Simple record-level VCF concordance should not automatically be interpreted as equivalent to formal benchmark performance.**

---

# 🔎 Missed-Variant Analysis

The 50-region normalized comparison identified **123 truth variants that were not recovered by the project callset**.

Their observed composition was:

| Variant class | Missed variants |
| ------------- | --------------: |
| Deletions     |              66 |
| Insertions    |              56 |
| SNVs          |               1 |
| **Total**     |         **123** |

The residual missed variants were therefore overwhelmingly indel events.

This observation motivates further investigation of:

* indel representation,
* alignment complexity,
* local sequence context,
* difficult genomic regions,
* and variant-calling sensitivity.

---

# 📍 Low-Recall Regional Analysis

Aggregate performance can conceal localized weaknesses.

A dedicated regional analysis was therefore implemented using a configured low-recall threshold of:

> **92% recall**

Regions below this threshold are examined independently to determine whether reduced performance is associated with particular genomic contexts.

This creates an additional analytical layer:

```text
Global benchmark performance
            ↓
Regional performance
            ↓
Low-recall regions
            ↓
Potential difficult genomic contexts
            ↓
Targeted error interpretation
```

---

# 🧩 Error and Discrepancy Analysis

The project does not stop at reporting recall and precision.

It explicitly examines discrepancies through:

### Missed-variant analysis

Identifies variants present in the benchmark but absent from the project callset.

### Variant-class analysis

Determines whether residual errors are dominated by SNVs, insertions, deletions, or other variant classes.

### Low-recall analysis

Identifies regions where performance falls below the predefined threshold.

### Benchmark-method comparison

Compares normalized `bcftools isec` results with formal RTG `vcfeval` results.

The resulting framework therefore moves from:

> **performance measurement**

to:

> **performance diagnosis**

---

# 📈 Publication-Ready Outputs

The final structured outputs are organized under:

[`results/publication_ready/`](results/publication_ready/)

They include:

### Tables

1. Benchmark-scale comparison
2. Formal RTG vcfeval result
3. Missed-variant summary
4. Low-recall regions
5. bcftools vs RTG discrepancy regions

### Figures

1. Benchmark-scale performance
2. bcftools isec vs RTG vcfeval
3. Missed-variant composition
4. Low-recall regional analysis
5. Benchmark-aware workflow overview

---

# 🧰 Software and Tools

| Analysis stage      | Software          |
| ------------------- | ----------------- |
| Programming         | Python            |
| Quality control     | FastQC            |
| QC aggregation      | MultiQC           |
| Read preprocessing  | fastp             |
| Alignment           | BWA-MEM2          |
| BAM processing      | samtools          |
| Variant processing  | bcftools / HTSlib |
| Formal benchmarking | RTG Tools         |
| Data analysis       | pandas / NumPy    |
| Visualization       | matplotlib        |
| Configuration       | YAML              |

The computational environment is specified in:

[`environment.yml`](environment.yml)

The benchmark configuration is specified in:

[`config/benchmark.yaml`](config/benchmark.yaml)

---

# ♻️ Reproducibility

Reproducibility is treated as a core research requirement.

The repository contains:

* workflow scripts,
* analysis scripts,
* benchmark configuration,
* software environment specification,
* provenance documentation,
* analytical reports,
* research records,
* compact derived results,
* publication-ready tables,
* and figures.

Large external sequencing and reference files are intentionally excluded from version control.

Excluded resources include:

* FASTQ/FASTQ.GZ
* BAM/BAI
* CRAM/CRAI
* large VCF/BCF files
* reference FASTA files
* genome indexes
* large intermediate outputs

See:

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

I am an MSc Bioinformatics graduate and early-career bioinformatics researcher working at the intersection of **computational genomics, NGS analysis, variant benchmarking, reproducible bioinformatics, and translational health research**.

My current research interests include:

* whole-genome sequencing
* variant discovery and validation
* genomic benchmarking
* computational genomics
* reproducible analysis workflows
* variant interpretation
* precision and preventive genomics
* computational approaches to biological and health research

This project represents my effort to develop a research workflow that goes beyond executing standard bioinformatics tools and instead emphasizes **benchmark design, reproducibility, quantitative validation, error analysis, and scientific interpretation**.

My broader research goal is to develop rigorous computational approaches that can connect genomic data analysis with meaningful biological and translational questions while maintaining appropriate scientific and clinical boundaries.

### Connect

* **Email:** `ritika.rawat27@outlook.com`
* **LinkedIn:** [Ritika Rajendra Rawat](YOUR_LINKEDIN_URL)
* **GitHub:** [@Rita1791](https://github.com/Rita1791)

---

# 🧭 Research Perspective

I approach computational genomics through four principles:

### Reproducibility

A computational result should be traceable to the data, parameters, software and analysis used to produce it.

### Benchmarking

Performance should be evaluated against an appropriate independent reference rather than assumed from successful pipeline execution.

### Error characterization

A single accuracy number is insufficient. Understanding where and why a workflow fails is equally important.

### Scientific restraint

Computational benchmark performance should not automatically be translated into clinical claims without appropriate validation.

These principles guide the design and interpretation of this repository.

---

# ⚠️ Scope and Limitations

This repository represents a **computational regional validation study**, not a clinical validation study.

The current analysis is limited to:

* HG001
* GRCh38
* chromosome 22
* selected GIAB high-confidence regions
* the evaluated sequencing dataset
* the implemented workflow configuration

Therefore, the current results should not be interpreted as evidence of:

* clinical diagnostic accuracy,
* clinical sensitivity or specificity,
* genome-wide performance,
* population-wide generalizability,
* universal variant-caller performance,
* or direct clinical decision-making capability.

Broader conclusions would require validation across additional:

* samples,
* chromosomes,
* benchmark regions,
* sequencing technologies,
* variant classes,
* and independent datasets.

---

# 🚀 Future Research

Potential extensions include:

1. Expansion to additional chromosomes.
2. Genome-wide GIAB benchmarking.
3. Validation across additional GIAB samples.
4. Comparison of multiple variant callers.
5. Variant-class-specific benchmarking.
6. Systematic difficult-region stratification.
7. Platform-aware benchmarking.
8. Reproducibility testing across computational environments.
9. Larger and more diverse benchmark datasets.
10. Extension toward population-scale and translational genomics research.

---

# 🏢 Acknowledgement

I acknowledge **Nainsense Labs Private Limited** for the professional environment and practical exposure that supported the development of this research work.

**Organization:** Nainsense Labs Private Limited
**Website:** `nainsense.com`
**Email:** `admin@nainsense.com`

This acknowledgement recognizes the professional environment and exposure associated with the development of the work and does not imply institutional endorsement of the scientific methodology, results, conclusions, or interpretations presented in this repository.

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

---

# 📄 License

This project is released under the **MIT License**.

See [`LICENSE`](LICENSE).

---

## Project Status

**Status:** Active research / benchmark validation

**Primary benchmark:** GIAB HG001

**Reference:** GRCh38

**Primary chromosome:** chr22

**Regional scales:** 5, 25, 50 regions

**Normalized comparison:** `bcftools isec`

**Formal benchmark:** RTG `vcfeval`

**Research focus:** Reproducible computational genomics and benchmark-aware WGS variant validation

---

### Researcher

**Ritika Rajendra Rawat**
MSc Bioinformatics | Bioinformatics Researcher
Computational Genomics • WGS • Variant Benchmarking • Reproducible Bioinformatics

**Email:** `ritika.rawat27@outlook.com`
**LinkedIn:** `https://www.linkedin.com/in/ritika-rawat-551107219/`
**GitHub:** [github.com/Rita1791](https://github.com/Rita1791)

---

> **Core contribution:** A benchmark-aware and reproducible framework for evaluating WGS variant-calling performance through progressively expanded regional validation, formal benchmarking, and systematic error characterization.
