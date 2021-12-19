def validate_file_extensions(file_path, extensions):
    for file in file_path:
        for extension in extensions:
            if not file.endswith(extension):
                return False
    return True
