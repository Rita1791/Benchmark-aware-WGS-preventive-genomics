# Reviewer Summary

## Study

**Benchmark-aware regional validation of a reproducible WGS variant-calling workflow using GIAB HG001 chr22 reference regions**

## Research objective

This study evaluates the accuracy, reproducibility, and benchmark sensitivity of a whole-genome sequencing variant-calling workflow using Genome in a Bottle (GIAB) HG001/NA12878 benchmark material and GRCh38 chromosome 22 high-confidence regions.

The analysis focuses on whether variant-calling performance remains stable when benchmark evaluation is progressively expanded from a small regional validation set to a larger set of genomic regions.

## Study design

The workflow was evaluated using:

- GIAB HG001/NA12878 benchmark material
- GRCh38 reference genome
- chromosome 22 high-confidence benchmark regions
- progressive 5-, 25-, and 50-region evaluations
- normalized `bcftools isec` comparison
- formal RTG `vcfeval` benchmarking
- missed-variant analysis
- low-recall region analysis
- difficult-region annotation analysis
- discrepancy analysis between benchmarking approaches

## Primary result

The final 50-region RTG `vcfeval` benchmark identified:

- True positives: 2,465
- False positives: 4
- False negatives: 127
- Precision: 99.84%
- Sensitivity: 95.10%
- F-measure: 97.41%

## Supporting normalized comparison

The corresponding normalized `bcftools isec` comparison identified:

- Truth variants: 2,592
- Shared variants: 2,469
- Truth-only variants: 123
- Project-only variants: 0
- Recall: 95.25%
- Precision: 100.00%
- F1: 97.57%

## Principal error pattern

Missed variants were strongly enriched for indels:

- Deletions: 66
- Insertions: 56
- SNVs: 1

A total of 77 missed variants had difficult-region annotations.

The results therefore indicate that the principal remaining limitation is not broad SNV detection, but sensitivity to indels and difficult genomic contexts.

## Scientific interpretation

The results support the use of benchmark-aware regional validation as a reproducibility framework for WGS variant-calling research.

However, the study is not a whole-genome clinical validation study. The analysis is restricted to selected GRCh38 chromosome 22 benchmark regions and should therefore be interpreted as a research validation framework rather than evidence of clinical diagnostic performance.

## Key contribution

The main contribution is the integration of:

1. reproducible WGS processing,
2. benchmark-aware regional validation,
3. independent formal benchmarking,
4. scale-dependent evaluation,
5. discrepancy analysis, and
6. systematic investigation of missed variants.

The resulting workflow provides a transparent framework for identifying where a variant-calling pipeline performs well and where additional optimization is required.
