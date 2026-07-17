from template_manager import load_template


def generate_readme(readme_configuration: dict) -> str:
    """Generate a README document from modular templates."""

    # Load core templates
    header_template = load_template("readme/core/header.md")
    about_template = load_template("readme/core/about.md")
    getting_started_template = load_template(
        "readme/core/getting_started.md"
    )
    project_status_template = load_template(
        "readme/core/project_status.md"
    )
    author_template = load_template("readme/core/author.md")
    license_template = load_template("readme/core/license.md")

    # Extract configuration data
    header_data = readme_configuration["header"]
    about_data = readme_configuration["about"]
    getting_started_data = readme_configuration["getting_started"]
    project_status_data = readme_configuration["project_status"]
    author_data = readme_configuration["author"]
    license_data = readme_configuration["license"]

    # Generate core sections
    header_markdown = header_template.format(
        project_name=header_data["project_name"],
        short_description=header_data["short_description"],
    )

    about_markdown = about_template.format(
        problem_statement=about_data["problem_statement"],
        project_overview=about_data["project_overview"],
        project_justification=about_data["project_justification"],
    )

    getting_started_markdown = getting_started_template.format(
        prerequisites=getting_started_data["prerequisites"],
        installation_instructions=getting_started_data[
            "installation_instructions"
        ],
        first_execution_command=getting_started_data[
            "first_execution_command"
        ],
        expected_result=getting_started_data["expected_result"],
    )

    project_status_markdown = project_status_template.format(
        current_stage=project_status_data["current_stage"],
        status_description=project_status_data["status_description"],
    )

    author_markdown = author_template.format(
        authors=author_data["authors"],
    )

    license_markdown = license_template.format(
        license_name=license_data["license_name"],
    )

    core_sections = [
        header_markdown,
        about_markdown,
        getting_started_markdown,
        project_status_markdown,
        author_markdown,
        license_markdown,
    ]

    clean_sections = [
        section.strip()
        for section in core_sections
    ]

    return "\n\n".join(clean_sections) + "\n"
