def show_main_menu():
    print("=========================================")
    print("Engineering Documentation Generator")
    print("Version 0.1")
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


def choose_document_type() -> str:
    """Ask the user which type of document they want to generate."""

    print()
    print("Select document type")
    print("--------------------")
    print("1. README")
    print("2. Technical Knowledge Document")
    print()

    return input("Document type: ").strip()
    """Ask the user which type of document they want to generate."""

    print()
    print("Select document type")
    print("--------------------")
    print("1. README")
    print("2. Technical Knowledge Document")
    print()

    return input("Document type: ").strip()