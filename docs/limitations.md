# Limitations

## 1. Regional rather than whole-genome evaluation

The current analysis evaluates selected chromosome 22 high-confidence regions rather than the complete human genome.

Therefore, the results cannot be generalized directly to whole-genome performance.

## 2. Limited genomic representation

Chromosome 22 contains important genomic contexts but does not represent the full diversity of sequence complexity across all human chromosomes.

## 3. Indel sensitivity

The major observed limitation was missed indel detection.

Of the 123 truth-only variants in the normalized 50-region comparison, 122 were indels.

## 4. Difficult genomic regions

A substantial fraction of missed variants occurred in difficult genomic contexts.

Seventy-seven missed variants had difficult-region annotations.

## 5. Benchmark dependence

Benchmark performance depends on the selected truth set, confident regions, reference genome, normalization procedure, and benchmarking methodology.

## 6. Methodological comparison

`bcftools isec` and RTG `vcfeval` are not interchangeable evaluation methods.

The normalized comparison is useful for direct record-level comparison, whereas RTG `vcfeval` provides a more representation-aware benchmark.

## 7. Clinical interpretation

The workflow is a research validation framework.

It has not been established as a clinical diagnostic pipeline and should not be interpreted as evidence of clinical validity, clinical sensitivity, or clinical specificity.

## 8. Future validation

Future work should include:

- additional chromosomes,
- whole-genome GIAB benchmarking,
- additional benchmark samples,
- independent sequencing datasets,
- alternative variant callers,
- improved indel detection,
- more detailed difficult-region analysis.

## 9. Reproducibility limitation

The public repository does not contain the complete raw sequencing and reference datasets.

Instead, it provides computational code, documentation, and compact results required to understand and reproduce the analytical workflow using independently obtained public resources.
