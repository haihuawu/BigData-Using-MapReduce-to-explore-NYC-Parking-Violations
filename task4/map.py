#!/usr/bin/python

import sys
import string
import os
from csv import reader

fileName = os.environ.get('mapreduce_map_input_file')

for line in reader(sys.stdin):
    try:
        registration_state = line[16]
        if registration_state != 'NY':
            print('{0:s}\t{1:d}'.format("Other",1))
        else:
            print('{0:s}\t{1:d}'.format(registration_state, 1))
    except:
        continue
