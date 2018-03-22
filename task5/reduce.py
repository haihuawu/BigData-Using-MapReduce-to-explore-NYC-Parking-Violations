#!/usr/bin/python

import sys
import string
 
# dictionary for parking violation except those opened
current_count = 0
current_vehicle = None
dicVehicle = {}

for line in sys.stdin:

    line = line.strip()
    vehicle, count = line.split('\t',1)
    
    try:
        count = int(count)
    except:
        continue

    if current_vehicle == vehicle:
        current_count += count
    else:
        if current_vehicle:
            dicVehicle[current_vehicle] = current_count

        current_vehicle = vehicle
        current_count = count

if current_vehicle == vehicle:
    dicVehicle[current_vehicle] = current_count

maxVehicle = max(dicVehicle.items(), key=lambda x:x[1])
print('{0:s}\t{1:d}'.format(maxVehicle[0], maxVehicle[1]))
    
