import PySimpleGUI as sg
import platform
from utils.image_tools import pdf_from_images, zip_from_images, merge_pdfs
from utils.file_tools import get_images_from_path
from utils.file_tools import file_paths_from_gui
from utils.validation import validate_file_extensions
from os import getcwd
from os.path import join
from utils.gui import layout

if platform.system() == "Windows":
    import ctypes

    if platform.release() == "7":
        ctypes.windll.user32.SetProcessDPIAware()
    elif float(platform.release()) >= 8:
        ctypes.windll.shcore.SetProcessDpiAwareness(1)


if __name__ == "__main__":
    # images = get_images_from_path("test_dir")
    # print(images)
    # pdf_from_images(images, "test_dir\\images")
    # zip_from_images(images, "test_dir\\images")
    window = sg.Window("Time Saver 2.0", layout, finalize=True)
    window["folder_path"].update(getcwd())

    current_extensions = ["jpg", "jpeg"]
    jpg_set = frozenset(("jpg", "jpeg"))
    while True:
        event, values = window.read()
        if event == "file_path":
            window["file_path"].update(values["file_path"].replace("/", "\\"))

        if event == "folder_path":
            window["folder_path"].update(
                values["folder_path"].replace("/", "\\")
            )

        if event == "pack_pdf" and (
            validate_file_extensions(
                file_paths_from_gui(values["file_path"]), current_extensions
            )
            or values["file_path"] == ""
        ):
            if not values["file_path"] == "":
                file_paths = file_paths_from_gui(values["file_path"])
                pdf_from_images(
                    file_paths,
                    join(values["folder_path"], values["file_name"]),
                    int(values["quality"]),
                )
            file_paths = get_images_from_path(
                values["folder_path"], current_extensions
            )
            pdf_from_images(
                file_paths,
                join(values["folder_path"], values["file_name"]),
                int(values["quality"]),
            )

        if event == "merge_pdfs" and validate_file_extensions(
            file_paths_from_gui(values["file_path"]), "pdf"
        ):
            file_paths = file_paths_from_gui(values["file_path"])
            merge_pdfs(
                file_paths, join(values["folder_path"], values["file_name"])
            )
        # if event == "zip_images" and validate_file_extensions("jpg"

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

        print(current_extensions)

        if event in (None, "Exit"):
            break
