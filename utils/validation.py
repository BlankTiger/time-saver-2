def validate_file_extensions(file_path, extensions):
    """Validates the file extension.

    Args:
        file_path (str): The path to the file.
        extensions (list): The list of extensions.

    Returns:
        bool: True if the file extension is valid, False otherwise.
    """
    for file in file_path:
        for extension in extensions:
            if not file.endswith(extension):
                return False
    return True
