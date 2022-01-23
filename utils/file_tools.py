from os import listdir, remove
from os.path import basename, join, splitext
from zipfile import ZipFile

from PyPDF4 import PdfFileMerger


def get_file_extension(file_path):
    return splitext(file_path)[1].lower().strip(".")


def get_file_with_ext_from_path(path, extensions=("jpg", "jpeg", "png")):
    images_paths = []
    for file in listdir(path):
        f_ext = get_file_extension(file)
        if f_ext in extensions and not f_ext == "":
            images_paths.append(join(path, file))
    return images_paths


def merge_pdfs(pdf_paths, pdf_name):
    pdf_merger = PdfFileMerger()
    for file in pdf_paths:
        pdf_merger.append(file)
    with open(pdf_name + ".pdf", "wb") as fileobj:
        pdf_merger.write(fileobj)
        pdf_merger.close()


def zip_from_files(images_paths, zip_name, quality_value=100):
    from .image_tools import compress_image

    new_paths = []
    for image in images_paths:
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
    return chosen_files.split(";")
