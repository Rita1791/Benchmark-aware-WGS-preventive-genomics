
### `tests/test_repository_structure.py`

```python
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]


REQUIRED_DIRECTORIES = [
    "config",
    "docs",
    "pipeline",
    "reports",
    "results",
    "scripts",
    "tests",
    "reference_datasets",
    "manuscript",
]


REQUIRED_FILES = [
    "README.md",
    "CITATION.cff",
    "LICENSE",
    "environment.yml",
    ".gitignore",
    "config/benchmark.yaml",
    "docs/data_provenance.md",
    "docs/software_versions.md",
]


def test_required_directories_exist():
    missing = [
        directory
        for directory in REQUIRED_DIRECTORIES
        if not (REPO_ROOT / directory).is_dir()
    ]

    assert not missing, f"Missing required directories: {missing}"


def test_required_files_exist():
    missing = [
        file_path
        for file_path in REQUIRED_FILES
        if not (REPO_ROOT / file_path).is_file()
    ]

    assert not missing, f"Missing required files: {missing}"


def test_main_readme_is_not_empty():
    readme = REPO_ROOT / "README.md"

    assert readme.stat().st_size > 1000, (
        "README.md appears too small for the main project documentation."
    )
