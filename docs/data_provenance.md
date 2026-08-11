# Data Provenance

## Purpose

This document records the provenance, identity, and handling of external datasets and reference resources used by the benchmark-aware WGS variant-calling workflow.

Large sequencing datasets, reference genomes, and derived alignment/variant files are **not redistributed through this repository**. They are obtained and processed locally.

---

## 1. Primary benchmark

| Attribute | Value |
|---|---|
| Benchmark provider | Genome in a Bottle (GIAB) |
| Benchmark sample | HG001 |
| Alternate sample identifier | NA12878 |
| Reference build | GRCh38 |
| Primary chromosome | chr22 |
| Truth-set release | GIAB v4.2.1 |
| Benchmark scope | Selected high-confidence chr22 regions |
| Region scales evaluated | 5, 25, and 50 regions |

HG001 is the primary benchmark sample used throughout the validation workflow. NA12878 is retained as an alternate identifier because HG001 is historically associated with the NA12878 sample designation.

---

## 2. Sequencing data

The whole-genome sequencing data used for the workflow are stored locally and are intentionally excluded from the public repository.

The repository therefore does not redistribute the raw sequencing reads.

The local analysis workspace includes sequencing datasets used for:

- initial workflow testing,
- read preprocessing and quality control,
- alignment,
- chromosome 22 extraction,
- reduced-scale and 1M-read experiments,
- variant calling,
- benchmark comparison.

Where applicable, the final analysis record should retain the following metadata:

| Metadata | Status |
|---|---|
| Source database | Documented in project records |
| Accession | Documented in dataset-selection records |
| Dataset identifier | Documented in project records |
| File format | FASTQ / compressed FASTQ |
| Download date | To be recorded where available |
| Checksum | To be recorded where available |

Raw FASTQ/SRA files are excluded through `.gitignore`.

---

## 3. GIAB truth set

The GIAB HG001 truth resources are used as the benchmark truth set for regional variant validation.

### Current benchmark identity

| Attribute | Value |
|---|---|
| Sample | HG001 |
| Assembly | GRCh38 |
| Release | v4.2.1 |
| Chromosome | chr22 |
| Truth resource | HG001 GRCh38 v4.2.1 benchmark truth set |
| Confidence regions | GRCh38 high-confidence benchmark regions |

The local workspace contains the GIAB truth resources required for regional benchmarking.

Large truth VCF files and associated indexes are excluded from the public repository.

The compact BED region definitions used by the analysis may be retained in the repository where they are sufficiently small and represent explicit analysis inputs.

---

## 4. Reference genome

The workflow uses the GRCh38 reference sequence for chromosome 22.

The reference FASTA and computational indexes are maintained locally and are not redistributed through this repository.

### Reference identity

| Attribute | Value |
|---|---|
| Genome build | GRCh38 |
| Primary chromosome | chr22 |
| Reference sequence | GRCh38 chr22 FASTA |
| Alignment indexes | Generated locally |
| Variant-normalization reference | Same GRCh38 reference |
| RTG benchmark reference | GRCh38-compatible reference |

Reference indexes are generated from the corresponding reference sequence and are excluded from version control.

---

## 5. Benchmark regions

The workflow evaluates progressively larger sets of selected chr22 regions:

| Benchmark | Number of regions | Purpose |
|---|---:|---|
| 5-region | 5 | Initial regional validation |
| 25-region | 25 | Expanded validation |
| 50-region | 50 | Primary expanded regional benchmark |

The regions are selected from GIAB high-confidence benchmark resources and are intended to provide increasingly broad regional validation.

The analysis should **not** interpret these regional sets as independent biological replicates. They represent different validation scopes within the same chromosome and benchmark sample.

---

## 6. Derived analysis files

The following files are generated during the computational workflow and are not treated as primary external datasets:

- aligned BAM files,
- BAM indexes,
- called VCF/BCF files,
- normalized VCF files,
- RTG vcfeval outputs,
- intermediate comparison files,
- temporary pipeline files,
- alignment and variant-calling logs.

Large derived files remain local.

Compact, publication-relevant summaries may be retained in the repository, including:

- benchmark summary tables,
- region-level summary tables,
- missed-variant summaries,
- low-recall region summaries,
- bcftools versus RTG discrepancy tables,
- publication-ready figures.

---

## 7. Data processing lineage

The principal data lineage is:

```text
External sequencing data
        |
        v
Quality control / preprocessing
        |
        v
Read alignment to GRCh38
        |
        v
chr22-focused analysis
        |
        v
Variant calling
        |
        v
VCF normalization
        |
        +----------------------+
        |                      |
        v                      v
bcftools isec             RTG vcfeval
        |                      |
        +----------+-----------+
                   |
                   v
        Benchmark comparison
                   |
                   v
        Error / missed-variant
        / low-recall analysis
                   |
                   v
        Publication-ready
        summaries and figures
