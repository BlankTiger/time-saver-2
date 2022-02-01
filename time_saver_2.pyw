import platform
from os import getcwd
from os.path import join
from sys import argv
from sys import exit

import PySimpleGUI as sg

from utils.argparser import get_args
from utils.file_tools import (
    file_paths_from_gui,
    get_file_extension,
    get_file_with_ext_from_path,
    merge_pdfs,
    zip_from_files,
)
from utils.gui import layout
from utils.image_tools import (
    compress_image,
    convert_image,
    convert_svg2pdf,
    pdf_from_images,
)

# Changes the GUI to be DPI aware so that the GUI is not pix elated
if platform.system() == "Windows":
    import ctypes

    ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(
        "CompanyName.ProductName.SubProduct.VersionInformation"
    )

    if platform.release() == "7":
        ctypes.windll.user32.SetProcessDPIAware()
    elif float(platform.release()) >= 8:
        ctypes.windll.shcore.SetProcessDpiAwareness(1)


def if_pack_pdf(file_name, files_path, folder_path, extensions, quality):
    """Packs images into a pdf.

    Function used for packing images into pdf if user decides to pack a pdf
    either from gui or cli. Wrapper function for pdf_from_images from
    image_tools.

    Args:
        file_name (str): Name of the output file.
        files_path (list): List of files to be compressed and merged.
        folder_path (str): Path to the folder where the files are located or to
            the folder where the output file will be saved.
        extensions (list): List of extensions that the user wants to pack into pdf.
        quality (int): Quality of the compression of images.
    """
    if files_path == [""] or files_path == "":
        file_paths = get_file_with_ext_from_path(folder_path, extensions)
        pdf_from_images(
            file_paths,
            join(folder_path, file_name),
            int(quality),
        )
        return

    pdf_from_images(files_path, join(folder_path, file_name), int(quality))


def if_pack_zip(file_name, files_path, folder_path, extensions, quality):
    """Packs images into a zip.

    Function used for packaging selected files into a zip file. If user decides
    to not choose files, function will zip all the files ending with the
    provided extensions in the folder_path. Wrapper function for zip_from_files
    from file_tools.

    Args:
        file_name (str): Name of the output file.
        files_path (list): List of files that will be zipped.
        folder_path (str): Path to the folder where the files are located or
            and where the output file will be saved.
        extensions (list): List of extensions that the user wants to pack into
            zip if files_path is empty.
        quality (int): Quality of the compression of images.
    """
    if files_path == [""] or files_path == "":
        file_paths = get_file_with_ext_from_path(folder_path, extensions)
        zip_from_files(file_paths, join(folder_path, file_name), int(quality))
        return

    zip_from_files(files_path, join(folder_path, file_name), int(quality))


def if_merge_pdfs(file_name, files_path, folder_path):
    """Merges pdfs.

    Function used for merging pdfs. If user decides to not choose files,
    function will merge all the pdfs in the folder_path. Wrapper function for
    merge_pdfs from file_tools.

    Args:
        file_name (str): Name of the output file.
        files_path (list): List of files that will be merged.
        folder_path (str): Path to the folder where the files are located or and
            where the output file will be saved.
    """
    if files_path == [""] or files_path == "":
        file_paths = get_file_with_ext_from_path(folder_path, "pdf")
        merge_pdfs(file_paths, join(folder_path, file_name))
        return

    merge_pdfs(files_path, join(folder_path, file_name))


def if_convert_png2jpg(files_path, folder_path):
    """Converts png to jpg.

    Function used for converting png to jpg. If user decides to not choose files,
    function will convert all the pngs in the folder_path. Wrapper function for
    convert_image from image_tools.

    Args:
        files_path (list): List of files that will be converted.
        folder_path (str): Path to the folder where the files are located or and
            where the output file will be saved.
    """
    if files_path == [""] or files_path == "":
        file_paths = get_file_with_ext_from_path(folder_path, "png")
        for file in file_paths:
            convert_image(file, "png", folder_path, "jpg")
        return

    for file in files_path:
        convert_image(file, "png", folder_path, "jpg")


def if_convert_jpg2png(files_path, folder_path):
    """Converts jpg to png.

    Function used for converting jpg to png. If user decides to not choose files,
    function will convert all the jpgs in the folder_path. Wrapper function for
    convert_image from image_tools.

    Args:
        files_path(list): List of files that will be converted.
        folder_path(str): Path to the folder where the files are located or and
            where the output file will be saved.
    """
    if files_path == [""] or files_path == "":
        file_paths = get_file_with_ext_from_path(folder_path, "jpg")
        for file in file_paths:
            convert_image(file, "jpg", folder_path, "png")
        return

    for file in files_path:
        convert_image(file, "jpg", folder_path, "png")


def if_convert_svg2pdf(file_paths, folder_path):
    """Converts svg to pdf.

    Function used for converting svg to pdf. If user decides to not choose files,
    function will convert all the svgs in the folder_path. Wrapper function for
    convert_svg2pdf from image_tools.

    Args:
        file_paths(list): List of files that will be converted.
        folder_path(str): Path to the folder where the files are located or and
            where the output file will be saved.
    """
    if file_paths == [""] or file_paths == "":
        file_paths = get_file_with_ext_from_path(folder_path, extensions=("svg"))
        for file in file_paths:
            convert_svg2pdf(file, folder_path)
        return

    for file in file_paths:
        convert_svg2pdf(file, folder_path)


def if_compress_images(files_path, folder_path, extensions, quality):
    """Compresses images.

    Function used for compressing images. If user decides to not choose files,
    function will compress all the images in the folder_path. Wrapper function
    for compress_images from image_tools.

    Args:
        files_path(list): List of files that will be compressed.
        folder_path(str): Path to the folder where the files are located or and
            where the output file will be saved.
        extensions(list): List of extensions that the user wants to compress.
        quality(int): Quality of the compression of images.
    """
    if files_path == [""] or files_path == "":
        file_paths = get_file_with_ext_from_path(folder_path, extensions)
        for file in file_paths:

            f_ext = get_file_extension(file)
            compress_image(file, f_ext, int(quality), folder_path, f_ext)
        return

    for file in files_path:
        f_ext = get_file_extension(file)
        compress_image(file, f_ext, int(quality), folder_path, f_ext)


if __name__ == "__main__":
    # Checks if the user gave any arguments to the script
    # if any arguments are given, the script will run as in CLI mode
    # if no arguments are given, the script will run as in GUI mode
    if len(argv) > 1:
        args = get_args()
        if args.pack_to_pdf:
            if_pack_pdf(
                args.output, args.files, args.destination, args.extensions, args.quality
            )
        elif args.pack_to_zip:
            if_pack_zip(
                args.output, args.files, args.destination, args.extensions, args.quality
            )
        elif args.merge_pdfs:
            if_merge_pdfs(args.output, args.files, args.destination)
        elif args.png2jpg:
            if_convert_png2jpg(args.files, args.destination)
        elif args.jpg2png:
            if_convert_jpg2png(args.files, args.destination)
        elif args.svg2pdf:
            if_convert_svg2pdf(args.files, args.destination)
        elif args.compress:
            if_compress_images(
                args.files, args.destination, args.extensions, args.quality
            )
        exit()
    window = sg.Window(
        "Time Saver 2.0",
        layout,
        icon=r".\icon.ico",
        finalize=True,
    )
    window["folder_path"].update(getcwd())

    current_extensions = ["jpg", "jpeg"]
    jpg_set = frozenset(("jpg", "jpeg"))
    while True:
        event, values = window.read()
        if event == "file_path":
            window["file_path"].update(values["file_path"].replace("/", "\\"))

        if event == "folder_path":
            window["folder_path"].update(values["folder_path"].replace("/", "\\"))

        if event == "pack_pdf":
            if_pack_pdf(
                values["file_name"],
                file_paths_from_gui(values["file_path"]),
                values["folder_path"],
                current_extensions,
                values["quality"],
            )

        if event == "pack_zip":
            if_pack_zip(
                values["file_name"],
                file_paths_from_gui(values["file_path"]),
                values["folder_path"],
                current_extensions,
                values["quality"],
            )

        if event == "merge_pdfs":
            if_merge_pdfs(
                values["file_name"],
                file_paths_from_gui(values["file_path"]),
                values["folder_path"],
            )

        if event == "convert_png2jpg":
            if_convert_png2jpg(
                file_paths_from_gui(values["file_path"]), values["folder_path"]
            )

        if event == "convert_jpg2png":
            if_convert_jpg2png(
                file_paths_from_gui(values["file_path"]), values["folder_path"]
            )

        if event == "convert_svg2pdf":
            if_convert_svg2pdf(
                file_paths_from_gui(values["file_path"]), values["folder_path"]
            )

        if event == "compress_images":
            if_compress_images(
                file_paths_from_gui(values["file_path"]),
                values["folder_path"],
                current_extensions,
                values["quality"],
            )

        if event == "jpg_chkbx":
            if "jpg" not in current_extensions:
                current_extensions.extend(jpg_set)
            else:
                for x in jpg_set:
                    current_extensions.remove(x)

        if event == "png_chkbx":
            if "png" not in current_extensions:
                current_extensions.append("png")
            else:
                current_extensions.remove("png")

        if event == "pdf_chkbx":
            if "pdf" not in current_extensions:
                current_extensions.append("pdf")
            else:
                current_extensions.remove("pdf")

        if event == "svg_chkbx":
            if "svg" not in current_extensions:
                current_extensions.append("svg")
            else:
                current_extensions.remove("svg")

        if event in (None, "Exit"):
            break
