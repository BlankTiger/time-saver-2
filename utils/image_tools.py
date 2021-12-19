from PyPDF4 import PdfFileMerger
from PIL.Image import open as open_image
from PIL.ImageOps import exif_transpose
from os import remove
from os.path import basename
from zipfile import ZipFile
from .file_tools import get_file_extension


def merge_pdfs(pdf_paths, pdf_name):
    pdf_merger = PdfFileMerger()
    for file in pdf_paths:
        pdf_merger.append(file)
    with open(pdf_name + ".pdf", "wb") as fileobj:
        pdf_merger.write(fileobj)
        pdf_merger.close()


def convert_image_to_pdf(image_path, extension, quality_value=100) -> None:
    image = open_image(image_path)
    image = exif_transpose(image)
    new_path = "".join((image_path.rstrip("." + extension), "_compressed.pdf"))
    image.save(
        new_path,
        "PDF",
        optimize=True,
        quality=quality_value,
    )
    image.close()
    return new_path


def compress_image(image_path, extension, quality_value=100):
    image = open_image(image_path)
    image = exif_transpose(image)
    new_path = "".join(
        (image_path.rstrip("." + extension), "_compressed", extension)
    )
    image.save(
        new_path,
        optimize=True,
        quality=quality_value,
    )
    image.close()
    return new_path


def pdf_from_images(images_paths, pdf_name, quality_value=100):
    new_paths = []
    for image in images_paths:
        if get_file_extension(image) == "pdf":
            new_paths.append(image)
        else:
            new_paths.append(
                convert_image_to_pdf(
                    image, get_file_extension(image), quality_value
                )
            )
    pdf_merger = PdfFileMerger()
    for file in new_paths:
        pdf_merger.append(file)
    with open(pdf_name + ".pdf", "wb") as fileobj:
        pdf_merger.write(fileobj)
        pdf_merger.close()
    for file in new_paths:
        remove(file)


def zip_from_images(images_paths, zip_name, quality_value=100):
    new_paths = []
    for image in images_paths:
        new_paths.append(
            compress_image(image, get_file_extension(image), quality_value)
        )
    zip_file = ZipFile(zip_name + ".zip", "w")
    for file in new_paths:
        zip_file.write(file, basename(file))
    for file in new_paths:
        remove(file)
    zip_file.close()
