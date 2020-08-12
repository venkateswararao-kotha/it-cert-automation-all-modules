#!/usr/bin/env python3

import sys
import subprocess
# this script runs after findJane.sh and replace jane with jdoe in file names in data folder

# move the file /home/student-00-b78cd5306b72/data/jane_profile_07272018.doc to
# /home/student-00-b78cd5306b72/data/jdoe_profile_07272018.doc

# move this file /home/student-00-b78cd5306b72/data/jane_contact_07292018.csv to
# /home/student-00-b78cd5306b72/data/jdoe_contact_07292018.csv

#!/usr/bin/env python3
import sys
import subprocess

'''
# below script written by others and looks pretty good than my script
my script is shown below uncommented

with open(sys.argv[1]) as f:
  for line in f.readlines():
    old_name = line.strip()
    new_name = old_name.replace('jane', 'jdoe')
    subprocess.run(['mv', old_name, new_name])
'''

with open(sys.argv[1], 'r') as file_input:
  old_file_names_list = file_input.readlines()
  for old_file_name in old_file_names_list:
    new_file_name = old_file_name.strip().replace("jane", "jdoe")
    old_file_name_nonl = old_file_name.strip()
    print(old_file_name_nonl, new_file_name)
    subprocess.run(["mv", old_file_name_nonl, new_file_name])