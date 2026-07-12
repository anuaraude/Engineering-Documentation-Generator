from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parent.parent
TEMPLATES_DIRECTORY = PROJECT_ROOT / "templates"


def load_template(relative_path: str) -> str:
    """Load and return a Markdown template as text."""

    template_path = TEMPLATES_DIRECTORY / relative_path

    return template_path.read_text(encoding="utf-8")
