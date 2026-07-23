import pytest

from src.configuration import create_readme_configuration
from src.document_generator import generate_readme
from src.readme_contract import MissingCoreFieldsError


def build_test_configuration() -> dict:
    """Create a complete README configuration for testing."""

    return create_readme_configuration(
        project_name="Test Engineering Project",
        short_description="A controlled README generation test.",
        problem_statement="A repeatable documentation problem.",
        project_overview="A modular test project overview.",
        project_justification="A measurable testing justification.",
        prerequisites="Python 3.11",
        installation_instructions="Clone the test repository.",
        first_execution_command="python -m test_project",
        expected_result="A generated test README.",
        current_stage="Testing",
        status_description="The test project is under verification.",
        authors="Test Engineer",
        license_name="Test-License-1.0",
    )


def test_generate_readme_includes_all_configuration_values() -> None:
    configuration = build_test_configuration()

    markdown = generate_readme(configuration)

    expected_values = (
        "Test Engineering Project",
        "A controlled README generation test.",
        "A repeatable documentation problem.",
        "A modular test project overview.",
        "A measurable testing justification.",
        "Python 3.11",
        "Clone the test repository.",
        "python -m test_project",
        "A generated test README.",
        "Testing",
        "The test project is under verification.",
        "Test Engineer",
        "Test-License-1.0",
    )

    for expected_value in expected_values:
        assert expected_value in markdown


def test_generate_readme_replaces_all_expected_placeholders() -> None:
    configuration = build_test_configuration()

    markdown = generate_readme(configuration)

    expected_placeholders = (
        "project_name",
        "short_description",
        "problem_statement",
        "project_overview",
        "project_justification",
        "prerequisites",
        "installation_instructions",
        "first_execution_command",
        "expected_result",
        "current_stage",
        "status_description",
        "authors",
        "license_name",
    )

    for placeholder in expected_placeholders:
        assert f"{{{placeholder}}}" not in markdown


def test_generate_readme_rejects_missing_required_value() -> None:
    configuration = build_test_configuration()
    del configuration["header"]["project_name"]

    with pytest.raises(MissingCoreFieldsError) as exc_info:
        generate_readme(configuration)

    assert exc_info.value.missing_fields == (
        "header.project_name",
    )


def test_generate_readme_preserves_core_section_order() -> None:
    configuration = build_test_configuration()

    markdown = generate_readme(configuration)

    section_markers = (
        "# Test Engineering Project",
        "## About",
        "## Getting Started",
        "## Project Status",
        "## Author",
        "## License",
    )

    section_positions = [
        markdown.index(marker)
        for marker in section_markers
    ]

    assert section_positions == sorted(section_positions)


def test_generate_readme_ends_with_single_newline() -> None:
    configuration = build_test_configuration()

    markdown = generate_readme(configuration)

    assert markdown.endswith("\n")
    assert not markdown.endswith("\n\n")


def test_generate_readme_has_consistent_section_spacing() -> None:
    configuration = build_test_configuration()

    markdown = generate_readme(configuration)

    assert not markdown.startswith("\n")
    assert "\n\n\n" not in markdown