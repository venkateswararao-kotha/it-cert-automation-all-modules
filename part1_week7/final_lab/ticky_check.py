#!/usr/bin/env python3

import re
import operator

error_report = {}
user_report = {}

with open("syslog.log",'r') as f:
    for line in f.readlines():
        key_user = re.search(r"\([\w \.]*\)$", line)
        keyu = key_user.group().strip()
        keyu = keyu.replace("(","")
        keyu = keyu.replace(")","")
        #print(keyu)

        if "ERROR" in line.split():
            key_string = re.search(r"ERROR ([\w ]*) ", line)
            key = " ".join(key_string.group().split()[1:])
            if error_report.get(key):
                error_report[key] = error_report[key] + 1
            else:
                error_report[key] = 1

            if user_report.get(keyu):
                user_report[keyu].append("ERROR")
            else:
                user_report[keyu] = ["ERROR"]
        elif "INFO" in line.split():
            if user_report.get(keyu):
                user_report[keyu].append("INFO")
            else:
                user_report[keyu] = ["INFO"]


#print(error_report)
#print(sorted(error_report.items(), key=operator.itemgetter(1),reverse=True))
#print(user_report)

with open("error_message.csv","w") as fw:
    fw.write("Error, Count\n")
    for rec in sorted(error_report.items(), key=operator.itemgetter(1),reverse=True):
        fw.write('{0},{1}\n'.format(rec[0],rec[1]))


with open("user_statistics.csv","w") as fw:
    fw.write("Username, INFO, ERROR\n")
    for k,v in sorted(user_report.items()):
        fw.write('{0},{1},{2}\n'.format(k,v.count("INFO"),v.count("ERROR")))
