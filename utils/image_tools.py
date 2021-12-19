from os import remove
from os.path import basename
from os.path import join as join_path

from cairosvg import svg2pdf
from PIL.Image import open as open_image
from PIL.ImageOps import exif_transpose
from PyPDF4 import PdfFileMerger


def convert_image_to_pdf(image_path, extension, quality_value=100) -> None:
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
    path = join_path(
        folder_path, basename(file).lower().replace(".svg", ".pdf")
    )
    svg2pdf(url=file, write_to=path)
    return path


def convert_image(image_path, extension, folder_path="", new_extension=""):
    return compress_image(
        image_path, extension, 100, folder_path, new_extension
    )


def compress_image(
    image_path, extension, quality_value, folder_path="", new_extension=""
):
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
