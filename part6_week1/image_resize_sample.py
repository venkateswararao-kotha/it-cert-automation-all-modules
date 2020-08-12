'''
For example, if we wanted to resize an image and save the new image with a new name,
we could do it with:
'''
from PIL import Image
im = Image("example.jpg")
new_im = im.resize((640,480))
new_im.save("example_resized.jpg")

'''
if we want to rotate an image, we can use code like this:
'''

from PIL import Image
im = Image("example.jpg")
new_im = im.rotate(90)
new_im.save("example_rotated.jpg")

'''
This method also returns a new image that we can then use to create the new rotated file. 
Because the methods return a new object, we can even combine these operations into 
just one line that rotates, resizes, and saves:
'''

from PIL import Image
im = Image("example.jpg")
im.rotate(180).resize((640,480)).save("flipped_and_resized.jpg")

# Note: to save a file in specific directory and JPEG format
img.save('/absolute/path/to/myphoto.jpg', 'JPEG')
'''
For More Information Use Below

https://pillow.readthedocs.io/en/stable/handbook/tutorial.html
'''


'''
List all files in a directory using scandir()
An easier way to list files in a directory is to use os.scandir() or pathlib.Path():
'''

import os

basepath = 'my_directory/'
with os.scandir(basepath) as entries:
    for entry in entries:
        if entry.is_file():
            print(entry.name)

# The modified version looks like this: using generator expression

from pathlib import Path

# List all files in directory using pathlib
basepath = Path('my_directory/')
files_in_basepath = (entry for entry in basepath.iterdir() if entry.is_file())
for item in files_in_basepath:
    print(item.name)

# glob makes it easy to search for files recursively in subdirectories too:

import glob
for file in glob.iglob('**/*.py', recursive=True):
    print(file)

# Simple Filename Pattern Matching Using fnmatch
import os
import fnmatch

for file_name in os.listdir('some_directory/'):
    if fnmatch.fnmatch(file_name, '*.txt'):
        print(file_name)
