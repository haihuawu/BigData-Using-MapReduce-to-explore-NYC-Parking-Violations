#!/usr/bin/python

import sys
import string
 
# dictionary for parking violation except those opened
dicParking = {}

currentkey = None

for line in sys.stdin:

    line = line.strip()

    key, value = line.split('\t',1)
    flag, value = value.split(', ',1)

    key = int(key)
    flag = str(flag)
    value = str(value)

    if key==currentkey:
        if flag == 'open':
            dicParking.pop(key)
    else:
        if currentkey:
            if currentkey in dicParking:
                print('{0:d}\t{1:s}'.format(currentkey,dicParking[currentkey]))

        currentkey = key
        dicParking = {}

        if flag == 'parking':
            dicParking[key] = value

if currentkey in dicParking:
    print('{0:d}\t{1:s}'.format(currentkey,dicParking[currentkey]))

