import cv2 as cv
import numpy as np
flags = [i for i in dir(cv) if i.startswith('COLOR_')]
# print(flags)
cam=cv.VideoCapture(0, cv.CAP_DSHOW)
while True:
    _, frame=cam.read()
    
    ################################ HSV_CONVERSION & OBJECT DETECTION ################################
    
    # hsv=cv.cvtColor(frame,cv.COLOR_BGR2HSV)
    # lower_b = np.array([35, 50, 50])  # Adjust based on lighting
    # upper_b = np.array([85, 255, 255])
    # mask=cv.inRange(hsv,lower_b,upper_b)
    # res=cv.bitwise_and(frame, frame ,mask=mask)
    # cv.imshow('frame',frame)
    # cv.imshow('mask', mask)
    # cv.imshow('res', res)
    # if cv.waitKey(1)==ord("q"):
    #     break

    gray_frame=cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    # resized_frame = cv.resize(gray_frame, (720, 680), interpolation = cv.INTER_CUBIC)
    cv.imshow('Frame', gray_frame)
    key =cv.waitKey(1)
    if key ==13:
        cv.imwrite('test6.jpg', gray_frame)
    elif key==27:
        print('Exiting')
        break

cam.release()
cv.destroyAllWindows()