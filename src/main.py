from configuration import create_readme_configuration
from document_generator import generate_readme
from user_interface import (
    choose_document_type,
    collect_about_information,
    collect_header_information,
    show_main_menu,
)


def main():
    option = show_main_menu()

    if option == "1":
        document_type = choose_document_type()

        if document_type == "1":
            project_name, short_description = collect_header_information()

            (
                problem_statement,
                project_overview,
                project_justification,
            ) = collect_about_information()

            readme_configuration = create_readme_configuration(
                project_name=project_name,
                short_description=short_description,
                problem_statement=problem_statement,
                project_overview=project_overview,
                project_justification=project_justification,
            )

            markdown = generate_readme(readme_configuration)

            print()
            print("Generated README")
            print("----------------")
            print(markdown)

        elif document_type == "2":
            print()
            print("Technical Knowledge Document is not implemented yet.")

        else:
            print("Invalid document type.")

    elif option == "2":
        print("Goodbye!")

    else:
        print("Invalid option.")


if __name__ == "__main__":
    main()