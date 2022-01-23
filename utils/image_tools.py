from os import remove
from os.path import basename
from os.path import join as join_path

from cairosvg import svg2pdf
from PIL.Image import open as open_image
from PIL.ImageOps import exif_transpose
from PyPDF4 import PdfFileMerger


def convert_image_to_pdf(image_path, extension, quality_value=100):
    """Converts an image to a pdf.

    Args:
        image_path (str): The path to the image.
        extension (str): The extension of the image.
        quality_value (int): The compression quality.

    Returns:
        str: The path to the pdf.
    """
    if extension == "svg":
        return convert_svg2pdf(image_path, "")

    image = open_image(image_path).convert("RGB")
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


def convert_svg2pdf(file, folder_path):
    """Converts an svg to a pdf.

    Args:
        file (str): The path to the svg.
        folder_path (str): The path where the pdf will be saved.

    Returns:
        str: The path to the pdf.
    """
    path = join_path(folder_path, basename(file).lower().replace(".svg", ".pdf"))
    svg2pdf(url=file, write_to=path)
    return path


def convert_image(image_path, extension, folder_path="", new_extension=""):
    """Converts between JPG and PNG.

    Function uses compress_image function to convert the image while not
    compressing because quality is set to 100.

    Args:
        image_path (str): The path to the image.
        extension (str): The extension of the image.
        folder_path (str): The path where the image will be saved.
        new_extension (str): The new extension of the image.

    Returns:
        str: The path to the image.
    """
    return compress_image(image_path, extension, 100, folder_path, new_extension)


def compress_image(
    image_path, extension, quality_value, folder_path="", new_extension=""
):
    """Compresses an image.

    Args:
        image_path (str): The path to the image.
        extension (str): The extension of the image.
        quality_value (int): The compression quality.
        folder_path (str): The path where the image will be saved.
        new_extension (str): The new extension of the image.

    Returns:
        str: The path to the image.
    """
    if extension not in ["jpg", "jpeg", "png"]:
        return
    image = None
    if new_extension == "":
        new_extension = extension
    image = open_image(image_path).convert("RGB")
    image = exif_transpose(image)
    new_path = join_path(
        folder_path,
        "".join(
            (
                basename(image_path).replace(extension, "").rstrip("."),
                "_compressed",
                ".",
                new_extension,
            )
        ),
    )

    image.save(
        new_path,
        optimize=True,
        quality=quality_value,
    )
    image.close()
    return new_path


def pdf_from_images(images_paths, pdf_name, quality_value=100):
    """Creates a pdf from a list of images.

    Args:
        images_paths (list): The paths to the images.
        pdf_name (str): The name of the pdf.
        quality_value (int): The compression quality.
    """
    from .file_tools import get_file_extension

    new_paths = []
    for image in images_paths:
        f_ext = get_file_extension(image)
        if f_ext == "pdf":
            new_paths.append(image + "already")
        elif f_ext == "svg":
            new_paths.append(convert_image_to_pdf(image, f_ext, 100))
        else:
            new_paths.append(convert_image_to_pdf(image, f_ext, quality_value))
    pdf_merger = PdfFileMerger()
    for file in new_paths:
        if file.endswith("already"):
            file = file.replace("already", "")
        pdf_merger.append(file)
    with open(pdf_name + ".pdf", "wb") as fileobj:
        pdf_merger.write(fileobj)
        pdf_merger.close()
    for file in new_paths:
        if not file.endswith("already"):
            remove(file)
