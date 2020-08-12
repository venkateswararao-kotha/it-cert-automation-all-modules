#!/bin/bash

'''
Qwiklabs Assessment: Editing Files Using Substrings

In this lab, you'll change the username of your coworker
Jane Doe from "jane" to "jdoe" in compliance with company's naming policy.
The username change has already been done. However, some files that were named
with Jane's previous username "jane" haven't been updated yet.

To help with this, you'll write a bash script and a Python script that will take care
of the necessary rename operations.

What you'll do

Practice using the cat, grep, and cut commands for file operations
Use > and >> commands to redirect I/O stream
Replace a substring using Python
Run bash commands in Python


we have to use this

subprocess.run(command,shell = True)
'''

#!/bin/bash

# this script runs first and identify the old files with Jane name in data folder
# and place the filenames with path in oldFiles.txt

> oldFiles.txt

files=`grep " jane " ../data/list.txt | cut -d ' ' -f3`
echo $files

for file in $files; do
	if test -e $HOME$file; then
		echo "$HOME$file" >> oldFiles.txt
	fi
done
