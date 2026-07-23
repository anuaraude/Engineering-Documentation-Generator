import pytest

from src.configuration import create_readme_configuration
from src.readme_contract import (
    MissingCoreFieldsError,
    validate_readme_configuration,
)


REQUIRED_FIELD_PATHS = (
    ("header", "project_name"),
    ("header", "short_description"),
    ("about", "problem_statement"),
    ("about", "project_overview"),
    ("about", "project_justification"),
    ("getting_started", "prerequisites"),
    ("getting_started", "installation_instructions"),
    ("getting_started", "first_execution_command"),
    ("getting_started", "expected_result"),
    ("project_status", "current_stage"),
    ("project_status", "status_description"),
    ("author", "authors"),
    ("license", "license_name"),
)


def build_test_configuration() -> dict:
    """Create a complete README configuration for contract tests."""

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


def test_validate_readme_configuration_accepts_complete_configuration(
) -> None:
    configuration = build_test_configuration()

    result = validate_readme_configuration(configuration)

    assert result is None


@pytest.mark.parametrize(
    ("section_name", "field_name"),
    REQUIRED_FIELD_PATHS,
)
def test_validate_readme_configuration_reports_each_missing_field(
    section_name: str,
    field_name: str,
) -> None:
    configuration = build_test_configuration()
    del configuration[section_name][field_name]

    expected_path = f"{section_name}.{field_name}"

    with pytest.raises(MissingCoreFieldsError) as exc_info:
        validate_readme_configuration(configuration)

    assert exc_info.value.missing_fields == (expected_path,)
    assert expected_path in str(exc_info.value)


def test_validate_readme_configuration_reports_all_missing_fields() -> None:
    configuration = build_test_configuration()

    del configuration["header"]["project_name"]
    del configuration["about"]["project_overview"]
    del configuration["license"]["license_name"]

    expected_paths = (
        "header.project_name",
        "about.project_overview",
        "license.license_name",
    )

    with pytest.raises(MissingCoreFieldsError) as exc_info:
        validate_readme_configuration(configuration)

    assert exc_info.value.missing_fields == expected_paths

    for expected_path in expected_paths:
        assert expected_path in str(exc_info.value)


def test_validate_readme_configuration_reports_missing_section_fields(
) -> None:
    configuration = build_test_configuration()
    del configuration["header"]

    expected_paths = (
        "header.project_name",
        "header.short_description",
    )

    with pytest.raises(MissingCoreFieldsError) as exc_info:
        validate_readme_configuration(configuration)

    assert exc_info.value.missing_fields == expected_paths


def test_validate_readme_configuration_reports_invalid_section_fields(
) -> None:
    configuration = build_test_configuration()
    configuration["header"] = "invalid section"

    expected_paths = (
        "header.project_name",
        "header.short_description",
    )

    with pytest.raises(MissingCoreFieldsError) as exc_info:
        validate_readme_configuration(configuration)

    assert exc_info.value.missing_fields == expected_paths
