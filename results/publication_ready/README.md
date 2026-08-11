# Publication-Ready Results

This directory contains the final structured tables and figures generated from the benchmark-aware WGS validation analysis.

## Tables

| Table | Description |
|---|---|
| [Table 1](tables/table_1_benchmark_scale_comparison.md) | Benchmark performance across 5-, 25-, and 50-region validation |
| [Table 2](tables/table_2_formal_rtg_vcfeval_result.md) | Formal RTG vcfeval benchmark |
| [Table 3](tables/table_3_missed_variant_summary.md) | Missed variants by variant class |
| [Table 4](tables/table_4_low_recall_regions.md) | Regions below the configured recall threshold |
| [Table 5](tables/table_5_bcftools_vs_rtg_discrepancy_regions.md) | Region-level differences between bcftools isec and RTG vcfeval |

## Figures

| Figure | Description |
|---|---|
| Figure 1 | Benchmark-scale performance |
| Figure 2 | bcftools isec vs RTG vcfeval |
| Figure 3 | Missed-variant composition |
| Figure 4 | Low-recall benchmark regions |
| Figure 5 | Benchmark-aware WGS validation workflow |

## Primary benchmark

The primary expanded validation uses 50 selected GIAB HG001 GRCh38 chr22 regions.

### Normalized record-level comparison

- Recall: **95.25%**
- Precision: **100.00%**
- F1: **97.57%**

### Formal RTG vcfeval benchmark

- Sensitivity: **95.10%**
- Precision: **99.84%**
- F-measure: **97.41%**

## Reproducibility

The tables and figures are derived from the computational results and analysis scripts in the repository.

The publication-ready outputs should be regenerated whenever the underlying benchmark results change.
