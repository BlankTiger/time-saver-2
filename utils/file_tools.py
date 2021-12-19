from os.path import splitext
from os import listdir
from os.path import join


def get_file_extension(file_path):
    return splitext(file_path)[1].lower().strip(".")


def get_images_from_path(path, extensions=("jpg", "jpeg", "png")):
    images_paths = []
    for file in listdir(path):
        for extension in extensions:
            if get_file_extension(file) == extension:
                images_paths.append(join(path, file))
    return images_paths


def file_paths_from_gui(chosen_files):
    return chosen_files.split(";")
