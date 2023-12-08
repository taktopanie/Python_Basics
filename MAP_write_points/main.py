import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

import matplotlib.image as mpimg

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

BBox = (23.2239, 23.2913, 50.7302, 50.7536)

mapka = mpimg.imread('/home/maciej/Downloads/map.png')

pts = np.array([[330,620],[950,620],[692,450],[587,450]])

#plt.plot(640, 570, "og", markersize=10)  # og:shorthand for green circle
# plt.scatter(pts[:, 0], pts[:, 1], marker="x", color="red", s=200)

#fig, ax = plt.subplots(figsize = (8,7))
mapka = cv2.circle(mapka, (50, 50), radius=10, color=(0, 0, 255), thickness=-1)

# ax.scatter(longtitude, latitude, zorder=1, alpha= 0.2, c='b', s=10)
# ax.set_title('Plotting Spatial Data on Riyadh Map')
# ax.set_xlim(BBox[0],BBox[1])
# ax.set_ylim(BBox[2],BBox[3])

# ax.imshow(mapka, zorder=0, extent = BBox, aspect= 'equal')

# my_image = mpimg.imread("/content/drive/MyDrive/kote-puerto-so5nsYDOdxw-unsplash.jpg")

#plt.imshow(mapka)

#img_read = cv2.imread('/home/maciej/Downloads/map.png')
cv2.imshow('itslinuxfoss',mapka)
cv2.waitKey(0)
cv2.destroyAllWindows()