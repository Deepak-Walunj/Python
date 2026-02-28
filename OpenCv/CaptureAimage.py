import cv2 as cv
import sys
try:
    cam=cv.VideoCapture(0)
    if not cam.isOpened():
        sys.exit("Can't open the camera")
    while True:
        try:
            ret, frame=cam.read()
            if not ret:
                sys.exit("Can't read")
                break
            cv.imshow("Camera Feed", frame)
            key=cv.waitKey(1)
            if key==13:
                cv.imwrite("Image.jpg",frame)
            elif key==27:
                sys.exit("Image captured and saved as 'Image.jpg'")
        except Exception as e:
            print(e)
except Exception as e:
    print(e)