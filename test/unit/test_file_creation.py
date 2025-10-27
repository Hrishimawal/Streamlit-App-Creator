from pathlib import Path
from tempfile import TemporaryDirectory
from types import MappingProxyType
from typing import Callable
import pytest

@pytest.mark.parametrize(
    "expected_file",
    [
        ".copier-answers.yml",
        ".gitignore",
        ".gitlab-ci.yml",
        "Dockerfile",
        "README.md",
        "requirements.txt",
        "streamlit_app.py",
    ],
)
def test_file_creation(
    use_copier: Callable[[Path, dict[str, str]], None],
    sample_template_answers: MappingProxyType[str, str],
    expected_file: str,
) -> None:
    answers = dict(sample_template_answers)
    with TemporaryDirectory() as tmp_dir:
        use_copier(Path(tmp_dir), answers)
        assert (Path(tmp_dir) / expected_file).exists(), f"{expected_file} was not created"
