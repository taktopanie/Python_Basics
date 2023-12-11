import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

import matplotlib.image as mpimg

import matplotlib
matplotlib.use('GTK3Cairo')

import cv2

import sys


longtitude = []
latitude = []

# total = 0 # variable to store total sum

with open('/home/maciej/Desktop/PUTTY.LOG') as file_object: # open file in a with statement
    #Skip the first line with no GPS data
    file_object.readline()

    for line in file_object:  # iterate line by line
        numbers = [float(e) for e in line.split()] # split line and convert string elements into int
        i = 0
        for number in numbers:
            if i == 0:
                latitude.append(number)

                i+=1
            else:
                longtitude.append(number)
file_object.close()


for i in range (len(latitude)):
    print(str(i) + " point is: " + str(longtitude[i]) + " " + str(latitude[i]) + '\n')

print("Latitude max: " + str(max(latitude)) + ", min Latitude :" + str(min(latitude)) + '\n')
print("Longtitude max: " + str(max(longtitude)) + ", min longtitude :" + str(min(longtitude)) + '\n')

## uncoment to resize for given measurements
# BBox = (min(longtitude), max(longtitude),
#          min(latitude), max(latitude))

BBox = (23.1928, 23.2982, 50.6875, 50.7482)

mapka = plt.imread('/home/maciej/Downloads/map.png')

fig, ax = plt.subplots(figsize = (20,20))
ax.scatter(longtitude, latitude, zorder=1, alpha= 0.5, c='r', s=10)

ax.set_title('Routemap printed on the MAP')

ax.set_xlim(BBox[0],BBox[1])
ax.set_ylim(BBox[2],BBox[3])

ax.imshow(mapka, zorder=0, extent = BBox, aspect= 'equal')

plt.show()