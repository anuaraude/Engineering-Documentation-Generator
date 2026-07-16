from configuration import create_readme_configuration
from document_generator import generate_readme
from user_interface import (
    choose_document_type,
    collect_about_information,
    collect_author_information,
    collect_getting_started_information,
    collect_header_information,
    collect_license_information,
    collect_project_status_information,
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

            (
                prerequisites,
                installation_instructions,
                first_execution_command,
                expected_result,
            ) = collect_getting_started_information()

            (
                current_stage,
                status_description,
            ) = collect_project_status_information()

            authors = collect_author_information()
            license_name = collect_license_information()

            readme_configuration = create_readme_configuration(
                project_name=project_name,
                short_description=short_description,
                problem_statement=problem_statement,
                project_overview=project_overview,
                project_justification=project_justification,
                prerequisites=prerequisites,
                installation_instructions=installation_instructions,
                first_execution_command=first_execution_command,
                expected_result=expected_result,
                current_stage=current_stage,
                status_description=status_description,
                authors=authors,
                license_name=license_name,
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