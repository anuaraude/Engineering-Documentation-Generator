REQUIRED_README_FIELDS = {
    "header": (
        "project_name",
        "short_description",
    ),
    "about": (
        "problem_statement",
        "project_overview",
        "project_justification",
    ),
    "getting_started": (
        "prerequisites",
        "installation_instructions",
        "first_execution_command",
        "expected_result",
    ),
    "project_status": (
        "current_stage",
        "status_description",
    ),
    "author": (
        "authors",
    ),
    "license": (
        "license_name",
    ),
}


class MissingCoreFieldsError(KeyError):
    """Raised when required README Core fields are missing."""

    def __init__(self, missing_fields: tuple[str, ...]) -> None:
        self.missing_fields = missing_fields
        super().__init__(missing_fields)

    def __str__(self) -> str:
        missing_field_list = "\n".join(
            f"- {field_path}"
            for field_path in self.missing_fields
        )

        return (
            "Missing required README fields:\n"
            f"{missing_field_list}"
        )


def validate_readme_configuration(
    readme_configuration: dict,
) -> None:
    """Validate the presence of every required README Core field."""

    missing_fields = []

    for section_name, required_fields in REQUIRED_README_FIELDS.items():
        section_data = readme_configuration.get(section_name)

        if not isinstance(section_data, dict):
            missing_fields.extend(
                f"{section_name}.{field_name}"
                for field_name in required_fields
            )
            continue

        for field_name in required_fields:
            if field_name not in section_data:
                missing_fields.append(
                    f"{section_name}.{field_name}"
                )

    if missing_fields:
        raise MissingCoreFieldsError(tuple(missing_fields))
