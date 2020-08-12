#! /usr/bin/env python3

import os
import requests
from pathlib import Path

dirpath = '~/supplier-data/images'
files = [f for f in os.listdir(dirpath)
         if os.path.isfile(os.path.join(dirpath, f)) and
            f.endswith('.' + 'jpeg')]
print(files)
os.chdir("~/supplier-data/images")
url = "http://35.222.164.1/upload" # TODO


for file in files:
    with open(file,'rb') as f:
        response = requests.post(url, files={'file':opened})
        if not response.ok:
            response.raise_for_status()