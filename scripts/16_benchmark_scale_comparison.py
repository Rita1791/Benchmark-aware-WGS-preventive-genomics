from pathlib import Path

outdir = Path("results/final_comparison")
outdir.mkdir(parents=True, exist_ok=True)

tsv = outdir / "benchmark_scale_comparison.tsv"
md = outdir / "benchmark_scale_comparison.md"

rows = [
    {
        "benchmark": "5-region chr22",
        "truth_total": 444,
        "project_total": 428,
        "shared": 428,
        "truth_only": 16,
        "project_only": 0,
        "recall": 96.40,
        "precision": 100.00,
        "f1": 98.17,
        "missed_deletion": 10,
        "missed_insertion": 6,
        "missed_snv": 0,
        "difficult_missed": 8,
    },
    {
        "benchmark": "25-region chr22",
        "truth_total": 1504,
        "project_total": 1421,
        "shared": 1421,
        "truth_only": 83,
        "project_only": 0,
        "recall": 94.48,
        "precision": 100.00,
        "f1": 97.16,
        "missed_deletion": 45,
        "missed_insertion": 37,
        "missed_snv": 1,
        "difficult_missed": 50,
    },
    {
        "benchmark": "50-region chr22",
        "truth_total": 2592,
        "project_total": 2469,
        "shared": 2469,
        "truth_only": 123,
        "project_only": 0,
        "recall": 95.25,
        "precision": 100.00,
        "f1": 97.57,
        "missed_deletion": 66,
        "missed_insertion": 56,
        "missed_snv": 1,
        "difficult_missed": 77,
    },
]

headers = [
    "benchmark", "truth_total", "project_total", "shared",
    "truth_only", "project_only", "recall", "precision", "f1",
    "missed_deletion", "missed_insertion", "missed_snv", "difficult_missed"
]

with open(tsv, "w") as f:
    f.write("\t".join(headers) + "\n")
    for r in rows:
        f.write("\t".join(str(r[h]) for h in headers) + "\n")

with open(md, "w") as f:
    f.write("# Benchmark Scale Comparison — GIAB HG001 chr22 Regional Validation\n\n")

    f.write("## Goal\n")
    f.write("To compare benchmark performance across 5-region, 25-region, and 50-region GIAB HG001 chr22 validation experiments.\n\n")

    f.write("## Performance Comparison\n\n")
    f.write("| Benchmark | Truth Variants | Project Variants | Shared | Missed Truth | Extra Project | Recall | Precision | F1 |\n")
    f.write("|---|---:|---:|---:|---:|---:|---:|---:|---:|\n")
    for r in rows:
        f.write(
            f"| {r['benchmark']} | {r['truth_total']} | {r['project_total']} | {r['shared']} | "
            f"{r['truth_only']} | {r['project_only']} | {r['recall']:.2f}% | "
            f"{r['precision']:.2f}% | {r['f1']:.2f}% |\n"
        )

    f.write("\n## Missed Variant Pattern\n\n")
    f.write("| Benchmark | Deletions | Insertions | SNVs | Difficult-Region Missed |\n")
    f.write("|---|---:|---:|---:|---:|\n")
    for r in rows:
        f.write(
            f"| {r['benchmark']} | {r['missed_deletion']} | {r['missed_insertion']} | "
            f"{r['missed_snv']} | {r['difficult_missed']} |\n"
        )

    f.write("\n## Scientific Interpretation\n")
    f.write(
        "The benchmark remained stable as the validation expanded from 5 to 25 and then 50 chr22 regions. "
        "The 50-region benchmark achieved 95.25% recall, 100.00% precision, and 97.57% F1 across 2592 normalized truth variants. "
        "The absence of project-only extra variants across all scales indicates strong precision after normalization. "
        "Missed variants were consistently dominated by insertions and deletions, with very few missed SNVs, suggesting that remaining limitations are mainly related to indel detection in difficult genomic contexts.\n\n"
    )

    f.write("## Conclusion\n")
    f.write(
        "The 50-region result provides the strongest current evidence for regional benchmark validity. "
        "This result is more robust than the 5-region and 25-region analyses because it covers more truth variants and more genomic contexts while maintaining high recall and perfect precision.\n"
    )

print("Created:")
print(tsv)
print(md)
print(md.read_text())
