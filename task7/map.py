#!/usr/bin/env python
 
import sys
import os

fileName = os.environ.get("mapreduce_map_imput_file")

for line in sys.stdin:
    try:
        line = line.strip()
        entry = line.split(",")

        print("{0:s}\t{1:s},{2:d}".format(entry[2], entry[1], 1))
            
    except:
        continue

