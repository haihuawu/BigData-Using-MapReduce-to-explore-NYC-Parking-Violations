#!/usr/bin/python

import sys
import string
 
# dictionary for parking violation except those opened
current_count = 0
current_county = None

for line in sys.stdin:

    line = line.strip()
    county, count = line.split('\t',1)
    
    try:
        count = int(count)
    except:
        continue

    if current_county == county:
        current_count += count
    else:
        if current_county:
            print('{0:s}\t{1:d}'.format(current_county, current_count))

        current_county = county
        current_count = count

if current_county == county:
    print('{0:s}\t{1:d}'.format(current_county, current_count))

