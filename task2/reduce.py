#!/usr/bin/python

import sys
import string
 
# dictionary for parking violation except those opened
current_code = None
current_count = 0
code = None

for line in sys.stdin:

    line = line.strip()
    code, count = line.split('\t',1)

    try:
        count = int(count)
    except:
        continue

    if current_code == code:
        current_count += count
    else:
        if current_code:
            print('{0:s}\t{1:d}'.format(current_code, current_count))

        current_count = count
        current_code = code

if current_code == code:
    print('{0:s}\t{1:d}'.format(current_code, current_count))

