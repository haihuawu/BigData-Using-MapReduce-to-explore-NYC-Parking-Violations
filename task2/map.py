#!/usr/bin/python

import sys
import string
import os

fileName = os.environ.get('mapreduce_map_input_file')

for entry in sys.stdin:
    entry = entry.strip()
    try:
        violationCode = int(entry.split(',',3)[2])
        print('{0:d}\t{1:d}'.format(violationCode, 1))
    except:
        continue
