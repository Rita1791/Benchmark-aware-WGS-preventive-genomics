#!/usr/bin/env python3

"""
Aggregate RTG vcfeval results across the 50 chromosome 22 regions.

Input:
    results/formal_vcfeval_chr22_50_region/region_*/summary.txt

Outputs:
    results/formal_vcfeval_chr22_50_region/reports/
        vcfeval_50_region_summary.tsv
        vcfeval_50_region_formal_benchmark_report.md

    results/final_summary.csv
    results/low_recall_regions.csv
"""

from pathlib import Path
import csv


BASE = Path("results/formal_vcfeval_chr22_50_region")
REPORT_DIR = BASE / "reports"

REPORT_DIR.mkdir(parents=True, exist_ok=True)

SUMMARY_TSV = REPORT_DIR / "vcfeval_50_region_summary.tsv"
SUMMARY_MD = REPORT_DIR / "vcfeval_50_region_formal_benchmark_report.md"

FINAL_SUMMARY = Path("results/final_summary.csv")
LOW_RECALL = Path("results/low_recall_regions.csv")


# ------------------------------------------------------------
# Parse RTG summary
# ------------------------------------------------------------

def parse_summary(path):

    if not path.exists():
        raise FileNotFoundError(f"RTG summary not found: {path}")

    with path.open("r", encoding="utf-8") as handle:

        for line in handle:

            line = line.strip()

            if not line:
                continue

            parts = line.split()

            if len(parts) < 8:
                continue

            try:

                return {
                    "tp_baseline": int(parts[1]),
                    "tp_call": int(parts[2]),
                    "fp": int(parts[3]),
                    "fn": int(parts[4]),
                    "precision": float(parts[5]),
                    "sensitivity": float(parts[6]),
                    "f_measure": float(parts[7]),
                }

            except ValueError:
                continue

    raise ValueError(
        f"No valid RTG vcfeval result row found in {path}"
    )


# ------------------------------------------------------------
# Read 50 regions
# ------------------------------------------------------------

rows = []

for i in range(1, 51):

    region_id = f"region_{i}"

    summary_path = (
        BASE
        / region_id
        / "summary.txt"
    )

    result = parse_summary(summary_path)

    result["region_id"] = region_id

    rows.append(result)


if len(rows) != 50:
    raise ValueError(
        f"Expected 50 regions but found {len(rows)}."
    )


# ------------------------------------------------------------
# Aggregate counts
# ------------------------------------------------------------

total_tp_baseline = sum(
    row["tp_baseline"]
    for row in rows
)

total_tp_call = sum(
    row["tp_call"]
    for row in rows
)

total_fp = sum(
    row["fp"]
    for row in rows
)

total_fn = sum(
    row["fn"]
    for row in rows
)


# ------------------------------------------------------------
# Aggregate metrics
# ------------------------------------------------------------

precision = (
    total_tp_call / (total_tp_call + total_fp)
    if total_tp_call + total_fp
    else 0.0
)

sensitivity = (
    total_tp_baseline / (total_tp_baseline + total_fn)
    if total_tp_baseline + total_fn
    else 0.0
)

f_measure = (
    2 * precision * sensitivity / (precision + sensitivity)
    if precision + sensitivity
    else 0.0
)


# ------------------------------------------------------------
# Region-level summary
# ------------------------------------------------------------

with SUMMARY_TSV.open(
    "w",
    newline="",
    encoding="utf-8",
) as handle:

    fieldnames = [
        "region_id",
        "tp_baseline",
        "tp_call",
        "fp",
        "fn",
        "precision",
        "sensitivity",
        "f_measure",
    ]

    writer = csv.DictWriter(
        handle,
        fieldnames=fieldnames,
        delimiter="\t",
    )

    writer.writeheader()

    for row in rows:

        writer.writerow(
            {
                "region_id": row["region_id"],
                "tp_baseline": row["tp_baseline"],
                "tp_call": row["tp_call"],
                "fp": row["fp"],
                "fn": row["fn"],
                "precision": f"{row['precision']:.6f}",
                "sensitivity": f"{row['sensitivity']:.6f}",
                "f_measure": f"{row['f_measure']:.6f}",
            }
        )


# ------------------------------------------------------------
# Lowest-recall regions
# ------------------------------------------------------------

lowest = sorted(
    rows,
    key=lambda row: row["sensitivity"],
)[:10]


# ------------------------------------------------------------
# Create compact final_summary.csv
# ------------------------------------------------------------

final_rows = [
    {
        "benchmark_method": "RTG_vcfeval",
        "true_positives": total_tp_call,
        "false_positives": total_fp,
        "false_negatives": total_fn,
        "precision_percent": f"{precision * 100:.2f}",
        "sensitivity_percent": f"{sensitivity * 100:.2f}",
        "f_measure_percent": f"{f_measure * 100:.2f}",
    }
]

with FINAL_SUMMARY.open(
    "w",
    newline="",
    encoding="utf-8",
) as handle:

    fieldnames = [
        "benchmark_method",
        "true_positives",
        "false_positives",
        "false_negatives",
        "precision_percent",
        "sensitivity_percent",
        "f_measure_percent",
    ]

    writer = csv.DictWriter(
        handle,
        fieldnames=fieldnames,
    )

    writer.writeheader()
    writer.writerows(final_rows)


# ------------------------------------------------------------
# Create compact low-recall CSV
# ------------------------------------------------------------

with LOW_RECALL.open(
    "w",
    newline="",
    encoding="utf-8",
) as handle:

    fieldnames = [
        "region_id",
        "coordinates",
        "truth_total",
        "project_total",
        "missed",
        "shared",
        "recall_percent",
        "precision_percent",
        "f1_percent",
    ]

    writer = csv.DictWriter(
        handle,
        fieldnames=fieldnames,
    )

    writer.writeheader()

    for row in lowest:

        truth_total = (
            row["tp_baseline"]
            + row["fn"]
        )

        project_total = (
            row["tp_call"]
            + row["fp"]
        )

        writer.writerow(
            {
                "region_id": row["region_id"],
                "coordinates": "",
                "truth_total": truth_total,
                "project_total": project_total,
                "missed": row["fn"],
                "shared": row["tp_baseline"],
                "recall_percent": f"{row['sensitivity'] * 100:.2f}",
                "precision_percent": f"{row['precision'] * 100:.2f}",
                "f1_percent": f"{row['f_measure'] * 100:.2f}",
            }
        )


# ------------------------------------------------------------
# Markdown report
# ------------------------------------------------------------

with SUMMARY_MD.open(
    "w",
    encoding="utf-8",
) as handle:

    handle.write(
        "# Formal RTG vcfeval Benchmark Report — 50 chr22 Regions\n\n"
    )

    handle.write("## Goal\n\n")

    handle.write(
        "To aggregate RTG vcfeval results across 50 GIAB HG001 "
        "GRCh38 chromosome 22 benchmark regions.\n\n"
    )

    handle.write("## Combined vcfeval Metrics\n\n")

    handle.write(
        f"- Total true positives baseline: {total_tp_baseline}\n"
    )

    handle.write(
        f"- Total true positives call: {total_tp_call}\n"
    )

    handle.write(
        f"- Total false positives: {total_fp}\n"
    )

    handle.write(
        f"- Total false negatives: {total_fn}\n"
    )

    handle.write(
        f"- Precision: {precision * 100:.2f}%\n"
    )

    handle.write(
        f"- Sensitivity: {sensitivity * 100:.2f}%\n"
    )

    handle.write(
        f"- F-measure: {f_measure * 100:.2f}%\n\n"
    )

    handle.write("## Lowest 10 Regions by Sensitivity\n\n")

    handle.write(
        "| Region | TP Baseline | TP Call | FP | FN | "
        "Precision | Sensitivity | F-measure |\n"
    )

    handle.write(
        "|---|---:|---:|---:|---:|---:|---:|---:|\n"
    )

    for row in lowest:

        handle.write(
            f"| {row['region_id']} "
            f"| {row['tp_baseline']} "
            f"| {row['tp_call']} "
            f"| {row['fp']} "
            f"| {row['fn']} "
            f"| {row['precision'] * 100:.2f}% "
            f"| {row['sensitivity'] * 100:.2f}% "
            f"| {row['f_measure'] * 100:.2f}% |\n"
        )

    handle.write("\n## Interpretation\n\n")

    handle.write(
        "RTG vcfeval provides a formal benchmark comparison between "
        "the project callset and the GIAB HG001 truth set. Aggregate "
        "metrics are calculated from the per-region benchmark counts "
        "rather than by averaging region-level percentages.\n"
    )


print("Created:")
print(SUMMARY_TSV)
print(SUMMARY_MD)
print(FINAL_SUMMARY)
print(LOW_RECALL)

print()
print("Combined RTG vcfeval metrics:")
print(f"TP baseline: {total_tp_baseline}")
print(f"TP call: {total_tp_call}")
print(f"FP: {total_fp}")
print(f"FN: {total_fn}")
print(f"Precision: {precision * 100:.2f}%")
print(f"Sensitivity: {sensitivity * 100:.2f}%")
print(f"F-measure: {f_measure * 100:.2f}%")
