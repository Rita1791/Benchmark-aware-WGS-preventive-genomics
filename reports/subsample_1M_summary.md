# Subsampled FASTQ Summary

## Project
Nainfit WGS/NGS Research Pipeline

## Purpose
A 1-million-read-pair subset was created from trimmed paired-end FASTQ files to enable controlled downstream alignment and variant-calling tests under limited local compute resources.

## Input Files
- data/real_trimmed_fastq/SRR4420293_1.trimmed.fastq.gz
- data/real_trimmed_fastq/SRR4420293_2.trimmed.fastq.gz

## Output Files
- data/subsampled_fastq/SRR4420293_1.subsample_1M.fastq.gz
- data/subsampled_fastq/SRR4420293_2.subsample_1M.fastq.gz

## Method
A Python gzip-based streaming script copied the first 1000000 complete FASTQ records from both R1 and R2. Each FASTQ record contains 4 lines.

## Validation
- Expected lines per file: 4000000
- R1 output lines: 4000000
- R2 output lines: 4000000
- R1 and R2 read-pair counts match.

## Scientific Reasoning
Subsampling allows controlled testing of pipeline modules before scaling to larger WGS datasets. It reduces computational burden, improves debugging, and preserves paired-end synchronization.

## Limitation
This is a deterministic first-N-read subset, not a random subsample. For formal benchmarking, random subsampling with seqtk or equivalent tools should be used later.

## Next Step
Use the 1M read-pair subset for full-reference alignment testing.
