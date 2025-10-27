import subprocess
import pytest

from types import MappingProxyType
from typing import Any, Callable
from copier import Path, run_copy


@pytest.fixture(scope="session")
def use_copier(
    template_path: Path, template_commit_sha: str
) -> Callable[[Path, dict[str, str]], None]:
    def _use_copier(dst: Path, answers: dict[str, str]) -> None:
        run_copy(
            template_path.as_posix(),
            dst.as_posix(),
            data=answers,
            vcs_ref=template_commit_sha,
            quiet=True,
        )

    return _use_copier


@pytest.fixture(scope="session")
def template_path() -> Path:
    return Path(__file__).parent.parent


@pytest.fixture(scope="session")
def template_commit_sha() -> str:
    return subprocess.run(
        ["git", "rev-parse", "HEAD"], stdout=subprocess.PIPE, text=True
    ).stdout.strip()


@pytest.fixture(scope="session")
def sample_template_answers() -> MappingProxyType[str, Any]:
    return MappingProxyType(
        {
            "webapp_name": "streamlit-auth-app",
            "azure_appconfig_endpoint": "https://streamlit-auth-config.azconfig.io",
            "azure_container_registry_name": "acrtestuser",
            "docker_image_name": "streamlit-auth-app",
            "resource_group": "D28520",
        }
    )
