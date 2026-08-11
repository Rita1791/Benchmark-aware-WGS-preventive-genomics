# Reproducibility

## Reproducibility objective

The repository is designed to preserve the computational logic required to understand and reproduce the reported analysis without storing large sequencing or reference files.

## Repository contains

The public repository should contain:

- pipeline scripts,
- analysis scripts,
- configuration,
- documentation,
- compact result tables,
- manuscript text,
- figure-generation code,
- publication-ready summaries.

## Repository excludes

The following large resources are intentionally excluded:

- raw FASTQ files,
- BAM files,
- BAI files,
- VCF/BCF datasets where large,
- reference FASTA files,
- genome indexes,
- large SRA downloads,
- large intermediate outputs.

## Reproducibility requirements

A complete reproduction requires:

1. obtaining the same public benchmark resources,
2. obtaining the same reference genome,
3. using the documented software environment,
4. executing the documented pipeline,
5. generating normalized VCFs,
6. running the benchmark comparisons,
7. generating compact result tables,
8. generating the publication figures.

## Provenance

For every externally obtained dataset or reference resource, the final repository should record:

- source,
- accession or identifier,
- version/release,
- download date where relevant,
- checksum where practical.

## Computational environment

The repository uses `environment.yml` to document software dependencies.

Tool versions should be pinned whenever practical, particularly for:

- BWA/BWA-MEM2,
- samtools,
- bcftools,
- tabix,
- FastQC,
- fastp,
- MultiQC,
- RTG Tools,
- Python.

## Determinism

Where tools support deterministic execution, fixed parameters and consistent input ordering should be used.

## Result provenance

Final reported metrics should originate from analysis outputs rather than being manually typed into publication tables.

This is particularly important for preventing discrepancies between the computational analysis, manuscript, tables, and figures.
