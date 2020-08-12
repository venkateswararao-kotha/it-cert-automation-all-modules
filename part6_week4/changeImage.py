from PIL import Image
import os
from pathlib import Path

dirpath = '~/supplier-data/images'
files = [f for f in os.listdir(dirpath) if os.path.isfile(os.path.join(dirpath, f))]
os. chdir("./images")
from io import BytesIO
from PIL import Image, ImageFile

ImageFile.LOAD_TRUNCATED_IMAGES = True

with open('broken.png', 'rb') as f:
    b = BytesIO()
    f.seek(15, 0)

    b.write(f.read())

    im = Image.open(b)
    im.load()


for item in files:
    os. chdir("/home/student-02-7ad3fd472f24/supplier-data/images")
    im = Image.open(item)
    out = im.convert("RGB")
    out.resize((600,400)).save(item,'jpeg')