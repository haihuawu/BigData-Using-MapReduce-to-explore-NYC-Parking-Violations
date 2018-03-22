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

sorted_vehiclelist = sorted(dicVehicle.items(), key = lambda x:(-x[1], x[0]))

outputLen = 20
if len(dicVehicle) < 20:
    outputLen = len(dicVehicle)

for i in range(outputLen):
    print('{0:s}\t{1:d}'.format(sorted_vehiclelist[i][0], sorted_vehiclelist[i][1]))
