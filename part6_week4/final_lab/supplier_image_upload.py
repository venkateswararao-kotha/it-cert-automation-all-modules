#! /usr/bin/env python3

import os
import requests
from pathlib import Path

dirpath = "/home/student-02-fa07f27c31e3/supplier-data/images" #TODO
files = [f for f in os.listdir(dirpath)
           if os.path.isfile(os.path.join(dirpath, f)) and
              f.endswith('.' + 'jpeg')]
print(files)
os.chdir("/home/student-02-fa07f27c31e3/supplier-data/images")
url = "http://35.239.89.170/upload/" # TODO


for file in files:
    with open(file,'rb') as opened:
        response = requests.post(url, files={'file':opened})
        if not response.ok:
            response.raise_for_status()
