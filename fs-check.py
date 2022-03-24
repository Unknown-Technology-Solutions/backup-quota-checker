import os, sys


def convert_bytes(num):
    step_unit = 1024.0
    for x in ['B', 'KB', 'MB', 'GB', 'TB', 'PB']:
        if num < step_unit:
            return "%3.1f %s" % (num, x)
        num /= step_unit


Folderpath = sys.argv[1] # Take directory in

size = 0
for ele in os.scandir(Folderpath):
    size += os.stat(ele).st_size

print(convert_bytes(size))
