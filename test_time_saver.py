import pytest
import time_saver as ts
import os


def test_pdf_created():
    ts.pdf_from_images(
        ts.get_images_from_path("test_dir"), "test_dir\\test_file"
    )
    assert os.path.isfile("test_dir\\test_file.pdf")
    os.remove("test_dir\\test_file.pdf")


def test_zip_created():
    ts.zip_from_images(
        ts.get_images_from_path("test_dir"), "test_dir\\test_file"
    )
    assert os.path.isfile("test_dir\\test_file.zip")
    os.remove("test_dir\\test_file.zip")
