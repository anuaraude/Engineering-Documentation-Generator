from pathlib import Path

import pytest

from src.file_writer import save_readme


def test_save_readme_creates_file_with_expected_content(
    tmp_path: Path,
) -> None:
    markdown = "# Test Project\n"

    saved_path = save_readme(
        markdown=markdown,
        destination_folder=str(tmp_path),
    )

    assert saved_path.exists()
    assert saved_path.name == "README.md"
    assert saved_path.read_text(encoding="utf-8") == markdown


def test_save_readme_creates_missing_destination_directories(
    tmp_path: Path,
) -> None:
    destination_folder = tmp_path / "nested" / "output"

    saved_path = save_readme(
        markdown="# Nested Project\n",
        destination_folder=str(destination_folder),
    )

    assert destination_folder.exists()
    assert saved_path == (destination_folder / "README.md").resolve()


def test_save_readme_raises_error_when_file_already_exists(
    tmp_path: Path,
) -> None:
    existing_readme = tmp_path / "README.md"
    existing_readme.write_text(
        "# Existing Project\n",
        encoding="utf-8",
    )

    with pytest.raises(FileExistsError, match="already exists"):
        save_readme(
            markdown="# New Project\n",
            destination_folder=str(tmp_path),
        )


def test_save_readme_overwrites_existing_file_when_authorized(
    tmp_path: Path,
) -> None:
    existing_readme = tmp_path / "README.md"
    existing_readme.write_text(
        "# Existing Project\n",
        encoding="utf-8",
    )

    saved_path = save_readme(
        markdown="# Updated Project\n",
        destination_folder=str(tmp_path),
        overwrite=True,
    )

    assert saved_path == existing_readme.resolve()
    assert existing_readme.read_text(
        encoding="utf-8",
    ) == "# Updated Project\n"


def test_save_readme_adds_final_newline_when_missing(
    tmp_path: Path,
) -> None:
    saved_path = save_readme(
        markdown="# Project without final newline",
        destination_folder=str(tmp_path),
    )

    saved_content = saved_path.read_text(encoding="utf-8")

    assert saved_content == "# Project without final newline\n"


def test_save_readme_preserves_utf8_content(
    tmp_path: Path,
) -> None:
    markdown = (
        "# Proyecto de visión\n\n"
        "Documentación técnica: percepción, cámara y medición.\n"
    )

    saved_path = save_readme(
        markdown=markdown,
        destination_folder=str(tmp_path),
    )

    saved_content = saved_path.read_text(encoding="utf-8")

    assert saved_content == markdown