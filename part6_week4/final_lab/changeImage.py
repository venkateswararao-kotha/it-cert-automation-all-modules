#! /usr/bin/env python3

from io import BytesIO
from PIL import Image
import os
from pathlib import Path

dirpath = "/home/student-02-fa07f27c31e3/supplier-data/images"  # TODO
files = [f for f in os.listdir(dirpath) if os.path.isfile(os.path.join(dirpath, f))]
print(files)

from io import BytesIO
from PIL import Image, ImageFile

os.chdir("/home/student-02-fa07f27c31e3/supplier-data/images")
for item in files:
    print(item)
    im = Image.open(item)
    out = im.convert("RGB")
    #b = BytesIO()
    #im = Image.open(f)
    out = im.convert("RGB")
    item1 = item.split(".")[0]+".jpeg"
    #out.resize((600,400)).save(item,'jpeg')
    out.resize((600,400)).save(item1)
