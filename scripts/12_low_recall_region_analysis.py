#!/usr/bin/env python3

from pathlib import Path
import csv
from collections import defaultdict


BASE = Path("results/benchmark_valid_chr22_25_region")

REPORT_DIR = BASE / "reports"

SUMMARY_FILE = REPORT_DIR / "clean_multi_region_benchmark_summary.tsv"
MISSED_FILE = REPORT_DIR / "missed_truth_variant_analysis.tsv"

LOW_SUMMARY_OUT = REPORT_DIR / "low_recall_region_summary.tsv"
LOW_MISSED_OUT = REPORT_DIR / "low_recall_missed_variants.tsv"
LOW_REPORT_OUT = REPORT_DIR / "low_recall_region_interpretation.md"

RECALL_THRESHOLD = 92.0


with SUMMARY_FILE.open() as handle:

    summary_rows = list(
        csv.DictReader(handle, delimiter="\t")
    )


low_summary_rows = [
    row
    for row in summary_rows
    if float(row["recall_pct"]) < RECALL_THRESHOLD
]

low_regions = {
    row["region_id"]
    for row in low_summary_rows
}


with MISSED_FILE.open() as handle:

    missed_rows = [
        row
        for row in csv.DictReader(handle, delimiter="\t")
        if row["region_id"] in low_regions
    ]


# ------------------------------------------------------------
# Write low-recall summary
# ------------------------------------------------------------

summary_fields = list(summary_rows[0].keys())

with LOW_SUMMARY_OUT.open("w", newline="") as handle:

    writer = csv.DictWriter(
        handle,
        fieldnames=summary_fields,
        delimiter="\t",
    )

    writer.writeheader()
    writer.writerows(low_summary_rows)


# ------------------------------------------------------------
# Write missed variants
# ------------------------------------------------------------

missed_fields = list(
    missed_rows[0].keys()
) if missed_rows else [
    "region_id",
    "chrom",
    "pos",
    "ref",
    "alt",
    "variant_type",
    "qual",
    "filter",
    "difficultregion",
    "platforms",
    "datasets",
]

with LOW_MISSED_OUT.open("w", newline="") as handle:

    writer = csv.DictWriter(
        handle,
        fieldnames=missed_fields,
        delimiter="\t",
    )

    writer.writeheader()
    writer.writerows(missed_rows)


# ------------------------------------------------------------
# Error classification
# ------------------------------------------------------------

type_by_region = defaultdict(
    lambda: defaultdict(int)
)

difficult_by_region = defaultdict(int)
total_by_region = defaultdict(int)

overall_type_counts = defaultdict(int)
overall_difficult = 0


for row in missed_rows:

    rid = row["region_id"]
    vtype = row["variant_type"]

    type_by_region[rid][vtype] += 1
    total_by_region[rid] += 1

    overall_type_counts[vtype] += 1

    if row["difficultregion"]:
        difficult_by_region[rid] += 1
        overall_difficult += 1


# ------------------------------------------------------------
# Report
# ------------------------------------------------------------

with LOW_REPORT_OUT.open("w") as handle:

    handle.write(
        "# Low-Recall Region Error Analysis — 25-Region chr22 Benchmark\n\n"
    )

    handle.write(
        f"Recall threshold: < {RECALL_THRESHOLD:.1f}%\n\n"
    )

    handle.write(
        f"Number of low-recall regions: {len(low_summary_rows)}\n\n"
    )

    handle.write("## Low-Recall Regions\n\n")

    handle.write(
        "| Region | Coordinates | Truth | Project | "
        "Missed | Shared | Recall | Precision | F1 |\n"
    )

    handle.write(
        "|---|---|---:|---:|---:|---:|---:|---:|---:|\n"
    )

    for row in low_summary_rows:

        handle.write(
            f"| {row['region_id']} "
            f"| {row['region']} "
            f"| {row['normalized_truth_total']} "
            f"| {row['normalized_project_total']} "
            f"| {row['truth_only_missed']} "
            f"| {row['shared']} "
            f"| {row['recall_pct']}% "
            f"| {row['precision_pct']}% "
            f"| {row['f1_pct']}% |\n"
        )

    handle.write(
        "\n## Missed Variant Types\n\n"
    )

    if overall_type_counts:

        for variant_type, count in sorted(
            overall_type_counts.items()
        ):

            handle.write(
                f"- {variant_type}: {count}\n"
            )

    else:

        handle.write(
            "No missed variants were associated with regions "
            "below the recall threshold.\n"
        )

    handle.write(
        f"\nTotal missed variants: {len(missed_rows)}\n"
    )

    handle.write(
        f"Difficult-region annotated: {overall_difficult}\n\n"
    )

    handle.write(
        "## Region-wise Error Pattern\n\n"
    )

    handle.write(
        "| Region | Missed | Difficult | Variant Types |\n"
    )

    handle.write(
        "|---|---:|---:|---|\n"
    )

    for rid in sorted(
        low_regions,
        key=lambda value: int(value.split("_")[1]),
    ):

        type_text = ", ".join(
            f"{key}: {value}"
            for key, value in sorted(
                type_by_region[rid].items()
            )
        )

        handle.write(
            f"| {rid} "
            f"| {total_by_region[rid]} "
            f"| {difficult_by_region[rid]} "
            f"| {type_text or 'None'} |\n"
        )

    handle.write(
        "\n## Interpretation\n\n"
    )

    handle.write(
        "Low-recall regions are treated as targeted error-analysis "
        "units. Their missed variants are characterized by variant "
        "type and available GIAB difficult-region annotations. "
        "This analysis does not by itself establish a causal "
        "mechanism for each missed call.\n"
    )


print("[DONE]")
print(f"Low-recall regions: {len(low_summary_rows)}")
print(f"Missed variants: {len(missed_rows)}")
print(f"Report: {LOW_REPORT_OUT}")
