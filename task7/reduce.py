#!/usr/bin/python

import sys
import string
 
# dictionary for parking violation except those opened
current_week_count = 0
current_weekend_count = 0
current_code = None
weekendlist = ['2016-03-05', '2016-03-06', '2016-03-12', '2016-03-13', '2016-03-19',
               '2016-03-20', '2016-03-26', '2016-03-27']
for line in sys.stdin:
    line = line.strip()
    code, value = line.split('\t',1)
    date, count = value.split(',',1)
    
    try:
        code = str(code)
        count = int(count)
        date = str(date)
    except:
        continue

    if current_code == code:
        if date in weekendlist:
            current_weekend_count  += count
        else:
            current_week_count += count
    else:
        if current_code:
            print('{0:s}\t{1:.2f}, {2:.2f}'.format(current_code, float(current_weekend_count/8.0), float(current_week_count/23.0)))
            current_weekend_count = 0
            current_week_count = 0

        current_code = code

        if date in weekendlist:
            current_weekend_count = count
        else:
            current_week_count = count
        
if current_code == code:
    print('{0:s}\t{1:.2f}, {2:.2f}'.format(current_code, float(current_weekend_count/8.0), float(current_week_count/23.0)))

