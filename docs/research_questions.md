# Research Questions

## Primary research question

How accurately and reproducibly does the WGS variant-calling workflow recover GIAB HG001 benchmark variants across progressively expanded GRCh38 chromosome 22 high-confidence regions?

## Secondary research questions

### RQ1 — Benchmark scale

Does variant-calling performance remain stable when benchmark evaluation is expanded from 5 to 25 and 50 chromosome 22 regions?

### RQ2 — Benchmarking methodology

How do normalized `bcftools isec` comparisons differ from formal RTG `vcfeval` benchmarking?

### RQ3 — Error structure

Which variant classes contribute most to missed benchmark variants?

### RQ4 — Difficult genomic regions

Are missed variants enriched in difficult or challenging genomic regions?

### RQ5 — Low-recall regions

Which benchmark regions exhibit reduced recall, and what variant characteristics contribute to their lower performance?

### RQ6 — Reproducibility

Can the analysis be represented as a transparent computational workflow in which the benchmark design, processing steps, comparison methods, and summary statistics are independently documented?

## Hypotheses

### H1

Overall benchmark performance will remain high as the number of evaluated regions increases.

### H2

Formal RTG `vcfeval` benchmarking will provide a more representation-aware assessment than direct normalized record comparison.

### H3

Missed variants will be enriched for indels relative to SNVs.

### H4

Difficult genomic regions will account for a substantial proportion of missed variants.

## Scope

These questions are evaluated within a regional chromosome 22 benchmark framework and are not intended to establish whole-genome clinical performance.
