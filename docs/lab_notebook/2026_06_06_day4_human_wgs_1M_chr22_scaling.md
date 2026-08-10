# Daily Research Log — 2026-06-06

## Research Goal for Today
To scale the verified human WGS mini-pipeline from a 100k paired-end subset to a 1M paired-end subset and compare QC, alignment, and variant-calling behavior.

## Starting Context
The project has successfully completed a technical human WGS mini-pipeline using GIAB/NIST HG001 NA12878 run SRR2052337:

SRA → FASTQ → QC → chr22 alignment → BAM → raw VCF → filtered VCF

The 100k subset produced:
- Raw VCF variants: 27,574
- Filtered VCF variants: 1,138
- Primary mapping rate to chr22: 32.20%

## Scientific Limitation from Previous Step
The 100k reads were randomly sampled from whole-genome data and aligned only to chr22. Therefore, the VCF was a technical proof-of-pipeline, not a biological or clinical callset.

## Today’s Scientific Question
Does increasing the controlled read subset from 100k paired-end reads to 1M paired-end reads improve alignment stability, coverage, and variant-calling behavior?

## Why This Matters Scientifically
Scaling the input subset allows assessment of whether observed mapping/variant-calling patterns are due to low read count, incomplete reference design, or both.

## Why This Matters for Swiss PhD-Level Research
A PhD-level genomics workflow must not only run tools, but compare pipeline behavior across controlled experimental conditions and document limitations clearly.

## Planned Work
1. Extract 1M paired-end reads from SRR2052337.
2. Validate FASTQ line counts.
3. Run FastQC and MultiQC.
4. Align to GRCh38 chr22.
5. Inspect BAM statistics.
6. Perform variant calling.
7. Filter VCF.
8. Compare 100k versus 1M results.

## Expected Output
A documented comparison between the 100k and 1M human WGS chr22 tests.

## Interpretation
Pending.


---

# 1M Human WGS QC Result

## FASTQ Extraction
A 1M paired-end read subset was extracted from SRR2052337.

## Output FASTQ Files
- data/human_wgs_fastq_1M/SRR2052337_1.fastq.gz
- data/human_wgs_fastq_1M/SRR2052337_2.fastq.gz

## Validation
- R1 line count: 4,000,000
- R2 line count: 4,000,000
- Interpretation: 1,000,000 reads per mate file

## MultiQC Summary
### R1
- Total sequences: 1,000,000
- Total bases: 148 Mbp
- Average read length: 148 bp
- GC content: 39%
- Duplicate percentage: 0.8348%
- FastQC failed modules: 0%

### R2
- Total sequences: 1,000,000
- Total bases: 148 Mbp
- Average read length: 148 bp
- GC content: 39%
- Duplicate percentage: 0.7746%
- FastQC failed modules: 0%

## FastQC Interpretation
Most modules passed, including per-base sequence quality, adapter content, and overrepresented sequences.

Only warning:
- per-sequence GC content

## Scientific Decision
No trimming was required before alignment.

## Next Step
Proceed to controlled chr22 alignment using bwa-mem2 and samtools.


---

# 1M chr22 Alignment Result

## Step Performed
Aligned the 1M paired-end human WGS subset from SRR2052337 to the GRCh38 chromosome 22 reference using bwa-mem2 and samtools.

## Output Files
- results/human_wgs_alignment_1M_chr22/SRR2052337_1M_chr22.sorted.bam
- results/human_wgs_alignment_1M_chr22/SRR2052337_1M_chr22.sorted.bam.bai
- results/human_wgs_alignment_1M_chr22/SRR2052337_1M_chr22.flagstat.txt
- results/human_wgs_alignment_1M_chr22/SRR2052337_1M_chr22.samtools_stats.txt
- results/human_wgs_alignment_1M_chr22/SRR2052337_1M_chr22.idxstats.txt

## Key Alignment Results
- Primary reads: 2,000,000
- Supplementary alignments: 75,676
- Primary mapped reads: 643,895
- Total mapped records: 719,571
- Primary mapping rate: 32.19%
- Properly paired reads: 259,456
- Properly paired rate: 12.97%
- Singletons: 185,205
- MQ0 reads: 230,599
- Error rate: approximately 6.655%

## Comparison With 100k Test
The 100k test had a primary mapping rate of 32.20%, while the 1M test had a primary mapping rate of 32.19%.

The mapping behavior remained nearly identical after scaling from 100k to 1M reads.

## Scientific Interpretation
Increasing read count by 10x did not improve the chr22-only alignment behavior. This confirms that the main limitation is not insufficient input reads, but the incomplete reference strategy: random whole-genome reads are being aligned only to chromosome 22.

## PhD-Level Significance
This is a controlled scaling experiment. It shows that pipeline behavior was reproducible across input sizes and that the limitation is structural rather than stochastic.

## Next Step
Perform 1M variant calling and compare raw and filtered variant counts with the 100k test.


---

# 1M Variant Calling and Filtering Result

## Step Performed
Performed variant calling and filtering on the 1M chr22 BAM using bcftools.

## Raw VCF
- results/human_wgs_variant_calling_1M_chr22/SRR2052337_1M_chr22.raw.vcf.gz

## Raw Variant Count
116,665

## Filtered VCF
- results/human_wgs_variant_calling_1M_chr22/SRR2052337_1M_chr22.filtered_QUAL30_DP5_MQ30.vcf.gz

## Filter Criteria
- QUAL >= 30
- DP >= 5
- MQ >= 30

## Filtered Variant Count
19,801

## Comparison With 100k Test
- 100k raw variants: 27,574
- 100k filtered variants: 1,138
- 1M raw variants: 116,665
- 1M filtered variants: 19,801

## Scientific Interpretation
The 1M test successfully scaled the technical pipeline and produced raw and filtered VCF files. However, the primary mapping rate and error rate remained nearly identical to the 100k test, confirming that the main limitation is the chr22-only reference design, not low read count.

## PhD-Level Significance
This is a controlled scaling experiment. It demonstrates that the workflow is reproducible at different input sizes and that limitations are being identified experimentally rather than assumed.

## Conclusion
The pipeline is technically functional and scalable from 100k to 1M reads. The next research step must improve biological validity through full-reference alignment, region-specific extraction, or GIAB benchmark truth-set comparison.
