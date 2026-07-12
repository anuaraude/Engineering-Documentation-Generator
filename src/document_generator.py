from template_manager import load_template


def generate_readme(readme_configuration: dict) -> str:
    """Generate a README document from modular templates."""

    header_template = load_template("readme/core/header.md")
    about_template = load_template("readme/core/about.md")

    header_data = readme_configuration["header"]
    about_data = readme_configuration["about"]

    header_markdown = header_template.format(
        project_name=header_data["project_name"],
        short_description=header_data["short_description"],
    )

    about_markdown = about_template.format(
        problem_statement=about_data["problem_statement"],
        project_overview=about_data["project_overview"],
        project_justification=about_data["project_justification"],
    )

    markdown_sections = [
        header_markdown,
        about_markdown,
    ]

    return "\n\n".join(markdown_sections)