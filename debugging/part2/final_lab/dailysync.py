#!/usr/bin/env python
import os
import subprocess
from multiprocessing import Pool

'''
Now, when you go through the hierarchy of the subfolders of /data/prod, data is from different projects 
(e.g., , beta, gamma, kappa) and they're independent of each other. So, in order to efficiently back up 
parallelly, use multiprocessing to take advantage of the idle CPU cores. Initially, 
because of CPU bound, the backup process takes more than 20 hours to finish, which isn't 
efficient for a daily backup. Now, by using multiprocessing, you can back up your data 
from the source to the destination parallelly by utilizing the multiple cores of the CPU.

run the parallel 
'''

def run(folder):
    src = "/home/student-02-d6c48599806a/data/prod/{}".format(folder)
    #dest = print("/data/prod_backup/{}".folder(folder))
    dest = "/home/student-02-d6c48599806a/data/prod_backup/"
    subprocess.call(["rsync", "-zavh", src, dest])
    #print(src, dest)


if __name__ == "__main__":
    path = "/home/student-02-d6c48599806a/data/prod"

    dname = []
    # we need to fix below line to just capture the dirs under /data/prod and not subdirs
    for root,d_names,f_names in os.walk(path,topdown=True, onerror=None, followlinks=False):
        #dname.append(os.path.join(root, d_names))
        dname.append(d_names)

    # just list the directories under ~/data/prod folder and don't list sub directories
    final_sub_dirs = dname[0]
    #print(final_sub_dirs)
    # Create a pool of specific number of CPUs
    p = Pool(len(final_sub_dirs))
    # Start each task within the pool
    p.map(run, final_sub_dirs)

