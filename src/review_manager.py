def confirm_save() -> bool:
    """Ask the user whether the generated document should be saved."""

    while True:
        response = input(
            "Do you want to save this document? (y/n): "
        ).strip().lower()

        if response in ("y", "yes"):
            return True

        if response in ("n", "no"):
            return False

        print("Invalid option. Please enter y or n.")


def confirm_overwrite() -> bool:
    """Ask the user whether an existing document should be overwritten."""

    while True:
        response = input(
            "A README.md file already exists in the destination folder. "
            "Overwrite it? (y/n): "
        ).strip().lower()

        if response in ("y", "yes"):
            return True

        if response in ("n", "no"):
            return False

        print("Invalid option. Please enter y or n.")


def collect_destination_folder() -> str:
    """Ask the user where the generated README should be saved."""

    destination_folder = input(
        "Destination folder [./output]: "
    ).strip()

    destination_folder = destination_folder.strip('"').strip()

    if not destination_folder:
        return "./output"

    return destination_folder
