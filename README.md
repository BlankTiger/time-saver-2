# Time Saver 2.0
Successor to Time Saver which I have written quite a while ago. It lacked some functionality and the code I wrote wasn't very clean. I decided to rewrite it.

# Inspiration
App inspired by the need to save time during tests, and exams. Allows to not waste time on compression and packaging of photos, when there is a need for fast delivery of them. Written completely in python. Currently works with jpegs, pngs, svgs, pdfs. Works only for windows (haven't tested linux support, but I doubt it works because of the way in which path handling has been done).

# Installation
Two options here, if you're running windows you can just run time_saver_2.exe downloaded from [] and it should work! It's compiled from time-saver.pyw with pyinstaller. If you want to do it yourself, you can just run `pyinstaller --icon=icon.ico time_saver.pyw` from within the main folder. To make the dist folder where the exe will appear a lot cleaner you could run `pyinstaller --icon=icon.ico --runtime-hook add_lib.py time_saver.pyw`. It will require you to move some of the files and folders into a lib folder though (not recommended if you don't know what you're doing). Compiled program will be found in the dist folder. Second option is to just run `pip install -r requirements.txt`, and open time-saver.pyw afterwards.

# Current features
- ability to either choose all the files ending with a certain extension or choose specific files;
- compression of jpeg and png images (you can choose the quality of compression);
- packing images into pdf;
- packing chosen files into zip;
- conversion of images PNG2JPG, JPG2PNG, SVG2PDF;
- merging pdfs.

# Current dependencies
- Pillow
- PyPDF4

<div>Icons made by <a href="https://www.flaticon.com/authors/vectors-market" title="Vectors Market">Vectors Market</a> from <a href="https://www.flaticon.com/" title="Flaticon">www.flaticon.com</a></div>