#!/usr/bin/env python
 
import sys
import os
from csv import reader

fileName = os.environ.get("mapreduce_map_imput_file")

for line in reader(sys.stdin):
    try:
        # 0 for make 1 for color
        maker = line[20]
        if maker == '':
            maker = 'NONE'

        color = line[19]
        if color == '':
            color = 'NONE'
    
        print('{0:d},{1:s}\t{2:d}'.format(0, maker, 1))
        print('{0:d},{1:s}\t{2:d}'.format(1, color, 1))
            
    except:
        continue

