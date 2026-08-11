from pathlib import Path

import yaml


REPO_ROOT = Path(__file__).resolve().parents[1]
CONFIG_FILE = REPO_ROOT / "config" / "benchmark.yaml"


def load_config():
    with CONFIG_FILE.open() as handle:
        return yaml.safe_load(handle)


def test_benchmark_sample():
    config = load_config()

    assert config["benchmark"]["sample"] == "HG001"


def test_reference_configuration():
    config = load_config()

    assert config["reference"]["genome_build"] == "GRCh38"
    assert config["reference"]["chromosome"] == "chr22"


def test_giab_release():
    config = load_config()

    assert config["benchmark"]["truth_set"]["version"] == "v4.2.1"


def test_benchmark_scales():
    config = load_config()

    region_sets = config["benchmark"]["region_sets"]
    region_counts = [item["n_regions"] for item in region_sets]

    assert region_counts == [5, 25, 50]


def test_comparison_tools():
    config = load_config()

    assert config["comparison"]["normalized"]["tool"] == "bcftools isec"
    assert config["comparison"]["formal"]["tool"] == "RTG vcfeval"


def test_analysis_components():
    config = load_config()

    analysis = config["analysis"]

    assert analysis["missed_variant_analysis"] is True
    assert analysis["difficult_region_analysis"] is True
    assert analysis["low_recall_analysis"] is True
    assert analysis["discrepancy_analysis"] is True
    assert analysis["benchmark_scale_comparison"] is True
