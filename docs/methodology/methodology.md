# Methodology

## 1. Study framework

This study evaluates a reproducible whole-genome sequencing (WGS) variant-calling workflow using Genome in a Bottle (GIAB) HG001/NA12878 benchmark material and the GRCh38 reference genome.

The current public analysis focuses on selected high-confidence regions on chromosome 22 rather than the complete genome.

## 2. Benchmark material

The primary benchmark sample is GIAB HG001, also known as NA12878.

The analysis uses:

- HG001 sequencing data
- GRCh38 reference sequence
- GIAB truth variants
- GIAB high-confidence benchmark regions

Large reference, sequencing, alignment, and benchmark files are excluded from the public repository because of their size. The repository documents their provenance and computational use instead.

## 3. Regional benchmark design

Three progressively larger chromosome 22 benchmark configurations were evaluated:

- 5 regions
- 25 regions
- 50 regions

The 50-region evaluation is the principal regional benchmark because it contains the largest number of evaluated benchmark variants among the configurations reported here.

## 4. WGS processing workflow

The computational workflow comprises the following major stages:

1. sequencing-data quality control,
2. adapter and quality trimming,
3. read alignment to GRCh38,
4. alignment processing and indexing,
5. variant calling,
6. VCF normalization,
7. benchmark comparison,
8. error and regional analysis.

The public pipeline scripts should document the computational logic used by the study without embedding machine-specific paths or large input files.

## 5. Alignment

Sequencing reads are aligned against the GRCh38 reference genome.

Alignment files are sorted and indexed before downstream variant calling and evaluation.

The final public pipeline must use the same alignment software, parameters, reference build, and read-group conventions used to generate the reported results.

## 6. Variant calling

Variant calling is performed using the project WGS variant-calling workflow.

The exact final caller and command-line parameters must correspond to the analysis that generated the reported benchmark results.

No software parameter is claimed here unless it is supported by the executed project workflow.

## 7. VCF normalization

Truth and project VCF representations are normalized before direct record-level comparison.

This reduces representation differences, particularly for indels, before `bcftools isec` evaluation.

## 8. Normalized comparison

Normalized truth and project callsets are compared using `bcftools isec`.

The comparison tracks:

- shared variants,
- truth-only variants,
- project-only variants.

For the normalized comparison:

$$
Recall = \frac{TP}{TP + FN}
$$

$$
Precision = \frac{TP}{TP + FP}
$$

$$
F1 = 2 \times \frac{Precision \times Recall}{Precision + Recall}
$$

## 9. Formal benchmarking

RTG `vcfeval` is used as the independent formal benchmarking method for the final 50-region evaluation.

The resulting true-positive, false-positive, and false-negative counts are used to calculate precision, sensitivity, and F-measure.

## 10. Benchmark-method comparison

Results from normalized `bcftools isec` comparison are compared with RTG `vcfeval` to identify discrepancies caused by differences in variant representation and benchmarking methodology.

Four regions were reported as showing discrepancies between the approaches:

- region_14
- region_20
- region_30
- region_40

## 11. Missed-variant analysis

Truth-only variants from the normalized 50-region comparison are classified by variant type.

The reported missed variants comprise:

- deletions,
- insertions,
- SNVs.

## 12. Difficult-region analysis

Missed variants are examined for overlap with difficult-region annotations to determine whether challenging genomic contexts contribute to reduced sensitivity.

## 13. Low-recall analysis

Regions with recall below the project-defined threshold of 92% are evaluated separately.

Their missed-variant composition and difficult-region annotations are summarized.

## 14. Reproducibility principle

The repository separates computational provenance from large input data.

Publicly version-controlled material should include:

- pipeline scripts,
- analysis scripts,
- configuration,
- documentation,
- compact result tables,
- figure-generation code,
- manuscript material.

Raw FASTQ files, BAM/CRAM files, large VCF/BCF files, reference genomes, indexes, and large intermediate outputs remain outside the public repository.
