# Daily Research Log — 2026-06-08

## Research Goal for Today
To prepare the human WGS mini-pipeline for benchmark-compatible validation using GIAB HG001 / NA12878 truth-set resources.

## Starting Context
The project has completed a technical human WGS mini-pipeline using SRR2052337:

SRA → FASTQ → QC → chr22 alignment → BAM → raw VCF → filtered VCF

The 100k and 1M tests showed that the pipeline is technically functional and scalable. However, mapping behavior remained nearly identical after scaling from 100k to 1M, confirming that the limitation is structural: random WGS reads were aligned only to a chromosome 22 reference.

## Scientific Problem
The current VCFs are not suitable for biological or clinical interpretation because the reference design is incomplete.

## Today’s Benchmarking Direction
Use GIAB HG001 / NA12878 benchmark truth-set resources to prepare a scientifically stronger validation framework.

## Why This Matters Scientifically
GIAB truth VCF and high-confidence BED files allow called variants to be compared against known benchmark variants in confident regions.

## Why This Matters for Swiss PhD-Level Research
A PhD-level genomics workflow must not stop at generating a VCF. It must validate variant calls against benchmark truth sets and clearly define regions where performance can be measured.

## Planned Work
1. Create GIAB truth-set resource folders.
2. Download HG001 GRCh38 benchmark VCF and BED.
3. Inspect truth-set files.
4. Check chromosome naming and reference-build compatibility.
5. Compare our pipeline VCF chromosome naming against GIAB truth naming.
6. Decide whether current chr22 outputs can be used for benchmarking or whether reference redesign is required.

## Expected Output
A benchmark-readiness report explaining whether current outputs are compatible with GIAB truth-set benchmarking.

## Interpretation
Pending.


---

# Corrected isec Record-Level Interpretation

## Step Performed
Recounted bcftools isec output files using grep -v "^#" to exclude VCF header lines.

## Corrected Counts
- GIAB-only variants: 46,368
- Project-only variants: 11,138
- Shared variants: 94

## Total Input Counts
- GIAB chr22 confident truth variants: 46,462
- Project filtered confident-region variants: 11,232

## Preliminary Interpretation
Only 94 variants were exactly shared between the project VCF and the GIAB truth VCF.

Approximate preliminary recall:
- 94 / 46,462 = ~0.20%

Approximate preliminary precision:
- 94 / 11,232 = ~0.84%

## Scientific Conclusion
The current pipeline output is not suitable for formal benchmark performance claims. The low overlap confirms that the chr22-only alignment strategy using randomly sampled whole-genome reads is structurally weak.

## PhD-Level Significance
This step demonstrates benchmark-readiness thinking. The project has moved beyond simply generating a VCF and has begun evaluating whether the VCF can be compared against truth-set resources.

## Next Step

Redesign the workflow toward biological validity before formal benchmarking.
