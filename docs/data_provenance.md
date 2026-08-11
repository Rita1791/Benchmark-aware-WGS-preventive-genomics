# Data Provenance

## Purpose

This document records the provenance of external datasets and reference resources used by the WGS benchmarking workflow.

Large external datasets are not redistributed through this repository.

## Primary benchmark

| Resource | Value |
|---|---|
| Sample | HG001 |
| Alternate sample identifier | NA12878 |
| Benchmark provider | Genome in a Bottle (GIAB) |
| Reference build | GRCh38 |
| Primary chromosome | chr22 |
| Benchmark scope | Selected high-confidence regions |

## Sequencing data

The sequencing data used for local analysis are not stored in the repository.

The final reproducibility record should include:

- source database,
- accession,
- dataset/release version,
- file type,
- download date where relevant,
- checksum where practical.

## Truth set

The GIAB HG001 truth set used for benchmarking is stored locally and excluded from the repository because of file size.

The final provenance record should identify:

- exact GIAB release,
- truth VCF filename,
- confidence-region filename,
- reference build,
- source URL,
- checksum where available.

## Reference genome

The GRCh38 reference genome and associated indexes are stored locally and excluded from the repository.

The final provenance record should identify:

- exact reference source,
- release/version,
- FASTA filename,
- index-generation method,
- checksum where available.

## Repository data policy

The public repository contains computational code and compact derived results rather than raw sequencing or reference data.

Excluded data include:

- FASTQ/FASTQ.GZ,
- BAM/BAI,
- CRAM/CRAI,
- large VCF/BCF files,
- reference FASTA files,
- genome indexes,
- large intermediate outputs.

## Reproducibility requirement

A future reproduction of the study should use the same:

1. benchmark sample,
2. benchmark release,
3. reference build,
4. genomic regions,
5. software versions,
6. workflow parameters.

The exact provenance information should be updated before the repository is considered publication-ready.
