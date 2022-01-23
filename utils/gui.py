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
            sg.Button("Pack into ZIP", key="pack_zip"),
            sg.Button("Merge PDFs", key="merge_pdfs"),
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
            sg.Button("Convert PNG to JPG", key="convert_png2jpg"),
            sg.Button("Convert JPG to PNG", key="convert_jpg2png"),
            sg.Button("Convert SVG to PDF", key="convert_svg2pdf"),
            # !TODO convert PDF to SVG button
            sg.Text("", size=(10, 0), expand_x=True),
        ]
    ],
    justification="center",
    expand_x=True,
)
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
