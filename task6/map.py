#!/usr/bin/python

import sys
import string
import os
from csv import reader

fileName = os.environ.get('mapreduce_map_input_file')

for entry in reader(sys.stdin):
    try:
        plate_id = entry[14]
        registration_state = entry[16]
        
        print('{0:s}, {1:s}\t{2:d}'.format(plate_id, registration_state, 1))
    except:
        continue
