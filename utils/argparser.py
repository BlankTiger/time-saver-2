import argparse


def get_args():
    """Create a parser for command line arguments."""
    parser = argparse.ArgumentParser(description="Convert images to other formats.")
    parser.add_argument(
        "destination",
        metavar="destination",
        type=str,
        help="The destination folder.",
    )
    parser.add_argument(
        "-f",
        "--files",
        help="Path to the files to convert/zip/merge.",
        nargs="+",
        default="",
    )
    parser.add_argument(
        "-o",
        "--output",
        help="Output file name.",
        default="file",
    )
    parser.add_argument(
        "-q",
        "--quality",
        help="Quality of the compression.",
        default=30,
        type=int,
    )
    parser.add_argument(
        "-e",
        "--extensions",
        help="File extensions to convert.",
        nargs="+",
        default=["jpg", "jpeg"],
    )
    parser.add_argument(
        "-p",
        "--pack-to-pdf",
        help="Pack files to pdf.",
        action="store_true",
    )
    parser.add_argument(
        "-m",
        "--merge-pdfs",
        help="Merge pdfs.",
        action="store_true",
    )
    parser.add_argument(
        "-z",
        "--pack-to-zip",
        help="Zip files.",
        action="store_true",
    )
    parser.add_argument(
        "-c",
        "--compress",
        help="Compress images.",
        action="store_true",
    )
    parser.add_argument(
        "-jp",
        "--jpg2png",
        help="Convert jpg to png.",
        action="store_true",
    )
    parser.add_argument(
        "-pj",
        "--png2jpg",
        help="Convert png to jpg.",
        action="store_true",
    )
    parser.add_argument(
        "-s",
        "--svg2pdf",
        help="Convert svg to pdf.",
        action="store_true",
    )

    return parser.parse_args()
