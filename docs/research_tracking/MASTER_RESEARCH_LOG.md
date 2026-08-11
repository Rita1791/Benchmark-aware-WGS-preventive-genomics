## Project

**Benchmark-aware regional validation of a reproducible WGS variant-calling workflow using GIAB HG001 chr22 reference regions**

---

## Research Objective

The project evaluates the performance and reproducibility of a WGS variant-calling workflow through regional benchmarking against the Genome in a Bottle (GIAB) HG001 truth set on GRCh38 chromosome 22.

The central research objective is to determine:

1. how variant-calling performance changes as benchmark scope expands,
2. which variant classes contribute most to missed variants,
3. which genomic regions show reduced recall,
4. how normalized record-level comparison differs from formal RTG vcfeval benchmarking,
5. and whether conclusions remain stable across progressively larger regional validation sets.

---

## Current Benchmark Design

| Benchmark | Scope |
|---|---|
| 5-region | Initial regional validation |
| 25-region | Expanded regional validation |
| 50-region | Primary expanded validation |

The benchmark uses:

```text
Sample: HG001
Alternate identifier: NA12878
Assembly: GRCh38
Chromosome: chr22
GIAB release: v4.2.1
