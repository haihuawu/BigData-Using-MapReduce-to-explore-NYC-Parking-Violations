#!/usr/bin/python

import sys
import string
import os

fileName = os.environ.get('mapreduce_map_input_file')

for entry in sys.stdin:
    entry = entry.strip()
    try:
        if '"' in entry:
            summons_number, plate, value = entry.split('"',2)
            license_type = str(value.split(',',2)[1])
            amount_due = str(value.split(',',12)[11])
            print('{0:s}\t{1:s},{2:d}'.format(license_type, amount_due, 1))
        else:
            license_type = str(entry.split(',',3)[2])
            amount_due = str(entry.split(',',13)[12])
            print('{0:s}\t{1:s},{2:d}'.format(license_type, amount_due, 1))
    except:
        continue
