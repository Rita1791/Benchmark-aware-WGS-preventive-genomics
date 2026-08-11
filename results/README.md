# Results

> **Benchmark-aware regional validation of a reproducible WGS variant-calling workflow using GIAB HG001 chr22 reference regions**

This directory contains the computational results generated during development, validation, benchmarking, error analysis, and publication preparation of the WGS variant-calling workflow.

The project evaluates a human WGS variant-calling workflow against the **Genome in a Bottle (GIAB) HG001 / NA12878 GRCh38 benchmark**, with a primary focus on chromosome 22.

---

## 🧬 Results at a Glance

| Analysis | Scope | Primary purpose | Status |
|---|---:|---|---|
| Benchmark readiness | chr22 | Verify benchmark resources and inputs | ✅ Complete |
| Initial benchmark | 5 regions | Controlled regional validation | ✅ Complete |
| Expanded benchmark | 25 regions | Increased validation scope | ✅ Complete |
| Primary expanded benchmark | 50 regions | Main regional validation | ✅ Complete |
| Formal benchmarking | 50 regions | RTG `vcfeval` validation | ✅ Complete |
| Missed-variant analysis | 50 regions | Characterize false negatives | ✅ Complete |
| Low-recall analysis | 50 regions | Identify problematic regions | ✅ Complete |
| Method comparison | 50 regions | Compare `bcftools isec` and RTG | ✅ Complete |
| Publication tables | Final results | Structured result summaries | ✅ Complete |
| Publication figures | Final results | Visual result summaries | ✅ Complete |

---

# 🔬 Main Scientific Question

The results address a central methodological question:

> **Does the WGS variant-calling workflow maintain reliable benchmark performance as the validation scope expands, and what explains the remaining discrepancies?**

The analysis therefore does not rely on a single accuracy number.

Instead, it evaluates:

```text
Benchmark scale
      │
      ├── 5 regions
      │
      ├── 25 regions
      │
      └── 50 regions
             │
             ▼
      Variant concordance
             │
             ├── Recall
             ├── Precision
             └── F1
             │
             ▼
      Formal benchmarking
             │
             └── RTG vcfeval
             │
             ▼
      Error characterization
             │
             ├── Missed variants
             ├── Variant type
             ├── Difficult regions
             └── Low-recall regions
             │
             ▼
      Method comparison
             │
             └── bcftools isec vs RTG vcfeval
