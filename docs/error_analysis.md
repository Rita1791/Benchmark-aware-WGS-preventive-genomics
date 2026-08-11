# Error Analysis

## Overview

Error analysis was performed to determine whether benchmark failures were randomly distributed or concentrated in specific variant classes and genomic contexts.

## Missed variant composition

The normalized 50-region comparison identified 123 truth-only missed variants.

The distribution was:

| Variant class | Missed |
|---|---:|
| Deletion | 66 |
| Insertion | 56 |
| SNV | 1 |

Therefore, 122 of the 123 missed variants were indels.

This indicates that the dominant sensitivity limitation is associated with indel detection rather than SNV detection.

## Difficult-region enrichment

Of the 123 missed variants, 77 had difficult-region annotations.

This corresponds to approximately 62.6% of missed variants.

The enrichment suggests that challenging genomic contexts contribute substantially to reduced sensitivity.

## Low-recall regions

Ten regions had recall below 92%.

Together these regions contained 56 missed variants:

- 31 deletions
- 24 insertions
- 1 SNV

Thirty-two missed variants in these regions had difficult-region annotations.

## Interpretation

The error profile indicates a structured rather than uniform failure pattern.

The workflow performs strongly for SNVs but loses sensitivity primarily for indels, particularly when variants occur in difficult genomic contexts.

Potential contributing factors include:

- repetitive sequence,
- local sequence complexity,
- alignment ambiguity,
- representation of indels,
- limitations of short-read evidence,
- variant-calling sensitivity in difficult regions.

These mechanisms should be treated as hypotheses unless directly tested in additional experiments.

## Benchmark-method discrepancy

The normalized `bcftools isec` comparison and RTG `vcfeval` results were highly concordant but not identical.

Differences were observed in:

- region_14
- region_20
- region_30
- region_40

The formal RTG benchmark was slightly stricter.

## Key conclusion

The principal optimization target is indel sensitivity in difficult genomic contexts.

Future experiments should test whether alternative variant callers, local assembly approaches, improved filtering, or additional evidence integration reduce these errors.
