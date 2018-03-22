#!/usr/bin/python

import sys
import string
import os

fileName = os.environ.get('mapreduce_map_input_file')

for entry in sys.stdin:
    entry = entry.strip()
    try:
        plate_id = str(entry.split(',',15)[14])
        registration_state = str(entry.split(',',17)[16])
        
        print('{0:s}, {1:s}\t{2:d}'.format(plate_id, registration_state, 1))
    except:
        continue
