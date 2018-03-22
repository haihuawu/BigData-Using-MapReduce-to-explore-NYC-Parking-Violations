#!/usr/bin/python

import sys
import string
 
# dictionary for parking violation except those opened
current_key = None
current_count = 0

for line in sys.stdin:

    line = line.strip()
    key, count = line.split('\t',1)

    try:
        count = int(count)
        key = str(key)
    except:
        continue

    if current_key == key:
        current_count += count
    else:
        if current_key:
            column_name, term = current_key.split(',',1)

            if column_name == '0':
                print('{0:s}\t{1:s}, {2:d}'.format('vehicle_make', term, current_count))
            else:
                print('{0:s}\t{1:s}, {2:d}'.format('vehicle_color', term, current_count))

        current_key = key
        current_count = count


if current_key == key:
    column_name, term = current_key.split(',',1)

    if column_name == '0':
        print('{0:s}\t{1:s}, {2:d}'.format('vehicle_make', term, current_count))
    else:
        print('{0:s}\t{1:s}, {2:d}'.format('vehicle_color', term, current_count)) 
