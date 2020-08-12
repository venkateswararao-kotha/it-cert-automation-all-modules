from PIL import Image
import os
from pathlib import Path


basepath = './images/'
'''
with os.scandir(basepath) as entries:
    for entry in entries:
        if entry.is_file():
            im = Image(entry)
            #new_im = im.resize((128,128))
            #new_im.save("/opt/icons/entry",'JPEG')
            im.rotate(90).resize((128,128)).save("/opt/icons/entry",'JPEG')


basepath = Path('/home/student-02-7ad3fd472f24/images/')
files_in_basepath = (entry for entry in basepath.iterdir() if entry.is_file())
for item in files_in_basepath:
    print(type(item), item)
    #print(item)
    #im = Image(item)
    #im.rotate(90).resize((128,128)).save("/opt/icons/entry",'JPEG')
'''

dirpath = './images'
files = [f for f in os.listdir(dirpath) if os.path.isfile(os.path.join(dirpath, f))]
#print(files)
os. chdir("./images")

for item in files:
    os. chdir("/home/student-02-7ad3fd472f24/images")
    #print(type(item), item)
    #print(item)
    im = Image.open(item)
    os.chdir("/opt/icons")
    im.rotate(90).resize((128,128)).save(item,'jpeg')

