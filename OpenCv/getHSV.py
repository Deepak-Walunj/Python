import numpy as np
import cv2 as cv
color=np.uint8([[[0,50,25],[150,255,200]]])
hsv_color=cv.cvtColor(color, cv.COLOR_BGR2HSV)
print(hsv_color)