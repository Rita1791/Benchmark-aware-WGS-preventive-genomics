# Error Analysis

## Overview

Error analysis was performed to characterize the observed benchmark failures by variant class, genomic context, and benchmark region.

## Missed variant composition

The normalized 50-region comparison identified 123 truth-only missed variants.

| Variant class | Missed variants |
|---|---:|
| Deletion | 66 |
| Insertion | 56 |
| SNV | 1 |

Thus, 122 of the 123 missed variants were indels.

## Difficult-region overlap

Of the 123 missed variants, 77 overlapped annotated difficult genomic regions, corresponding to 62.6% of the missed variants.

This observation indicates substantial overlap between missed variants and annotated difficult genomic contexts.

A formal statistical enrichment analysis would require an appropriate background set and is not claimed here.

## Low-recall regions

Ten regions had recall below 92%.

Together, these regions contained:

- 56 missed variants
- 31 deletions
- 24 insertions
- 1 SNV
- 32 missed variants overlapping difficult-region annotations

## Interpretation

The observed error profile was strongly concentrated in indel detection rather than being broadly distributed across SNVs.

The overlap with difficult genomic regions suggests that genomic context is an important characteristic of the observed misses.

These observations identify indel detection and difficult genomic contexts as priority areas for future workflow optimization.

## Benchmark-method discrepancy

The normalized `bcftools isec` comparison and RTG `vcfeval` results were highly concordant but not identical.

Differences were observed in:

- region_14
- region_20
- region_30
- region_40

RTG `vcfeval` produced the more conservative formal benchmark.

## Limitations of the error analysis

The current analysis is descriptive.

It does not establish statistical enrichment of indels or difficult regions because an appropriate genomic background and formal enrichment model were not evaluated.
