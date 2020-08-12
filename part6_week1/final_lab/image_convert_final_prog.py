from PIL import Image
import os
from pathlib import Path

dirpath = './images'
files = [f for f in os.listdir(dirpath) if os.path.isfile(os.path.join(dirpath, f))]
os. chdir("./images")

for item in files:
    os. chdir("/home/student-02-7ad3fd472f24/images")
    im = Image.open(item)
    out = im.convert("RGB")
    os.chdir("/opt/icons")
    #im.rotate(90).resize((128,128)).convert('RGB').save(item,'JPEG')
    out.rotate(90).resize((128,128)).save(item,'JPEG')
    #im.close()
