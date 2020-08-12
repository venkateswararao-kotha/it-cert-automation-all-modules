#! /usr/bin/env python3

import os
import requests
from pathlib import Path

dirpath = '/data/feedback'
files = [f for f in os.listdir(dirpath) if os.path.isfile(os.path.join(dirpath, f))]

os.chdir("/data/feedback")
for file in files:
    param_dict = dict()
    with open(file,'r') as f:
        param_dict['title'] = next(f).strip('\n')
        param_dict['name'] = next(f).strip('\n')
        param_dict['date'] = next(f).strip('\n')
        param_dict['feedback'] = next(f).strip('\n')
        #print(param_dict)
        #response = requests.post("http://35.222.164.1/feedback", data=param_dict)
        response = requests.post("http://35.222.164.1/feedback/", json=param_dict)
        print(response.status_code)
        print(response.text)
        print(response.ok)
        print(response.request.body)
        print(response.request.url)
        if not response.ok:
            response.raise_for_status()
