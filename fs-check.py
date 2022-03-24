import os, sys


def convert_bytes(num):
    """
    Convert a non-denominated value of bytes to a denominated value of bytes
    """
    step_unit = 1024.0 # Value to reach before incrementing denominators
    for x in ['B', 'KB', 'MB', 'GB', 'TB', 'PB']:
        if num < step_unit:
            return "%3.1f %s" % (num, x)
        num /= step_unit


Folderpath = sys.argv[1] # Take directory in

size = 0 # Create a var to hold the file size

for root, dirs, files in os.walk(Folderpath):
    for file_obj in files:
        size += os.stat(root + "/" + file_obj).st_size # Add each file's size together

print(convert_bytes(size))
