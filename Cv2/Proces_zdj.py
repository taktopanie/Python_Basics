import numpy as np
import cv2 as cv
import time 


#y=np.array([[0, 0,255,0,0], [0, 255, 255,255,0],[255,255,255,255,255], [255,255,255,255,255], [1,1,1,0,0]], np.uint8)
img = np.zeros((512,512,3), np.uint8)

cv.line(img,(0,0),(511,511),[0,0,255],5)

cv.rectangle(img,(10,10),(400,400),[255,0,0],10)

cv.circle(img, (200,200),100,[0,255,0],5)

cv.imshow('img',img)

cv.waitKey(0)

