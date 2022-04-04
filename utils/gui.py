import PySimpleGUI as sg

sg.theme("BlueMono")

column_1 = sg.Column(
    [
        [
            sg.Text("File name:", size=(20, 1), pad=(0, 0), justification="right"),
            sg.InputText(
                default_text="file",
                key="file_name",
                size=(40, 1),
                pad=((14, 0), (0, 0)),
                expand_x=True,
            ),
        ],
        [
            sg.Text(
                "Quality:", size=(20, 1), justification="right", pad=((0, 0), (10, 0))
            ),
            sg.Slider(
                range=(1, 100),
                default_value=30,
                orientation="h",
                key="quality",
                expand_x=True,
                size=(35, 15),
                pad=((15, 0), (0, 10)),
            ),
        ],
        [
            sg.FilesBrowse("Select files", target="file_path", size=(20, 1)),
            sg.InputText(
                key="file_path",
                expand_x=True,
                enable_events=True,
                size=(40, 1),
                pad=(0, 0),
            ),
        ],
        [
            sg.FolderBrowse("Destination folder", target="folder_path", size=(20, 1)),
            sg.InputText(
                key="folder_path",
                expand_x=True,
                enable_events=True,
                size=(40, 1),
                pad=(0, 0),
            ),
        ],
    ],
    vertical_alignment="center",
    justification="center",
    expand_x=True,
    expand_y=True,
)

button_row_1 = sg.Column(
    [
        [
            sg.Text("", expand_x=True),
            sg.Button("Pack into PDF", key="pack_pdf"),
            sg.Button("Merge PDFs", key="merge_pdfs"),
            sg.Button("Pack into ZIP", key="pack_zip"),
            sg.Button("Compress JPG and PNG", key="compress_images"),
            sg.Text("", expand_x=True),
        ],
    ],
    justification="center",
    expand_x=True,
)
button_row_2 = sg.Column(
    [
        [
            sg.Text("", size=(10, 0), expand_x=True),
            sg.Button("Convert SVG to PDF", key="convert_svg2pdf"),
            sg.Button("Convert JPG to PNG", key="convert_jpg2png"),
            sg.Button("Convert PNG to JPG", key="convert_png2jpg"),
            # !TODO convert PDF to SVG button
            sg.Text("", size=(10, 0), expand_x=True),
        ]
    ],
    justification="center",
    expand_x=True,
)
button_row_3 = sg.Column(
    [
        [
            sg.Text("", size=(10, 0), expand_x=True),
            sg.Button("Remove pdf password", key="remove_pdf_passwd"),
            sg.Button("Remove zip password", key="remove_zip_passwd"),
            sg.Text("", size=(10, 0), expand_x=True),
        ]
    ],
    justification="center",
    expand_x=True,
)
# !TODO add a row for adding a password to pdf or zip
# button_row_4 = sg.Column(
#     [
#         [
#             sg.Text("", size=(10, 0), expand_x=True),
#             sg.Button("Assign password to PDF", key="assign_pdf_passwd"),
#             sg.Button("Assign password to ZIP", key="assign_zip_passwd"),
#             sg.Text("", size=(10, 0), expand_x=True),
#         ],
#     ],
#     justification="center",
#     expand_x=True,
# )
# !TODO add a row for removal of metadata of images
# button_row_4 = sg.Column(
#     [
#         [
#             sg.Text("", size=(10, 0), expand_x=True),
#             sg.Button("Remove JPG EXIF data", key="remove_jpg_exif"),
#             sg.Button("Remove PNG EXIF data", key="remove_png_exif"),
#             sg.Text("", size=(10, 0), expand_x=True),
#         ]
#     ],
#     justification="center",
#     expand_x=True,
# )
chkbx_row = sg.Column(
    [
        [
            sg.Checkbox("JPG/JPEG", key="jpg_chkbx", enable_events=True, default=True),
            sg.Checkbox("PNG", key="png_chkbx", enable_events=True),
            sg.Checkbox("PDF", key="pdf_chkbx", enable_events=True),
            sg.Checkbox("SVG", key="svg_chkbx", enable_events=True),
        ]
    ],
    element_justification="center",
    vertical_alignment="center",
    expand_x=True,
)

layout = [
    [column_1],
    [button_row_1],
    [button_row_2],
    [button_row_3],
    # [button_row_4],
    [
        sg.Text(
            "Which files should be affected by the operation?",
            size=(40, 1),
            justification="center",
            expand_x=True,
        )
    ],
    [
        sg.Text(
            "This only has an effect if only destination folder is chosen and selected files box is empty.",
            size=(40, 1),
            justification="center",
            expand_x=True,
        )
    ],
    [chkbx_row],
]


def layout_passwd():
    pass_row = sg.Column(
        [
            [
                sg.Text("Name extension:", size=(20, 1), justification="left"),
                sg.InputText(
                    default_text="_no_passwd",
                    key="extension",
                    disabled_readonly_background_color="#222222",
                    enable_events=True,
                    size=(40, 1),
                    pad=((0, 0), (0, 0)),
                    expand_x=True,
                ),
            ],
            [
                sg.Text("Password:", size=(20, 1), justification="left"),
                sg.InputText(
                    key="password",
                    enable_events=True,
                    password_char="*",
                    size=(40, 1),
                    pad=((0, 0), (0, 0)),
                    expand_x=True,
                ),
            ],
            [sg.Button("Remove", key="remove_passwd")],
            [
                sg.Checkbox(
                    "Replace? ",
                    key="replace_file",
                    enable_events=True,
                )
            ],
            [
                sg.Text(
                    "If you check this box, after clicking on the remove button, the file will be overwritten.",
                    justification="center",
                )
            ],
        ],
        justification="center",
        element_justification="center",
        expand_x=True,
    )

    layout_pass = [[pass_row]]
    return layout_pass
