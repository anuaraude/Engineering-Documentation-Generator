from pathlib import Path


def save_readme(
    markdown: str,
    destination_folder: str,
    overwrite: bool = False,
) -> Path:
    """Save the generated Markdown as README.md."""

    folder_path = Path(destination_folder).expanduser()

    folder_path.mkdir(
        parents=True,
        exist_ok=True,
    )

    readme_path = folder_path / "README.md"

    if readme_path.exists() and not overwrite:
        raise FileExistsError(
            f"{readme_path} already exists."
        )

    if not markdown.endswith("\n"):
        markdown += "\n"

    readme_path.write_text(
        markdown,
        encoding="utf-8",
    )

    return readme_path.resolve()
