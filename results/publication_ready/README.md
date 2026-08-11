# Publication-Ready Results

This directory contains the final structured tables and figures generated from the benchmark-aware WGS variant-calling validation analysis.

The outputs summarize the primary benchmark results, formal benchmarking, residual errors, regional performance, and methodological comparison.

---

## 🔬 Primary Research Result

The primary expanded validation uses **50 selected GIAB HG001 GRCh38 chr22 benchmark regions**.

### Normalized record-level comparison

| Metric | Result |
|---|---:|
| Truth variants | 2,592 |
| Project variants | 2,469 |
| Shared variants | 2,469 |
| Missed truth variants | 123 |
| Extra project variants | 0 |
| Recall | **95.25%** |
| Precision | **100.00%** |
| F1 | **97.57%** |

### Formal RTG vcfeval benchmark

| Metric | Result |
|---|---:|
| True positives | 2,465 |
| False positives | 4 |
| False negatives | 127 |
| Sensitivity | **95.10%** |
| Precision | **99.84%** |
| F-measure | **97.41%** |

The two approaches show strong agreement while demonstrating a small number of benchmark-method-specific discrepancies.

---

# 📊 Tables

## Table 1 — Benchmark Scale Comparison

Compares performance across progressively expanded validation scopes:

- 5-region
- 25-region
- 50-region

**Markdown:**  
[Table 1 — Benchmark Scale Comparison](tables/table_1_benchmark_scale_comparison.md)

**TSV:**  
[Table 1 — Machine-readable TSV](tables/table_1_benchmark_scale_comparison.tsv)

---

## Table 2 — Formal RTG vcfeval Benchmark

Reports the formal 50-region RTG vcfeval benchmark.

**Markdown:**  
[Table 2 — Formal RTG vcfeval Result](tables/table_2_formal_rtg_vcfeval_result.md)

**TSV:**  
[Table 2 — Machine-readable TSV](tables/table_2_formal_rtg_vcfeval_result.tsv)

---

## Table 3 — Missed Variant Summary

Summarizes truth variants missed by the project callset according to variant class.

**Markdown:**  
[Table 3 — Missed Variant Summary](tables/table_3_missed_variant_summary.md)

**TSV:**  
[Table 3 — Machine-readable TSV](tables/table_3_missed_variant_summary.tsv)

---

## Table 4 — Low-Recall Regions

Identifies benchmark regions below the configured recall threshold.

Current threshold:

```text
92%
