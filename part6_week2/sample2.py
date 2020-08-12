#! /usr/bin/env python3

import os
from pathlib import Path

dirpath = '/data/feedback'
files = [f for f in os.listdir(dirpath) if os.path.isfile(os.path.join(dirpath, f))]

os.chdir("/data/feedback")
for file in files:
    param_dict = dict()
    with open(file,'r') as f:
        param_dict['title'] = next(f).strip
        param_dict['name'] = next(f)
        param_dict['date'] = next(f)
        param_dict['feedback'] = next(f)
        print(param_dict)

        response = requests.post("https://35.222.164.1/feedback", data=param_dict)
        print(response.status)
        if not response.ok:
            Response.raise_for_status()

