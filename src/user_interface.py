def show_main_menu():
    print("=========================================")
    print("Engineering Documentation Generator")
    print("Version 0.4")
    print("=========================================")
    print()
    print("Welcome!")
    print()
    print("Please select an option.")
    print("1. Create New Project")
    print("2. Exit")
    print()

    return input("Option: ").strip()


def collect_header_information() -> tuple[str, str]:
    """Collect the information required by the README header."""

    print()
    print("Header Information")
    print("------------------")

    project_name = input("Project name: ").strip()
    short_description = input(
        "Short description (one or two sentences): "
    ).strip()

    return project_name, short_description


def collect_about_information() -> tuple[str, str, str]:
    """Collect the information required by the About section."""

    print()
    print("About Information")
    print("-----------------")

    problem_statement = input(
        "What problem or need motivated this project? "
    ).strip()

    project_overview = input(
        "What does the project do in general? "
    ).strip()

    project_justification = input(
        "Why is this project worth developing? "
    ).strip()

    return (
        problem_statement,
        project_overview,
        project_justification,
    )


def collect_getting_started_information() -> tuple[str, str, str, str]:
    """Collect the information required by the Getting Started section."""

    print()
    print("Getting Started Information")
    print("---------------------------")

    prerequisites = input(
        "What prerequisites are required to use this project? "
    ).strip()

    installation_instructions = input(
        "How should the project be installed or configured? "
    ).strip()

    first_execution_command = input(
        "What command should be used for the first execution? "
    ).strip()

    expected_result = input(
        "What result should the user expect after running it? "
    ).strip()

    return (
        prerequisites,
        installation_instructions,
        first_execution_command,
        expected_result,
    )


def collect_project_status_information() -> tuple[str, str]:
    """Collect the information required by the Project Status section."""

    print()
    print("Project Status Information")
    print("--------------------------")

    current_stage = input(
        "Current stage "
        "(Planning, In Development, Beta, Stable, or Archived): "
    ).strip()

    status_description = input(
        "Briefly describe the current state of the project: "
    ).strip()

    return current_stage, status_description


def collect_author_information() -> str:
    """Collect the information required by the Author section."""

    print()
    print("Author Information")
    print("------------------")

    authors = input(
        "Author name or author names separated by commas: "
    ).strip()

    return authors


def collect_license_information() -> str:
    """Collect the information required by the License section."""

    print()
    print("License Information")
    print("-------------------")

    license_name = input(
        "License name "
        "(MIT, Apache-2.0, GPL-3.0, Proprietary, etc.): "
    ).strip()

    return license_name


def choose_document_type() -> str:
    """Ask the user which type of document they want to generate."""

    print()
    print("Select document type")
    print("--------------------")
    print("1. README")
    print("2. Technical Knowledge Document")
    print()

    return input("Document type: ").strip()