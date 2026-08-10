# Day 6 — Benchmark-Valid chr22 Regional Workflow

## Goal:
To move from benchmark-awareness to a benchmark-valid small regional workflow using GIAB HG001 / NA12878 GRCh38 truth resources.

## Starting Point:
The previous chr22 VCF was generated from randomly sampled WGS reads aligned only to chr22. It was useful as a technical proof-of-pipeline but showed very low overlap with GIAB truth.

## Problem:
The current VCF is not suitable for formal benchmarking because the experimental design is weak.

## Today’s Plan:
1. Select a small chr22 high-confidence region from the GIAB BED file.
2. Extract GIAB truth variants for that region.
3. Test access to GIAB-aligned BAM resources.
4. Decide whether a local benchmark-compatible regional variant-calling test is feasible.

## Scientific Reason:
Benchmarking must compare calls and truth variants in the same reference build, same chromosome naming, and same confident genomic region.

## Expected Output:
A small chr22 region, truth VCF for that region, and a decision on whether we can perform regional benchmarking locally.
