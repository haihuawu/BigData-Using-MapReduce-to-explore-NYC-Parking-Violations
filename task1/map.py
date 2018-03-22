#!/usr/bin/python

import sys
import string
import os
from csv import reader

fileName = os.environ.get('mapreduce_map_input_file')

for entry in reader(sys.stdin):

    if 'parking' in fileName:
        try:
            summberNumber = int(entry[0])
            issueDate = str(entry[1])
            violationCode = int(entry[2])
            violationPrecinct = int(entry[6])
            plateId = str(entry[14])

            print('{0:d}\t{1:s}, {2:s}, {3:d}, {4:d}, {5:s}'.format(summberNumber, "parking", plateId, violationPrecinct, violationCode, issueDate))
        except:
            continue

    if 'open' in fileName:
        try:
            summberNumber = int(entry[0])
            print('{0:d}\t{1:s}, none'.format(summberNumber, "open"))
	except:
            continue
