import cv2 as cv
# print(cv.__version__)
import sys

img=cv.imread("C:\\Users\\Deepak\\OneDrive\\Desktop\\useful images\\s1.png")
if img is None:
    sys.exit("Could not open or find the image.")
    
cv.imshow("Display Window",img)
k=cv.waitKey(0)

if k==ord('s'):
    cv.imwrite("starry_night_copy.png",img)
    print("Image saved!")