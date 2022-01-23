from os import listdir, remove
from os.path import basename, join, splitext
from zipfile import ZipFile

from PyPDF4 import PdfFileMerger


def get_file_extension(file_path):
    """Returns the extension from a file path.

    Args:
        file_path (str): The file path.
    """
    return splitext(file_path)[1].lower().strip(".")


def get_file_with_ext_from_path(path, extensions=("jpg", "jpeg", "png")):
    """Returns all files with the given extension from the given path.

    Args:
        path (str): The path to the folder.
        extensions (list): The extensions to look for.

    Returns:
        list: A list of files with the given extension from the given path.
    """

    file_paths = []
    for file in listdir(path):
        f_ext = get_file_extension(file)
        if f_ext in extensions and not f_ext == "":
            file_paths.append(join(path, file))
    return file_paths


def merge_pdfs(pdf_paths, pdf_name):
    """Merges multiple pdfs into one.

    Args:
        pdf_paths (list): A list of pdf paths.
        pdf_name (str): The name of the merged pdf.
    """
    pdf_merger = PdfFileMerger()
    for file in pdf_paths:
        pdf_merger.append(file)
    with open(pdf_name + ".pdf", "wb") as fileobj:
        pdf_merger.write(fileobj)
        pdf_merger.close()


def zip_from_files(file_paths, zip_name, quality_value=100):
    """Zips the given files.

    If the file is an image it will be compressed with the given quality value.

    Args:
        file_paths (list): A list of file paths.
        zip_name (str): The name of the zip file.
        quality_value (int): The compression quality.
    """
    from .image_tools import compress_image

    new_paths = []
    for image in file_paths:
        f_ext = get_file_extension(image)
        if f_ext == "pdf":
            new_paths.append(image + "already")
        elif f_ext == "svg":
            new_paths.append(image)
        elif quality_value != 100 and f_ext in ("jpg", "jpeg", "png"):
            new_paths.append(
                compress_image(image, get_file_extension(image), quality_value)
            )
        else:
            new_paths.append(image)
    zip_file = ZipFile(zip_name + ".zip", "w")
    for file in new_paths:
        if file.endswith("already"):
            file = file.replace("already", "")
        zip_file.write(file, basename(file))
    for file in new_paths:
        if not file.endswith(("already", "svg")):
            if file.endswith(
                (
                    "_compressed.pdf",
                    "_compressed.jpg",
                    "_compressed.jpeg",
                    "_compressed.png",
                )
            ):
                remove(file)
    zip_file.close()


def file_paths_from_gui(chosen_files):
    """Returns a list of file paths from the given string of chosen files.

    File paths from gui are separated by ";". This function will split the string
    and return a list of file paths.

    Args:
        chosen_files (str): A string containing chosen files.
    """
    return chosen_files.split(";")
