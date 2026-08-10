# Daily Research Log — 2026-06-04

## Research Goal for Today
To verify the biological and technical metadata of SRR4420293 before performing full-reference alignment.

## Why This Step Was Needed Scientifically
Reference genome selection depends on dataset metadata. If the organism, sequencing strategy, or library type is unknown, alignment to a human reference may be scientifically invalid.

## Why This Step Matters for Swiss PhD-Level Research
A high-quality computational genomics pipeline must not assume metadata. Swiss PhD-level work requires dataset provenance, organism confirmation, sequencing strategy verification, and correct reference selection before variant discovery.

## Starting Status
Completed before today:
- Raw FASTQ downloaded
- FastQC completed
- MultiQC completed
- fastp trimming completed
- chr22 technical alignment test completed
- 1M paired-end FASTQ subsample created and validated

## Today’s Tasks
- Confirm project directory
- Confirm previous output files
- Check compute environment
- Identify SRR4420293 metadata
- Decide correct reference genome strategy

## Commands Run
To be filled during the session.

## Key Result
Pending.

## Interpretation
Pending.

## Next Step
Pending.

---

# Metadata Retrieval Attempt

## Step Performed
Used NCBI E-utilities through Python to retrieve metadata for SRR4420293.

## Why This Step Was Needed Scientifically
The correct reference genome cannot be selected until the organism and sequencing strategy are confirmed.

## Why This Matters for Swiss PhD-Level Research
Dataset provenance and metadata verification are required for reproducible computational genomics. Alignment and variant calling are invalid if the dataset is processed against the wrong reference genome.

## Output Files Generated
- reports/dataset_metadata/SRR4420293_efetch.xml
- reports/dataset_metadata/SRR4420293_metadata_extracted.txt

## Interpretation
Pending review of extracted metadata.

## Next Step
Use the extracted metadata to decide the correct reference genome and downstream pipeline strategy.
