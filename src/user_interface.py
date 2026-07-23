def show_main_menu():
    print("=========================================")
    print("Engineering Documentation Generator")
    print("Version 0.6")
    print("=========================================")
    print()
    print("Welcome!")
    print()
    print("Please select an option.")
    print("1. Create New Project")
    print("2. Exit")
    print()

    return ask_valid_option(
        prompt="Option: ",
        valid_options=("1", "2"),
    )


def choose_document_type() -> str:
    """Ask the user which type of document they want to generate."""

    print()
    print("Select document type")
    print("--------------------")
    print("1. README")
    print("2. Technical Knowledge Document (deferred)")
    print()

    return ask_valid_option(
        prompt="Document type: ",
        valid_options=("1", "2"),
    )


def ask_required_text(prompt: str) -> str:
    """Ask for required text and repeat until a value is provided."""

    while True:
        value = input(prompt).strip()

        if value:
            return value

        print("This field is required. Please enter a value.")


def ask_valid_option(
    prompt: str,
    valid_options: tuple[str, ...],
) -> str:
    """Ask for an option and repeat until it is valid."""

    while True:
        option = input(prompt).strip()

        if option in valid_options:
            return option

        print(
            "Invalid option. Please enter one of: "
            f"{', '.join(valid_options)}."
        )


def collect_header_information() -> tuple[str, str]:
    """Collect the information required by the README header."""

    print()
    print("Header Information")
    print("------------------")

    project_name = ask_required_text(
        "Project name: "
    )

    short_description = ask_required_text(
        "Short description (one or two sentences): "
    )

    return project_name, short_description


def collect_about_information() -> tuple[str, str, str]:
    """Collect the information required by the About section."""

    print()
    print("About Information")
    print("-----------------")

    problem_statement = ask_required_text(
        "What problem or need motivated this project? "
    )

    project_overview = ask_required_text(
        "What does the project do in general? "
    )

    project_justification = ask_required_text(
        "Why is this project worth developing? "
    )

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

    prerequisites = ask_required_text(
        "What prerequisites are required to use this project? "
    )

    installation_instructions = ask_required_text(
        "How should the project be installed or configured? "
    )

    first_execution_command = ask_required_text(
        "What command should be used for the first execution? "
    )

    expected_result = ask_required_text(
        "What result should the user expect after running it? "
    )

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

    current_stage = ask_required_text(
        "Current stage "
        "(Planning, In Development, Beta, Stable, or Archived): "
    )

    status_description = ask_required_text(
        "Briefly describe the current state of the project: "
    )

    return current_stage, status_description


def collect_author_information() -> str:
    """Collect the information required by the Author section."""

    print()
    print("Author Information")
    print("------------------")

    authors = ask_required_text(
        "Author name or author names separated by commas: "
    )

    return authors


def collect_license_information() -> str:
    """Collect the information required by the License section."""

    print()
    print("License Information")
    print("-------------------")

    license_name = ask_required_text(
        "License name "
        "(MIT, Apache-2.0, GPL-3.0, Proprietary, etc.): "
    )

    return license_name
