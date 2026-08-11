# Reviewer Summary

## Study

**Benchmark-aware regional validation of a reproducible WGS variant-calling workflow using GIAB HG001 chr22 reference regions**

## Research objective

This study evaluates the accuracy, reproducibility, and benchmark sensitivity of a whole-genome sequencing (WGS) variant-calling workflow using Genome in a Bottle (GIAB) HG001/NA12878 benchmark material and the GRCh38 reference genome.

The current analysis focuses on selected high-confidence chromosome 22 regions rather than the complete genome.

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

## Primary benchmark

The final 50-region evaluation was assessed using formal RTG `vcfeval` benchmarking.

The benchmark identified:

- True positives: 2,465
- False positives: 4
- False negatives: 127
- Precision: 99.84%
- Sensitivity: 95.10%
- F-measure: 97.41%

## Normalized comparison

The corresponding normalized `bcftools isec` comparison identified:

- Truth variants: 2,592
- Shared variants: 2,469
- Truth-only missed variants: 123
- Project-only extra variants: 0
- Recall: 95.25%
- Precision: 100.00%
- F1: 97.57%

## Benchmark-scale comparison

The workflow was evaluated across progressively expanded regional benchmark scopes.

| Benchmark | Truth variants | Shared variants | Missed variants | Extra variants | Recall | Precision | F1 |
|---|---:|---:|---:|---:|---:|---:|---:|
| 5-region | 444 | 428 | 16 | 0 | 96.40% | 100.00% | 98.17% |
| 25-region | 1,504 | 1,421 | 83 | 0 | 94.48% | 100.00% | 97.16% |
| 50-region | 2,592 | 2,469 | 123 | 0 | 95.25% | 100.00% | 97.57% |

Performance remained within a relatively narrow range across the evaluated benchmark scopes. Recall decreased from 96.40% at 5 regions to 94.48% at 25 regions before increasing to 95.25% at 50 regions.

## Missed-variant analysis

The normalized 50-region comparison identified 123 truth-only missed variants.

The observed missed variants were:

| Variant class | Count |
|---|---:|
| Deletion | 66 |
| Insertion | 56 |
| SNV | 1 |

Thus, 122 of the 123 missed variants were indels.

This indicates that the dominant observed error category within the evaluated benchmark was indel detection rather than broad SNV failure.

## Difficult genomic regions

A total of 77 of the 123 missed variants overlapped annotated difficult genomic regions, corresponding to 62.6% of the missed variants.

This observation indicates substantial overlap between missed variants and annotated difficult genomic contexts.

A formal statistical enrichment analysis is not claimed because an appropriate background set and enrichment model were not evaluated.

## Low-recall regions

Ten benchmark regions had recall below 92%.

These regions contained:

- 56 missed variants
- 31 deletions
- 24 insertions
- 1 SNV
- 32 missed variants overlapping difficult-region annotations

The low-recall analysis therefore identifies a subset of benchmark regions in which indel detection and difficult genomic contexts contribute substantially to the observed missed variants.

## Benchmark-method discrepancy

The normalized `bcftools isec` comparison and formal RTG `vcfeval` benchmark were highly concordant but not identical.

Differences were observed in:

- region_14
- region_20
- region_30
- region_40

The formal RTG benchmark produced:

- 2,465 true positives
- 4 false positives
- 127 false negatives

compared with:

- 2,469 shared variants
- 0 project-only variants
- 123 truth-only variants

from the normalized comparison.

## Principal finding

Within the evaluated chromosome 22 benchmark, the workflow demonstrated high precision and high overall benchmark performance.

The dominant observed error category was indel detection, with substantial overlap between missed variants and annotated difficult genomic contexts.

## Scientific interpretation

The findings support the use of benchmark-aware regional validation as a reproducibility framework for WGS variant-calling research.

The results should be interpreted within the scope of the evaluated GIAB HG001 GRCh38 chromosome 22 regions.

They do not establish whole-genome clinical diagnostic performance.

## Main contribution

The study integrates:

1. reproducible WGS processing,
2. benchmark-aware regional validation,
3. progressive benchmark-scale evaluation,
4. normalized variant comparison,
5. formal RTG `vcfeval` benchmarking,
6. missed-variant classification,
7. difficult-region analysis,
8. low-recall region analysis, and
9. benchmark-method discrepancy analysis.

Together, these components provide a transparent framework for evaluating variant-calling performance and identifying specific areas requiring further workflow optimization.

## Limitations

The principal limitations are:

- evaluation restricted to selected chromosome 22 regions,
- dependence on the GIAB HG001 benchmark,
- limited genomic representation relative to whole-genome analysis,
- observed sensitivity limitations for indels,
- substantial overlap of missed variants with difficult genomic contexts,
- absence of a formal statistical enrichment analysis,
- absence of whole-genome clinical validation.

## Future work

Future validation should include:

- whole-genome GIAB benchmarking,
- additional chromosomes,
- additional GIAB benchmark samples,
- independent sequencing datasets,
- alternative variant callers,
- improved indel detection,
- expanded difficult-region analysis,
- and formal statistical analysis of error enrichment.

## Reproducibility

The public repository intentionally excludes large sequencing and reference files.

The repository provides:

- computational pipeline scripts,
- analysis scripts,
- benchmark configuration,
- documentation,
- compact derived result tables,
- manuscript material,
- and figure-generation code.

Large FASTQ, BAM/BAI, VCF/BCF, reference genome, genome-index, and intermediate files remain outside the public repository.

The repository therefore separates computational provenance from large input data while preserving the analytical logic required to inspect and reproduce the study.
