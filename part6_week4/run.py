#! /usr/bin/env python3

import os
import requests
from pathlib import Path

dirpath = '/home/student-02-fa07f27c31e3/supplier-data/descriptions/'   # TODO
files = [f for f in os.listdir(dirpath) if os.path.isfile(os.path.join(dirpath, f))]

os.chdir("/home/student-02-fa07f27c31e3/supplier-data/descriptions/")
for file in files:
    param_dict = dict()
    with open(file,'r') as f:
        param_dict['name'] = next(f).strip('\n')
        param_dict['weight'] = int(next(f).strip('\n').split()[0])
        param_dict['description'] = next(f).strip('\n')
        param_dict['image_name'] = file.strip('\n').split(".")[0] + '.jpeg' # TODO how to get image name for product
        response = requests.post("http://35.239.89.170/fruits/", json=param_dict) #TODO
        #print(response.status_code)
        #print(response.text)
        #print(response.ok)
        #print(response.request.body)
        #print(response.request.url)
        if not response.ok:
            response.raise_for_status()
