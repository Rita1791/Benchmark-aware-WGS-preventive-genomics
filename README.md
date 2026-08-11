# Benchmark-Aware Regional Validation of a Reproducible WGS Variant-Calling Workflow

### GIAB HG001 • GRCh38 • Chromosome 22 • Regional Benchmarking • `bcftools isec` • RTG `vcfeval`

[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Python](https://img.shields.io/badge/Python-3.11-blue.svg)](environment.yml)
[![Genome Build](https://img.shields.io/badge/Genome-GRCh38-orange.svg)](config/benchmark.yaml)
[![Benchmark](https://img.shields.io/badge/Benchmark-GIAB%20HG001-purple.svg)](config/benchmark.yaml)

> A reproducible, benchmark-aware computational genomics workflow for evaluating WGS variant-calling performance across selected high-confidence regions of human chromosome 22 using the Genome in a Bottle (GIAB) HG001 benchmark.

---

## 🔬 Project Overview

Whole-genome sequencing (WGS) variant-calling pipelines can produce apparently credible variant sets while still exhibiting systematic errors in specific genomic contexts.

A benchmark therefore should not be treated simply as a single overall accuracy number.

This project investigates a **benchmark-aware regional validation strategy** in which variant-calling performance is evaluated across progressively expanded genomic region sets and examined using complementary comparison and benchmarking approaches.

The workflow uses:

* **GIAB HG001** as the benchmark sample
* **NA12878** as the alternate identifier for HG001
* **GRCh38** as the reference genome build
* **chromosome 22** as the primary analysis chromosome
* selected **GIAB high-confidence regions**
* normalized variant comparison using **`bcftools isec`**
* formal benchmarking using **RTG `vcfeval`**
* regional evaluation across **5-, 25-, and 50-region benchmark designs**
* systematic analysis of missed variants
* low-recall region analysis
* difficult genomic-region analysis
* discrepancy analysis between benchmarking approaches

The objective is not simply to produce a VCF.

The objective is to determine **where, how, and why a variant-calling workflow agrees or disagrees with a trusted benchmark**.

---

# 🎯 Research Question

### Primary question

> How does variant-calling performance change when benchmark evaluation is performed across progressively expanded high-confidence genomic regions, and what genomic characteristics contribute to missed or discrepant variants?

### Secondary questions

1. How consistent are normalized VCF comparisons and formal benchmarking?
2. Does benchmark scale influence apparent variant-calling performance?
3. Which genomic regions contribute disproportionately to reduced recall?
4. What types of variants are missed by the evaluated workflow?
5. Can regional error analysis reveal limitations that are hidden by aggregate performance metrics?
6. Can a benchmark-aware workflow provide a more informative validation framework than a single global performance estimate?

---

# 🧬 Scientific Motivation

Benchmarking is essential when evaluating computational variant-calling workflows because the presence of a variant in a VCF does not itself establish that the call is correct.

A rigorous validation framework requires comparison against an independently established truth set.

This project therefore separates three related concepts:

### 1. Variant discovery

Can the workflow identify candidate variants from sequencing data?

### 2. Benchmark agreement

How closely do the called variants agree with the GIAB benchmark?

### 3. Error localization

Where does the workflow fail, and what characteristics are associated with those failures?

This distinction is central to the project.

A high aggregate performance value can conceal localized weaknesses. Regional analysis is therefore used to expose performance heterogeneity rather than treating the genome as computationally uniform.

---

# 🧪 Benchmark Design

| Component             | Design                                                                |
| --------------------- | --------------------------------------------------------------------- |
| Benchmark sample      | HG001                                                                 |
| Alternate identifier  | NA12878                                                               |
| Benchmark resource    | Genome in a Bottle (GIAB)                                             |
| Reference genome      | GRCh38                                                                |
| Primary chromosome    | chr22                                                                 |
| Benchmark regions     | Selected GIAB high-confidence regions                                 |
| Regional scales       | 5, 25, 50 regions                                                     |
| Normalized comparison | `bcftools isec`                                                       |
| Formal benchmarking   | RTG `vcfeval`                                                         |
| Error analysis        | Missed variants, low-recall regions, difficult regions, discrepancies |

The regional design allows the workflow to be evaluated at multiple scales rather than relying on a single predefined region.

---

# 🧠 Methodological Framework

```text
                    RAW SEQUENCING DATA
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
                    │ Trimming      │
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
                    │ Region-aware  │
                    │ filtering     │
                    └───────┬───────┘
                            │
                            ▼
             ┌────────────────────────────┐
             │ GIAB HG001 benchmark truth │
             └──────────────┬─────────────┘
                            │
                 ┌──────────┴──────────┐
                 ▼                     ▼
        ┌────────────────┐    ┌────────────────┐
        │ bcftools isec  │    │ RTG vcfeval    │
        │ normalized     │    │ formal         │
        │ comparison     │    │ benchmarking   │
        └───────┬────────┘    └───────┬────────┘
                │                     │
                └──────────┬──────────┘
                           ▼
                 ┌────────────────────┐
                 │ Regional error     │
                 │ and discrepancy    │
                 │ analysis           │
                 └─────────┬──────────┘
                           ▼
                 ┌────────────────────┐
                 │ Tables / Figures   │
                 │ / Reports          │
                 └────────────────────┘
```

---

# 📈 Regional Benchmarking Strategy

The central methodological feature of this repository is **progressive regional benchmarking**.

Three benchmark scales are defined:

| Benchmark scale | Purpose                                                |
| --------------- | ------------------------------------------------------ |
| 5-region        | Initial controlled regional validation                 |
| 25-region       | Expanded benchmark evaluation                          |
| 50-region       | Broader regional assessment and error characterization |

This design makes it possible to examine whether apparent performance is stable as the benchmark scope increases.

The project therefore treats benchmark size and regional composition as analytical variables rather than simply technical details.

---

# 🔍 Two Complementary Comparison Strategies

## `bcftools isec`

`bcftools isec` is used for normalized comparison of the benchmark and called variant sets.

This enables identification of:

* variants private to the truth set
* variants private to the called set
* variants shared between the two datasets

The resulting sets are used for downstream discrepancy and missed-variant analysis.

---

## RTG `vcfeval`

RTG `vcfeval` provides formal variant benchmarking using a representation-aware comparison framework.

It is used as a complementary evaluation method rather than assuming that a simple VCF intersection is sufficient for benchmarking.

This distinction is important because variant representation, normalization and complex variant matching can influence apparent agreement between datasets.

---

# 🧩 Error Analysis

Performance evaluation is followed by targeted analysis of disagreement.

The repository includes analyses focused on:

### Missed variants

Variants represented in the benchmark that were not recovered by the evaluated workflow.

### Low-recall regions

Regions where benchmark recall falls below the project-defined threshold.

### Difficult genomic contexts

Regions requiring additional investigation because genomic characteristics may complicate variant detection or representation.

### Benchmark discrepancies

Cases where normalized VCF comparison and formal benchmarking provide different interpretations of agreement.

The goal is to move from:

> **"How accurate is the pipeline?"**

toward:

> **"Where does the pipeline fail, and what explains the failure?"**

---

# 📊 Results and Research Outputs

The repository contains compact derived outputs rather than large sequencing datasets.

Key output categories include:

* benchmark-readiness reports
* regional benchmark reports
* variant comparison outputs
* low-recall analyses
* discrepancy analyses
* publication-oriented tables
* publication-oriented figures
* methodological documentation
* research logs

The results are organized so that computational outputs can be traced back to the corresponding analysis stage.

See:

* [`results/`](results/)
* [`reports/`](reports/)
* [`figures/`](figures/)
* [`docs/`](docs/)
* [`manuscript/`](manuscript/)

---

# 📁 Repository Structure

```text
Benchmark-aware-WGS-preventive-genomics/
│
├── config/
│   └── benchmark.yaml
│
├── data/
│   └── External / intermediate sequencing data
│
├── docs/
│   ├── lab_notebook/
│   ├── metadata/
│   ├── methodology/
│   ├── phd_positioning/
│   └── research_tracking/
│
├── figures/
│   └── Publication-oriented figures
│
├── logs/
│   └── Computational execution logs
│
├── manuscript/
│   └── Manuscript drafts and research text
│
├── pipeline/
│   └── Core pipeline stages
│
├── reference/
│   └── Local reference resources
│
├── reference_datasets/
│   └── GIAB benchmark resources and region definitions
│
├── reports/
│   └── Derived analytical reports
│
├── results/
│   └── Benchmarking and variant-level outputs
│
├── scripts/
│   └── Analysis and benchmarking scripts
│
├── tests/
│   └── Controlled test inputs and validation resources
│
├── CITATION.cff
├── LICENSE
├── README.md
├── .gitignore
├── environment.yml
└── config/benchmark.yaml
```

---

# ⚙️ Computational Environment

The computational environment is defined using Conda.

Core software includes:

| Category            | Tools                             |
| ------------------- | --------------------------------- |
| Programming         | Python 3.11                       |
| Quality control     | FastQC, MultiQC                   |
| Read processing     | fastp                             |
| Alignment           | BWA-MEM2                          |
| BAM processing      | samtools                          |
| Variant processing  | bcftools, HTSlib                  |
| Formal benchmarking | RTG Tools                         |
| Analysis            | pandas, NumPy, matplotlib, PyYAML |

Environment specification:

[`environment.yml`](environment.yml)

Benchmark configuration:

[`config/benchmark.yaml`](config/benchmark.yaml)

---

# ♻️ Reproducibility

Reproducibility is a core design principle of this project.

The repository records:

* computational scripts
* pipeline stages
* benchmark definitions
* configuration parameters
* software environment
* analytical reports
* research documentation
* provenance information
* publication-oriented outputs

Large sequencing and reference files are intentionally excluded from version control.

See:

* [`data_provenance`](docs/)
* [`software_versions`](docs/)
* [`.gitignore`](.gitignore)

A complete reproduction should use the same:

1. benchmark sample
2. GIAB release
3. reference genome build
4. benchmark region definitions
5. software versions
6. workflow parameters

---

# 🧪 Development Philosophy

The workflow was developed incrementally rather than attempting to execute a complete WGS pipeline in a single step.

The development sequence was:

```text
Controlled test
      ↓
Small/subsampled dataset
      ↓
Alignment validation
      ↓
Variant calling
      ↓
Benchmark readiness
      ↓
Regional benchmarking
      ↓
Expanded regional benchmarking
      ↓
Formal vcfeval benchmarking
      ↓
Error/discrepancy analysis
      ↓
Publication-oriented outputs
```

This staged strategy reduces computational risk and makes individual workflow components easier to validate.

It also creates a documented research trail showing how the methodology evolved.

---

# 🧑‍🔬 About the Researcher

## Ritika Rajendra Rawat

**Bioinformatics Researcher | Computational Genomics | WGS Variant Benchmarking**

I am a bioinformatics researcher working at the intersection of **computational genomics, NGS analysis, variant interpretation and translational health research**.

My research interests include:

* whole-genome sequencing
* variant discovery and benchmarking
* computational genomics
* reproducible bioinformatics
* genomic quality assessment
* benchmark-aware variant analysis
* precision and preventive genomics
* computational approaches to biological and clinical research questions

This repository represents an independent research effort to develop and document a computationally rigorous WGS variant-calling and benchmarking framework.

Rather than treating bioinformatics as a sequence of software commands, I use this project to investigate the methodological questions behind those commands:

> **What is being measured?**

> **Against what reference is it being measured?**

> **How robust is the measurement?**

> **Where does the computational workflow fail?**

> **Can the result be independently reproduced and critically evaluated?**

This research philosophy motivates the benchmark-aware regional design used throughout the project.

---

# 🎓 Research Development

This project is part of my broader development as a computational genomics researcher and is intended to strengthen my ability to independently:

* formulate computational research questions
* design reproducible analysis workflows
* work with benchmark datasets
* validate computational outputs
* investigate discrepancies
* document methodological decisions
* communicate results scientifically
* distinguish computational evidence from biological or clinical interpretation

The repository is therefore maintained as a **research record as well as a software repository**.

---

# 🏢 Research / Work Acknowledgement

I acknowledge **Nasense Labs Private Limited** for providing the professional environment and research context in which aspects of this computational genomics work were developed.

The organization provided exposure to applied computational biology, healthcare-oriented data analysis and practical research constraints that contributed to my development as a bioinformatics researcher.

This repository represents the computational research work and documentation maintained by **Ritika Rajendra Rawat**.

Where applicable, organizational acknowledgement does not imply institutional endorsement of the scientific conclusions, benchmark methodology or interpretations presented in this repository.

---

# ⚠️ Scope and Limitations

This project should be interpreted within its experimental scope.

The current benchmark framework focuses on:

* one primary benchmark sample: **HG001**
* GRCh38
* chromosome 22
* selected high-confidence benchmark regions
* regional rather than complete genome-wide validation

Therefore, conclusions from this repository should **not** automatically be generalized to:

* all human genomes
* all chromosomes
* all sequencing platforms
* all variant classes
* clinical diagnostic performance
* clinical sensitivity or specificity
* population-scale genomic diversity

The purpose of the project is methodological computational validation, not clinical validation.

Additional samples, chromosomes, sequencing technologies, variant classes and independent benchmark datasets would be required to establish broader generalizability.

---

# 🔐 Data and Privacy

Large external sequencing datasets, BAM/CRAM files, FASTQ files, reference genomes and large benchmark files are excluded from the public repository.

The repository is designed to expose:

* computational methods
* configuration
* compact derived results
* documentation
* reproducibility information

without redistributing large external datasets.

See [`data_provenance`](docs/) for the intended provenance record.

---

# 📚 Documentation

### Methodology

[`docs/methodology/WGS_NGS_PIPELINE_METHODOLOGY.md`](docs/methodology/WGS_NGS_PIPELINE_METHODOLOGY.md)

### Research log

[`docs/research_tracking/MASTER_RESEARCH_LOG.md`](docs/research_tracking/MASTER_RESEARCH_LOG.md)

### Data provenance

[`docs/`](docs/)

### Benchmark configuration

[`config/benchmark.yaml`](config/benchmark.yaml)

### Results

[`results/`](results/)

### Reports

[`reports/`](reports/)

### Figures

[`figures/`](figures/)

### Manuscript materials

[`manuscript/`](manuscript/)

---

# 📜 Citation

If you use this repository, workflow, derived analyses or methodological framework, please cite the repository using the information provided in:

[`CITATION.cff`](CITATION.cff)

---

# 📄 License

This project is released under the **MIT License**.

See [`LICENSE`](LICENSE).

---

# 🙏 Acknowledgements

I acknowledge the **Genome in a Bottle (GIAB) Consortium** and the developers and maintainers of the open-source tools used throughout this project.

I also acknowledge **Nainsense Labs Private Limited** for the professional environment and practical research exposure that supported the development of this work.

Finally, I acknowledge the broader open-source bioinformatics community whose software, benchmark resources and reproducibility practices make computational genomics research possible.

---

# 🚀 Research Direction

The current framework establishes a foundation for further investigation into:

* multi-sample benchmark validation
* additional chromosomes
* larger benchmark regions
* cross-tool variant-calling comparison
* platform-aware benchmarking
* variant-class-specific performance
* systematic difficult-region characterization
* reproducibility across computational environments
* extension toward population-scale and translational genomics research

The long-term objective is to develop increasingly rigorous computational frameworks for evaluating genomic analysis pipelines before downstream biological or health-related interpretation.

---

## Project Status

**Research stage:** Active development / benchmark analysis

**Primary benchmark:** GIAB HG001

**Reference:** GRCh38

**Primary analysis chromosome:** chr22

**Benchmark scales:** 5, 25 and 50 selected regions

**Primary comparison methods:** `bcftools isec` and RTG `vcfeval`

**Repository purpose:** Reproducible computational genomics research

---

### Author

**Ritika Rajendra Rawat**
Bioinformatics Researcher
Computational Genomics • WGS • Variant Benchmarking • Reproducible Bioinformatics

GitHub: [@Rita1791](https://github.com/Rita1791)
