def create_readme_configuration(
    project_name: str,
    short_description: str,
    problem_statement: str,
    project_overview: str,
    project_justification: str,
    prerequisites: str,
    installation_instructions: str,
    first_execution_command: str,
    expected_result: str,
    current_stage: str,
    status_description: str,
    authors: str,
    license_name: str,
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
        "getting_started": {
            "prerequisites": prerequisites,
            "installation_instructions": installation_instructions,
            "first_execution_command": first_execution_command,
            "expected_result": expected_result,
        },
        "project_status": {
            "current_stage": current_stage,
            "status_description": status_description,
        },
        "author": {
            "authors": authors,
        },
        "license": {
            "license_name": license_name,
        },
    }
