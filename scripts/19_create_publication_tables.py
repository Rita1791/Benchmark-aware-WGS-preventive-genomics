#!/usr/bin/env python3

"""
Generate publication-ready tables from compact repository result files.

Input files:
    results/benchmark_metrics.csv
    results/final_summary.csv
    results/variant_class_summary.csv

Optional input files:
    results/low_recall_regions.csv
    results/discrepancy_regions.csv

Outputs:
    results/publication_ready/tables/
"""

from pathlib import Path
import csv
import sys


# ---------------------------------------------------------------------
# Paths
# ---------------------------------------------------------------------

RESULTS_DIR = Path("results")
OUT_DIR = RESULTS_DIR / "publication_ready" / "tables"

OUT_DIR.mkdir(parents=True, exist_ok=True)


# ---------------------------------------------------------------------
# Utility functions
# ---------------------------------------------------------------------

def read_csv(path: Path):
    """Read a CSV file and return a list of dictionaries."""
    if not path.exists():
        raise FileNotFoundError(f"Required input file not found: {path}")

    with path.open("r", newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def write_tsv(path: Path, headers, rows):
    """Write rows to a TSV file."""
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.writer(handle, delimiter="\t")
        writer.writerow(headers)
        writer.writerows(rows)


def write_markdown_table(path: Path, headers, rows, title):
    """Write a Markdown table."""
    with path.open("w", encoding="utf-8") as handle:
        handle.write(f"# {title}\n\n")

        handle.write("| " + " | ".join(headers) + " |\n")
        handle.write(
            "|"
            + "|".join("---:" if i > 0 else "---" for i in range(len(headers)))
            + "|\n"
        )

        for row in rows:
            handle.write("| " + " | ".join(map(str, row)) + " |\n")


# ---------------------------------------------------------------------
# Table 1 — Benchmark scale comparison
# ---------------------------------------------------------------------

benchmark_rows = read_csv(
    RESULTS_DIR / "benchmark_metrics.csv"
)

table_1_headers = [
    "Benchmark",
    "Truth variants",
    "Shared variants",
    "Missed truth",
    "Extra project",
    "Recall",
    "Precision",
    "F1",
]

table_1_rows = []

for row in benchmark_rows:
    table_1_rows.append(
        [
            row["benchmark"],
            row["truth_variants"],
            row["shared_variants"],
            row["truth_only_missed"],
            row["project_only_extra"],
            f'{row["recall_percent"]}%',
            f'{row["precision_percent"]}%',
            f'{row["f1_percent"]}%',
        ]
    )

write_tsv(
    OUT_DIR / "table_1_benchmark_scale_comparison.tsv",
    table_1_headers,
    table_1_rows,
)

write_markdown_table(
    OUT_DIR / "table_1_benchmark_scale_comparison.md",
    table_1_headers,
    table_1_rows,
    "Table 1. Benchmark Scale Comparison",
)


# ---------------------------------------------------------------------
# Table 2 — Formal RTG vcfeval result
# ---------------------------------------------------------------------

final_rows = read_csv(
    RESULTS_DIR / "final_summary.csv"
)

rtg_rows = [
    row
    for row in final_rows
    if row["benchmark_method"].lower() == "rtg_vcfeval"
]

if not rtg_rows:
    raise ValueError(
        "No RTG_vcfeval row found in results/final_summary.csv"
    )

rtg = rtg_rows[0]

table_2_headers = [
    "Benchmark",
    "True positives",
    "False positives",
    "False negatives",
    "Precision",
    "Sensitivity",
    "F-measure",
]

table_2_rows = [
    [
        rtg["benchmark_method"],
        rtg["true_positives"],
        rtg["false_positives"],
        rtg["false_negatives"],
        f'{rtg["precision_percent"]}%',
        f'{rtg["sensitivity_percent"]}%',
        f'{rtg["f_measure_percent"]}%',
    ]
]

write_tsv(
    OUT_DIR / "table_2_formal_rtg_vcfeval_result.tsv",
    table_2_headers,
    table_2_rows,
)

write_markdown_table(
    OUT_DIR / "table_2_formal_rtg_vcfeval_result.md",
    table_2_headers,
    table_2_rows,
    "Table 2. Formal RTG vcfeval Benchmark Result",
)


# ---------------------------------------------------------------------
# Table 3 — Missed variant summary
# ---------------------------------------------------------------------

variant_rows = read_csv(
    RESULTS_DIR / "variant_class_summary.csv"
)

table_3_headers = [
    "Variant class",
    "Missed variants",
]

table_3_rows = [
    [
        row["variant_class"],
        row["missed_count"],
    ]
    for row in variant_rows
]

total_missed = sum(
    int(row["missed_count"])
    for row in variant_rows
)

table_3_rows.append(
    [
        "Total",
        total_missed,
    ]
)

write_tsv(
    OUT_DIR / "table_3_missed_variant_summary.tsv",
    table_3_headers,
    table_3_rows,
)

write_markdown_table(
    OUT_DIR / "table_3_missed_variant_summary.md",
    table_3_headers,
    table_3_rows,
    "Table 3. Missed Variant Summary",
)


# ---------------------------------------------------------------------
# Table 4 — Low-recall regions
# ---------------------------------------------------------------------
#
# This table is generated only when the compact repository-level
# low-recall result file exists.
#
# Expected file:
#     results/low_recall_regions.csv
#
# ---------------------------------------------------------------------

low_recall_file = RESULTS_DIR / "low_recall_regions.csv"

if low_recall_file.exists():

    low_rows = read_csv(low_recall_file)

    required_columns = {
        "region_id",
        "coordinates",
        "truth_total",
        "project_total",
        "missed",
        "shared",
        "recall_percent",
        "precision_percent",
        "f1_percent",
    }

    missing = required_columns - set(low_rows[0].keys())

    if missing:
        raise ValueError(
            "results/low_recall_regions.csv is missing columns: "
            + ", ".join(sorted(missing))
        )

    table_4_headers = [
        "Region",
        "Coordinates",
        "Truth total",
        "Project total",
        "Missed",
        "Shared",
        "Recall",
        "Precision",
        "F1",
    ]

    table_4_rows = [
        [
            row["region_id"],
            row["coordinates"],
            row["truth_total"],
            row["project_total"],
            row["missed"],
            row["shared"],
            f'{row["recall_percent"]}%',
            f'{row["precision_percent"]}%',
            f'{row["f1_percent"]}%',
        ]
        for row in low_rows
    ]

    write_tsv(
        OUT_DIR / "table_4_low_recall_regions.tsv",
        table_4_headers,
        table_4_rows,
    )

    write_markdown_table(
        OUT_DIR / "table_4_low_recall_regions.md",
        table_4_headers,
        table_4_rows,
        "Table 4. Low-Recall Regions",
    )

else:
    print(
        "INFO: results/low_recall_regions.csv not found. "
        "Table 4 will be generated after the compact low-recall result "
        "file is added."
    )


# ---------------------------------------------------------------------
# Table 5 — bcftools isec vs RTG vcfeval discrepancy regions
# ---------------------------------------------------------------------
#
# This table is generated only when the compact discrepancy result
# file exists.
#
# Expected file:
#     results/discrepancy_regions.csv
#
# ---------------------------------------------------------------------

discrepancy_file = RESULTS_DIR / "discrepancy_regions.csv"

if discrepancy_file.exists():

    discrepancy_rows = read_csv(discrepancy_file)

    required_columns = {
        "region_id",
        "bcftools_shared",
        "rtg_tp",
        "tp_difference",
        "bcftools_fn",
        "rtg_fn",
        "fn_difference",
        "bcftools_fp",
        "rtg_fp",
        "fp_difference",
    }

    missing = required_columns - set(discrepancy_rows[0].keys())

    if missing:
        raise ValueError(
            "results/discrepancy_regions.csv is missing columns: "
            + ", ".join(sorted(missing))
        )

    table_5_headers = [
        "Region",
        "bcftools shared",
        "RTG TP",
        "TP difference",
        "bcftools FN",
        "RTG FN",
        "FN difference",
        "bcftools FP",
        "RTG FP",
        "FP difference",
    ]

    table_5_rows = [
        [
            row["region_id"],
            row["bcftools_shared"],
            row["rtg_tp"],
            row["tp_difference"],
            row["bcftools_fn"],
            row["rtg_fn"],
            row["fn_difference"],
            row["bcftools_fp"],
            row["rtg_fp"],
            row["fp_difference"],
        ]
        for row in discrepancy_rows
    ]

    write_tsv(
        OUT_DIR / "table_5_bcftools_vs_rtg_discrepancy_regions.tsv",
        table_5_headers,
        table_5_rows,
    )

    write_markdown_table(
        OUT_DIR / "table_5_bcftools_vs_rtg_discrepancy_regions.md",
        table_5_headers,
        table_5_rows,
        "Table 5. bcftools isec vs RTG vcfeval Discrepancy Regions",
    )

else:
    print(
        "INFO: results/discrepancy_regions.csv not found. "
        "Table 5 will be generated after the compact discrepancy result "
        "file is added."
    )


# ---------------------------------------------------------------------
# Completion
# ---------------------------------------------------------------------

print()
print("Publication-ready tables generated in:")
print(OUT_DIR.resolve())

for path in sorted(OUT_DIR.iterdir()):
    print(f"  - {path.name}")
