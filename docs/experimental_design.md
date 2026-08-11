# Experimental Design

## Overview

The study uses a staged regional benchmarking design to evaluate a WGS variant-calling workflow against GIAB HG001/NA12878 benchmark data mapped to the GRCh38 reference genome.

The analysis focuses on chromosome 22 high-confidence benchmark regions.

## Experimental progression

The benchmark was evaluated at three scales:

| Benchmark | Truth variants | Shared variants | Missed truth | Extra project | Recall | Precision | F1 |
|---|---:|---:|---:|---:|---:|---:|---:|
| 5-region | 444 | 428 | 16 | 0 | 96.40% | 100.00% | 98.17% |
| 25-region | 1,504 | 1,421 | 83 | 0 | 94.48% | 100.00% | 97.16% |
| 50-region | 2,592 | 2,469 | 123 | 0 | 95.25% | 100.00% | 97.57% |

## Primary formal benchmark

The 50-region benchmark was additionally evaluated using RTG `vcfeval`.

| Metric | Value |
|---|---:|
| True positives | 2,465 |
| False positives | 4 |
| False negatives | 127 |
| Precision | 99.84% |
| Sensitivity | 95.10% |
| F-measure | 97.41% |

## Experimental logic

The analysis follows this sequence:

1. Select GIAB HG001 benchmark regions.
2. Extract or prepare the corresponding sequencing/alignment data.
3. Perform variant calling.
4. Normalize truth and project VCF representations.
5. Compare normalized callsets using `bcftools isec`.
6. Perform formal benchmarking using RTG `vcfeval`.
7. Aggregate region-level results.
8. Identify missed variants.
9. Classify missed variants by variant type.
10. Annotate difficult genomic contexts.
11. Identify low-recall regions.
12. Compare results from the two benchmarking approaches.

## Primary endpoint

The primary benchmark endpoint is RTG `vcfeval` performance across the final 50-region chromosome 22 evaluation.

## Secondary endpoints

Secondary endpoints include:

- normalized recall,
- normalized precision,
- normalized F1,
- variant-class distribution of missed variants,
- difficult-region enrichment,
- low-recall regions,
- discrepancy between `bcftools isec` and RTG `vcfeval`.

## Interpretation

The staged design is intended to determine whether performance observed in a small regional evaluation remains consistent when the evaluation is expanded.

The 50-region analysis is treated as the principal regional evaluation because it covers the largest number of benchmark variants and genomic contexts among the tested regional configurations.
