'''
Imagine one of your colleagues has written a Python script that's failing to run correctly.
They're asking for your help to debug it. In this lab, you'll look into why the script is
crashing and apply the problem-solving steps that we've already learned to get information,
find the root cause, and remediate the problem.

'''


In order to check how much your program utilizes CPU, you first need to install the pip3
which is a Python package installer. This downloads and configures new Python modules
with single-line commands. For any pop-up messages, when the prompt Do you want to continue appears,
type ‘Y'.


sudo apt install python3-pip

psutil (process and system utilities) is a cross-platform library for retrieving information on running processes and system utilization (CPU, memory, disks, network, sensors) in Python. It's mainly useful for system monitoring, profiling, and limiting process resources and management of running processes. Install the psutil python library using pip3:

pip3 install psutil

# Now open python3 interpreter.
python3

# Import psutil python3 module for checking CPU usage as well as the I/O and network bandwidth.
import psutil
psutil.cpu_percent()

'''
This shows that CPU utilization is low. Here, you have a CPU with multiple cores; this means one fully loaded CPU thread/virtual core equals 1.2% of total load. So, it only uses one core of the CPU regardless of having multiple cores.

After checking CPU utilization, you noticed that they're not reaching the limit.

So, you check the CPU usage, and it looks like the script only uses a single core to run. But your server has a bunch of cores, which means the task is CPU-bound.

Now, using psutil.disk_io_counters() and psutil.net_io_counters() you'll get byte read and byte write for disk I/O and byte received and byte sent for the network I/O bandwidth. For checking disk I/O, you can use the following command:
'''

psutil.disk_io_counters()

# For checking the network I/O bandwidth:
psutil.net_io_counters()


#Basics rsync command

rsync [Options] [Source-Files-Dir] [Destination]
Options
Uses
-v
Verbose output
-q
Suppress message output
-a
Archive files and directory while synchronizing
-r
Sync files and directories recursively
-b
Take the backup during synchronization
-z
Compress file data during the transfer


1) Copy or sync files locally:
rsync -zvh [Source-Files-Dir] [Destination]

2) Copy or sync directory locally:
rsync -zavh [Source-Files-Dir] [Destination]

3) Copy files and directories recursively locally:
rsync -zrvh [Source-Files-Dir] [Destination]

