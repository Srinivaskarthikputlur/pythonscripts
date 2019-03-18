#!/usr/bin/python
# Usage
# ./spider.py <directory_path>


import os
import sys

for dirpath, subdirs, files in os.walk(sys.argv[1]):
    print (str(dirpath) + "/")
    for f in files:
        print (" "*len(dirpath) + "|-" +str(f))
