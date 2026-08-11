#!/usr/bin/env python3

"""
Generate publication-ready figures from compact repository result files.

Input files:
    results/benchmark_metrics.csv
    results/final_summary.csv
    results/variant_class_summary.csv

Optional input files:
    results/low_recall_regions.csv

Outputs:
    results/publication_ready/figures/
"""

from pathlib import Path
import csv

import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch


# ---------------------------------------------------------------------
# Paths
# ---------------------------------------------------------------------

RESULTS_DIR = Path("results")
OUT_DIR = RESULTS_DIR / "publication_ready" / "figures"

OUT_DIR.mkdir(parents=True, exist_ok=True)


# ---------------------------------------------------------------------
# Utility
# ---------------------------------------------------------------------

def read_csv(path: Path):
    """Read a CSV file and return a list of dictionaries."""
    if not path.exists():
        raise FileNotFoundError(f"Required input file not found: {path}")

    with path.open("r", newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def save_figure(path: Path):
    """Save a publication-quality figure."""
    plt.tight_layout()
    plt.savefig(
        path,
        dpi=300,
        bbox_inches="tight",
    )
    plt.close()


# ---------------------------------------------------------------------
# Figure 1 — Benchmark scale performance
# ---------------------------------------------------------------------

benchmark_rows = read_csv(
    RESULTS_DIR / "benchmark_metrics.csv"
)

benchmarks = [
    row["benchmark"]
    for row in benchmark_rows
]

recall = [
    float(row["recall_percent"])
    for row in benchmark_rows
]

precision = [
    float(row["precision_percent"])
    for row in benchmark_rows
]

f1 = [
    float(row["f1_percent"])
    for row in benchmark_rows
]

x = list(range(len(benchmarks)))
width = 0.24

plt.figure(figsize=(8, 5))

plt.bar(
    [i - width for i in x],
    recall,
    width,
    label="Recall",
)

plt.bar(
    x,
    precision,
    width,
    label="Precision",
)

plt.bar(
    [i + width for i in x],
    f1,
    width,
    label="F1",
)

plt.xticks(
    x,
    benchmarks,
)

plt.ylabel("Performance (%)")
plt.xlabel("Benchmark scope")
plt.ylim(85, 102)

plt.title(
    "Variant-calling performance across benchmark scales"
)

plt.legend(
    frameon=False
)

save_figure(
    OUT_DIR / "figure_1_benchmark_scale_performance.png"
)


# ---------------------------------------------------------------------
# Figure 2 — bcftools isec vs RTG vcfeval
# ---------------------------------------------------------------------

final_rows = read_csv(
    RESULTS_DIR / "final_summary.csv"
)

methods = []
precision_values = []
sensitivity_values = []
f_measure_values = []

for row in final_rows:

    methods.append(
        row["benchmark_method"]
    )

    precision_values.append(
        float(row["precision_percent"])
    )

    sensitivity_values.append(
        float(row["sensitivity_percent"])
    )

    f_measure_values.append(
        float(row["f_measure_percent"])
    )

x = list(range(len(methods)))
width = 0.24

plt.figure(figsize=(8, 5))

plt.bar(
    [i - width for i in x],
    precision_values,
    width,
    label="Precision",
)

plt.bar(
    x,
    sensitivity_values,
    width,
    label="Recall / Sensitivity",
)

plt.bar(
    [i + width for i in x],
    f_measure_values,
    width,
    label="F1 / F-measure",
)

plt.xticks(
    x,
    methods,
)

plt.ylabel("Performance (%)")
plt.xlabel("Benchmarking method")
plt.ylim(90, 101)

plt.title(
    "Comparison of normalized and formal benchmarking"
)

plt.legend(
    frameon=False
)

save_figure(
    OUT_DIR / "figure_2_bcftools_vs_rtg_vcfeval.png"
)


# ---------------------------------------------------------------------
# Figure 3 — Missed variant type distribution
# ---------------------------------------------------------------------

variant_rows = read_csv(
    RESULTS_DIR / "variant_class_summary.csv"
)

labels = []
values = []

for row in variant_rows:

    variant_class = row["variant_class"]

    if variant_class.lower() == "total":
        continue

    labels.append(
        variant_class
    )

    values.append(
        int(row["missed_count"])
    )

plt.figure(figsize=(7, 5))

plt.bar(
    labels,
    values,
)

plt.ylabel("Missed variant count")
plt.xlabel("Variant class")

plt.title(
    "Observed missed-variant composition"
)

save_figure(
    OUT_DIR / "figure_3_missed_variant_type_distribution.png"
)


# ---------------------------------------------------------------------
# Figure 4 — Low-recall regions
# ---------------------------------------------------------------------
#
# Requires:
#     results/low_recall_regions.csv
#
# Expected columns:
#     region_id
#     recall_percent
# ---------------------------------------------------------------------

low_recall_file = RESULTS_DIR / "low_recall_regions.csv"

if low_recall_file.exists():

    low_rows = read_csv(
        low_recall_file
    )

    regions = [
        row["region_id"]
        for row in low_rows
    ]

    recalls = [
        float(row["recall_percent"])
        for row in low_rows
    ]

    plt.figure(figsize=(10, 5))

    plt.bar(
        regions,
        recalls,
    )

    plt.ylabel("Recall (%)")
    plt.xlabel("Benchmark region")
    plt.ylim(80, 100)

    plt.axhline(
        92,
        linestyle="--",
        linewidth=1,
        label="92% threshold",
    )

    plt.title(
        "Low-recall chromosome 22 benchmark regions"
    )

    plt.xticks(
        rotation=45,
        ha="right",
    )

    plt.legend(
        frameon=False
    )

    save_figure(
        OUT_DIR / "figure_4_low_recall_regions.png"
    )

else:

    print(
        "INFO: results/low_recall_regions.csv not found. "
        "Figure 4 will be generated after the compact low-recall "
        "result file is added."
    )


# ---------------------------------------------------------------------
# Figure 5 — Workflow overview
# ---------------------------------------------------------------------

fig, ax = plt.subplots(
    figsize=(13, 5)
)

ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.axis("off")

steps = [
    (
        0.08,
        "GIAB HG001\n/ NA12878"
    ),
    (
        0.28,
        "GRCh38\nchr22 regions"
    ),
    (
        0.48,
        "WGS processing\n& variant calling"
    ),
    (
        0.68,
        "VCF normalization\n& benchmarking"
    ),
    (
        0.88,
        "Error analysis\n& validation"
    ),
]

for x_position, label in steps:

    box = FancyBboxPatch(
        (
            x_position - 0.075,
            0.40,
        ),
        0.15,
        0.20,
        boxstyle="round,pad=0.02",
        linewidth=1.2,
        fill=False,
    )

    ax.add_patch(box)

    ax.text(
        x_position,
        0.50,
        label,
        ha="center",
        va="center",
        fontsize=10,
    )


for i in range(len(steps) - 1):

    x_start = steps[i][0] + 0.075
    x_end = steps[i + 1][0] - 0.075

    arrow = FancyArrowPatch(
        (
            x_start,
            0.50,
        ),
        (
            x_end,
            0.50,
        ),
        arrowstyle="->",
        mutation_scale=15,
        linewidth=1.2,
    )

    ax.add_patch(arrow)


ax.set_title(
    "Benchmark-aware WGS variant-calling validation workflow",
    fontsize=13,
)

save_figure(
    OUT_DIR / "figure_5_workflow_overview.png"
)


# ---------------------------------------------------------------------
# Completion
# ---------------------------------------------------------------------

print()
print("Publication-ready figures generated in:")
print(OUT_DIR.resolve())

for path in sorted(OUT_DIR.glob("*.png")):
    print(f"  - {path.name}")
