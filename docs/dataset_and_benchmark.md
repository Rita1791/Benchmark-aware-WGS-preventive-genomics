# Dataset and Benchmark

## Primary sample

**Sample:** HG001 / NA12878

HG001 is a Genome in a Bottle benchmark reference sample used for evaluation of human genome variant-calling workflows.

## Reference genome

**Reference build:** GRCh38

The reference genome used by the analysis should be obtained independently and stored locally.

Reference genome files and indexes are not included in this repository.

## Benchmark resource

The benchmark uses GIAB truth variants and high-confidence benchmark regions corresponding to HG001 and GRCh38.

## Genomic scope

The current study focuses on:

**Chromosome 22**

The analysis uses selected high-confidence benchmark regions rather than the complete genome.

## Benchmark scales

Three regional configurations were evaluated:

- 5 regions
- 25 regions
- 50 regions

The final 50-region evaluation is the principal regional benchmark.

## Data categories

| Data/resource | Repository | Local analysis |
|---|---|---|
| Raw FASTQ | No | Yes |
| SRA/public sequencing data | No | Yes |
| BAM/BAI | No | Yes |
| GRCh38 FASTA | No | Yes |
| GRCh38 indexes | No | Yes |
| GIAB truth VCF | No | Yes |
| GIAB confidence regions | No | Yes |
| Compact summary tables | Yes | Yes |
| Analysis scripts | Yes | Yes |

## Why large data are excluded

Large sequencing and reference files are excluded to:

1. keep the repository lightweight,
2. avoid duplicating public datasets,
3. prevent GitHub file-size limitations,
4. separate input data from analysis provenance.

The repository therefore documents how the datasets are used rather than storing complete raw resources.

## Benchmark evaluation methods

Two complementary approaches were used.

### Normalized `bcftools isec`

Used for direct comparison of normalized project and truth VCF representations.

### RTG `vcfeval`

Used as the primary formal benchmark for the final 50-region evaluation.

## Final benchmark result

The formal RTG benchmark produced:

- TP: 2,465
- FP: 4
- FN: 127
- Precision: 99.84%
- Sensitivity: 95.10%
- F-measure: 97.41%

## Data provenance

The final repository should record the exact source URL, accession, release/version, and checksum for each externally obtained dataset or reference resource used in the final analysis.
