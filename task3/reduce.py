#!/usr/bin/python

import sys
import string
 
# dictionary for parking violation except those opened
current_license = None
current_count = 0
total_amount = 0.00
license = None

for line in sys.stdin:

    line = line.strip()
    license, value = line.split('\t',1)
    amount, count = value.split(',',1)
    
    try:
        license = str(license)
        count = int(count)
	amount = float(amount)
    except:
        continue

    if current_license == license:
        total_amount += amount
        current_count += count
    else:
        if current_license:
            print('{0:s}\t{1:.2f}, {2:.2f}'.format(current_license, total_amount, float(total_amount/current_count)))

        current_count = count
        current_license = license
        total_amount = amount

if current_license == license:
    print('{0:s}\t{1:.2f}, {2:.2f}'.format(current_license, total_amount, float(total_amount/current_count)))

