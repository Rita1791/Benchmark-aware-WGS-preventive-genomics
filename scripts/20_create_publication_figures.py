from pathlib import Path
import csv
from collections import Counter
import matplotlib.pyplot as plt

OUT = Path("results/publication_ready/figures")
OUT.mkdir(parents=True, exist_ok=True)

# ---------- Figure 1: benchmark scale performance ----------
benchmarks = ["5-region", "25-region", "50-region"]
recall = [96.40, 94.48, 95.25]
precision = [100.00, 100.00, 100.00]
f1 = [98.17, 97.16, 97.57]

x = range(len(benchmarks))
width = 0.25

plt.figure(figsize=(8, 5))
plt.bar([i - width for i in x], recall, width, label="Recall")
plt.bar(list(x), precision, width, label="Precision")
plt.bar([i + width for i in x], f1, width, label="F1")
plt.xticks(list(x), benchmarks)
plt.ylabel("Performance (%)")
plt.ylim(85, 102)
plt.title("Benchmark Scale Performance")
plt.legend()
plt.tight_layout()
plt.savefig(OUT / "figure_1_benchmark_scale_performance.png", dpi=300)
plt.close()

# ---------- Figure 2: bcftools vs RTG vcfeval ----------
methods = ["bcftools isec", "RTG vcfeval"]
precision2 = [100.00, 99.84]
recall2 = [95.25, 95.10]
f12 = [97.57, 97.41]

x = range(len(methods))
width = 0.25

plt.figure(figsize=(8, 5))
plt.bar([i - width for i in x], precision2, width, label="Precision")
plt.bar(list(x), recall2, width, label="Recall/Sensitivity")
plt.bar([i + width for i in x], f12, width, label="F1/F-measure")
plt.xticks(list(x), methods)
plt.ylabel("Performance (%)")
plt.ylim(90, 101)
plt.title("bcftools isec vs RTG vcfeval")
plt.legend()
plt.tight_layout()
plt.savefig(OUT / "figure_2_bcftools_vs_rtg_vcfeval.png", dpi=300)
plt.close()

# ---------- Figure 3: missed variant type distribution ----------
missed_file = Path("results/benchmark_valid_chr22_50_region/reports/missed_truth_variant_analysis.tsv")
type_counts = Counter()

with open(missed_file) as f:
    reader = csv.reader(f, delimiter="\t")
    header = next(reader)
    for row in reader:
        if len(row) > 5:
            type_counts[row[5]] += 1

labels = list(type_counts.keys())
values = [type_counts[k] for k in labels]

plt.figure(figsize=(7, 5))
plt.bar(labels, values)
plt.ylabel("Missed variant count")
plt.title("Missed Variant Type Distribution")
plt.tight_layout()
plt.savefig(OUT / "figure_3_missed_variant_type_distribution.png", dpi=300)
plt.close()

# ---------- Figure 4: lowest recall regions ----------
low_file = Path("results/benchmark_valid_chr22_50_region/reports/low_recall_region_summary.tsv")
regions = []
recalls = []

with open(low_file) as f:
    reader = csv.DictReader(f, delimiter="\t")
    for row in reader:
        regions.append(row["region_id"])
        recalls.append(float(row["recall_pct"]))

plt.figure(figsize=(10, 5))
plt.bar(regions, recalls)
plt.ylabel("Recall (%)")
plt.ylim(80, 100)
plt.title("Low-Recall chr22 Benchmark Regions")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()
plt.savefig(OUT / "figure_4_low_recall_regions.png", dpi=300)
plt.close()

# ---------- Figure 5: workflow overview as text figure ----------
plt.figure(figsize=(12, 4))
plt.axis("off")
workflow = (
    "GIAB HG001 / NA12878 BAM\\n"
    "↓\\n"
    "chr22 Region Selection\\n"
    "↓\\n"
    "Read Extraction + Variant Calling\\n"
    "↓\\n"
    "VCF Normalization\\n"
    "↓\\n"
    "bcftools isec + RTG vcfeval\\n"
    "↓\\n"
    "Missed Variant + Low-Recall + Discrepancy Analysis"
)
plt.text(0.5, 0.5, workflow, ha="center", va="center", fontsize=12)
plt.title("Benchmark Workflow Overview")
plt.tight_layout()
plt.savefig(OUT / "figure_5_workflow_overview.png", dpi=300)
plt.close()

print("Publication-ready figures created in:", OUT)
for path in sorted(OUT.glob("figure_*.png")):
    print(path)
