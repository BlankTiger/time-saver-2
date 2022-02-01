# Time Saver 2.0
Successor to <a href="https://github.com/BlankTiger/time-saver">Time Saver</a> which I have written quite a while ago. It lacked some functionality and the code I wrote wasn't very clean. I decided to rewrite it.

<p align="center"> <img style="width: 60%;" src="https://user-images.githubusercontent.com/16402420/150687170-98fc3bf8-b950-4c10-b489-1f74828a38ed.png"/> </p>

# Inspiration
App inspired by the need to save time during tests, and exams. Allows to not waste time on compression and packaging of photos, when there is a need for fast delivery of them. Written completely in python. Currently works with jpegs, pngs, svgs, pdfs. Works only for windows (haven't tested linux support, but I doubt it works because of the way in which path handling has been done).

# Installation
Two options here, if you're running windows you can just run time_saver.exe from the dist folder if you downloaded the whole repo, or you can run time_saver.exe from the files downloaded from <a href="https://github.com/BlankTiger/time-saver-2/releases">releases</a>, and it should work! It's compiled from time_saver.pyw with pyinstaller. If you want to do it yourself, you can just run `pyinstaller --icon=icon.ico time_saver.pyw` from within the main folder. To make the dist folder where the exe will appear a lot cleaner you could run `pyinstaller --icon=icon.ico --runtime-hook add_lib.py time_saver.pyw`. It will require you to move some of the files and folders into a lib folder though (not recommended if you don't know what you're doing). Compiled program will be found in the dist folder. Second option is to just run `pip install -r requirements.txt`, and open time_saver.pyw afterwards.

# Current features
- ability to either run in CLI or GUI mode. To run in CLI mode, just run it from the command line with -h argument and it will show you all the possible options;
- ability to either choose all the files ending with a certain extension or choose specific files;
- compression of jpeg and png images (you can choose the quality of compression);
- packing images into pdf;
- packing chosen files into zip;
- conversion of images PNG2JPG, JPG2PNG, SVG2PDF;
- merging pdfs.

# Command line options
```
usage: time_saver_2.pyw [-h] [-f FILES [FILES ...]] [-o OUTPUT] [-q QUALITY] [-e EXTENSIONS [EXTENSIONS ...]] [-p]
                        [-m] [-z] [-c] [-jp] [-pj] [-s]
                        destination

Convert images to other formats.

positional arguments:
  destination           The destination folder.

options:
  -h, --help            show this help message and exit
  -f FILES [FILES ...], --files FILES [FILES ...]
                        Path to the files to convert/zip/merge.
  -o OUTPUT, --output OUTPUT
                        Output file name.
  -q QUALITY, --quality QUALITY
                        Quality of the compression.
  -e EXTENSIONS [EXTENSIONS ...], --extensions EXTENSIONS [EXTENSIONS ...]
                        File extensions to convert.
  -p, --pack-to-pdf     Pack files to pdf.
  -m, --merge-pdfs      Merge pdfs.
  -z, --pack-to-zip     Zip files.
  -c, --compress        Compress images.
  -jp, --jpg2png        Convert jpg to png.
  -pj, --png2jpg        Convert png to jpg.
  -s, --svg2pdf         Convert svg to pdf.
```
# Current dependencies
- Pillow,
- PyPDF4,
- cairosvg,
- PySimpleGUI.

<div>Icons made by <a href="https://www.flaticon.com/authors/vectors-market" title="Vectors Market">Vectors Market</a> from <a href="https://www.flaticon.com/" title="Flaticon">www.flaticon.com</a></div>
