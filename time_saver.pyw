import platform
from os import getcwd
from os.path import join
from sys import argv

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

if platform.system() == "Windows":
    import ctypes

    if platform.release() == "7":
        ctypes.windll.user32.SetProcessDPIAware()
    elif float(platform.release()) >= 8:
        ctypes.windll.shcore.SetProcessDpiAwareness(1)


def if_pack_pdf(file_name, files_path, folder_path, extensions, quality):
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
    if files_path == [""] or files_path == "":
        file_paths = get_file_with_ext_from_path(folder_path, extensions)
        zip_from_files(file_paths, join(folder_path, file_name), int(quality))
        return

    zip_from_files(files_path, join(folder_path, file_name), int(quality))


def if_merge_pdfs(file_name, files_path, folder_path):
    if files_path == [""] or files_path == "":
        file_paths = get_file_with_ext_from_path(folder_path, "pdf")
        merge_pdfs(file_paths, join(folder_path, file_name))
        return

    merge_pdfs(files_path, join(folder_path, file_name))


def if_convert_png2jpg(files_path, folder_path):
    if files_path == [""] or files_path == "":
        file_paths = get_file_with_ext_from_path(folder_path, "png")
        for file in file_paths:
            convert_image(file, "png", folder_path, "jpg")
        return

    for file in files_path:
        convert_image(file, "png", folder_path, "jpg")


def if_convert_jpg2png(files_path, folder_path):
    if files_path == [""] or files_path == "":
        file_paths = get_file_with_ext_from_path(folder_path, "jpg")
        for file in file_paths:
            convert_image(file, "jpg", folder_path, "png")
        return

    for file in files_path:
        convert_image(file, "jpg", folder_path, "png")


def if_convert_svg2pdf(file_paths, folder_path):
    if file_paths == [""] or file_paths == "":
        file_paths = get_file_with_ext_from_path(folder_path, extensions=("svg"))
        for file in file_paths:
            convert_svg2pdf(file, folder_path)
        return

    for file in file_paths:
        convert_svg2pdf(file, folder_path)


def if_compress_images(files_path, folder_path, extensions, quality):
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
    if len(argv) > 1:
        args = get_args()
        print(args)
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
    window = sg.Window("Time Saver 2.0", layout, finalize=True)
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
