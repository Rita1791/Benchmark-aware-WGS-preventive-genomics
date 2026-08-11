#!/usr/bin/env python3

"""
Create benchmark-scale comparison results from the compact benchmark CSV.

Input:
    results/benchmark_metrics.csv

Output:
    results/final_comparison/benchmark_scale_comparison.tsv
    results/final_comparison/benchmark_scale_comparison.md
"""

from pathlib import Path
import csv


RESULTS_DIR = Path("results")
OUT_DIR = RESULTS_DIR / "final_comparison"
OUT_DIR.mkdir(parents=True, exist_ok=True)

INPUT = RESULTS_DIR / "benchmark_metrics.csv"

OUT_TSV = OUT_DIR / "benchmark_scale_comparison.tsv"
OUT_MD = OUT_DIR / "benchmark_scale_comparison.md"


def read_csv(path):
    if not path.exists():
        raise FileNotFoundError(f"Input file not found: {path}")

    with path.open("r", newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


rows = read_csv(INPUT)

if not rows:
    raise ValueError("benchmark_metrics.csv contains no data rows.")


# ------------------------------------------------------------
# Validate required columns
# ------------------------------------------------------------

required_columns = {
    "benchmark",
    "truth_variants",
    "shared_variants",
    "truth_only_missed",
    "project_only_extra",
    "recall_percent",
    "precision_percent",
    "f1_percent",
}

missing = required_columns - set(rows[0].keys())

if missing:
    raise ValueError(
        "benchmark_metrics.csv is missing columns: "
        + ", ".join(sorted(missing))
    )


# ------------------------------------------------------------
# Write TSV
# ------------------------------------------------------------

headers = [
    "benchmark",
    "truth_variants",
    "shared_variants",
    "truth_only_missed",
    "project_only_extra",
    "recall_percent",
    "precision_percent",
    "f1_percent",
]

with OUT_TSV.open("w", newline="", encoding="utf-8") as handle:

    writer = csv.DictWriter(
        handle,
        fieldnames=headers,
        delimiter="\t",
    )

    writer.writeheader()

    for row in rows:
        writer.writerow(
            {
                key: row[key]
                for key in headers
            }
        )


# ------------------------------------------------------------
# Write Markdown report
# ------------------------------------------------------------

with OUT_MD.open("w", encoding="utf-8") as handle:

    handle.write(
        "# Benchmark Scale Comparison — GIAB HG001 chr22 Regional Validation\n\n"
    )

    handle.write("## Goal\n\n")

    handle.write(
        "To compare benchmark performance across progressively expanded "
        "GIAB HG001 GRCh38 chromosome 22 regional validation scopes.\n\n"
    )

    handle.write("## Performance Comparison\n\n")

    handle.write(
        "| Benchmark | Truth Variants | Shared | Missed Truth | "
        "Extra Project | Recall | Precision | F1 |\n"
    )

    handle.write(
        "|---|---:|---:|---:|---:|---:|---:|---:|\n"
    )

    for row in rows:

        handle.write(
            f"| {row['benchmark']} "
            f"| {row['truth_variants']} "
            f"| {row['shared_variants']} "
            f"| {row['truth_only_missed']} "
            f"| {row['project_only_extra']} "
            f"| {row['recall_percent']}% "
            f"| {row['precision_percent']}% "
            f"| {row['f1_percent']}% |\n"
        )

    handle.write("\n## Interpretation\n\n")

    final_row = rows[-1]

    handle.write(
        f"The largest evaluated benchmark scope contained "
        f"{final_row['truth_variants']} truth variants and achieved "
        f"{final_row['recall_percent']}% recall, "
        f"{final_row['precision_percent']}% precision, and "
        f"{final_row['f1_percent']}% F1 in the normalized comparison.\n\n"
    )

    handle.write(
        "The benchmark configurations represent progressively expanded "
        "regional validation scopes and should not be interpreted as "
        "independent biological replicates.\n"
    )


print("Created:")
print(OUT_TSV)
print(OUT_MD)
