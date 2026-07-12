def create_readme_configuration(
    project_name: str,
    short_description: str,
    problem_statement: str,
    project_overview: str,
    project_justification: str,
) -> dict:
    """Create the initial README configuration."""

    return {
        "header": {
            "project_name": project_name,
            "short_description": short_description,
        },
        "about": {
            "problem_statement": problem_statement,
            "project_overview": project_overview,
            "project_justification": project_justification,
        },
    }