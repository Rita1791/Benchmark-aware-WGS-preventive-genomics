# Methodology

## 1. Study framework

The workflow was developed as a reproducible WGS variant-calling validation framework using Genome in a Bottle (GIAB) HG001/NA12878 benchmark material.

The analysis uses the GRCh38 reference genome and focuses on chromosome 22 high-confidence benchmark regions.

## 2. Benchmark material

The primary benchmark sample is GIAB HG001, also known as NA12878.

The benchmark consists of:

- HG001 sequencing data,
- GRCh38 reference sequence,
- GIAB truth variants,
- high-confidence benchmark regions.

Large reference and sequencing files are intentionally excluded from this repository because of their size and because they can be obtained independently from their respective public sources.

## 3. Regional benchmark construction

The analysis was performed using progressively expanded chromosome 22 benchmark region sets:

- 5 regions,
- 25 regions,
- 50 regions.

The regional approach was used to permit iterative workflow development, controlled benchmarking, and detailed error analysis.

## 4. Sequencing data processing

The computational workflow includes the following major stages:

1. sequencing-data quality control,
2. adapter/quality trimming,
3. read alignment,
4. alignment processing and indexing,
5. variant calling,
6. VCF normalization,
7. benchmark comparison.

The exact software versions and command-line parameters used for the final analysis should be recorded in the repository environment and pipeline documentation.

## 5. Alignment

Reads were aligned against the GRCh38 reference genome.

Alignment outputs were sorted and indexed before variant calling and downstream analysis.

## 6. Variant calling

Variant calling was performed using the project WGS variant-calling workflow.

The final repository should preserve the exact scripts and parameters used for the reported benchmark so that the public implementation corresponds to the reported analysis.

## 7. VCF normalization

Truth and project VCF files were normalized before direct comparison.

Normalization was used to reduce differences caused by alternative representations of the same variant, particularly for indels.

## 8. Normalized comparison

Normalized project and truth VCFs were compared using `bcftools isec`.

For each benchmark region, the following categories were evaluated:

- shared variants,
- truth-only variants,
- project-only variants.

These categories were used to calculate:

$$
Recall = \frac{TP}{TP + FN}
$$

$$
Precision = \frac{TP}{TP + FP}
$$

$$
F1 = 2 \times \frac{Precision \times Recall}{Precision + Recall}
$$

## 9. Formal benchmarking

RTG `vcfeval` was used as an independent benchmark evaluation method.

The analysis was performed across the final 50 benchmark regions.

The resulting true-positive, false-positive, and false-negative counts were aggregated to obtain:

- precision,
- sensitivity,
- F-measure.

## 10. Discrepancy analysis

Results from normalized `bcftools isec` comparison were compared with RTG `vcfeval`.

Regions showing differences in TP, FP, or FN counts were identified for further investigation.

Four regions showed discrepancies between the two approaches:

- region_14
- region_20
- region_30
- region_40

## 11. Missed-variant analysis

Truth-only variants from the 50-region benchmark were classified according to variant type.

The observed missed variants included:

- deletions,
- insertions,
- SNVs.

## 12. Difficult-region analysis

Missed variants were examined for overlap with difficult-region annotations.

This analysis was used to determine whether reduced recall was associated with challenging genomic contexts.

## 13. Low-recall analysis

Benchmark regions with recall below 92% were separately evaluated.

Ten regions met this criterion and contained 56 missed variants.

## 14. Reproducibility principle

Raw sequencing data, BAM files, reference genomes, and large benchmark resources are not stored in the repository.

Instead, the repository should contain:

- processing scripts,
- configuration,
- documentation,
- analysis code,
- compact result tables,
- publication-ready summaries,
- instructions for obtaining required public resources.

This design separates computational provenance from large input datasets.
