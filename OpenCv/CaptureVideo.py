import cv2 as cv
import sys
cam=cv.VideoCapture(0)
fourcc=cv.VideoWriter_fourcc(*'mp4v')
out = cv.VideoWriter('output.mp4', fourcc, 60.0, (640,  480))
if not cam.isOpened():                      #fps  frame size
    sys.exit('Cannt open video capture')
while True:
    ret,frame=cam.read()
    if not ret:
        print("Can't read frame")
        break
    # gray=cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    # frame = cv.flip(frame, 1)
    out.write(frame)
    cv.imshow("video",frame)
    if cv.waitKey(1)==ord("q"):
        break
cam.release()
out.release()
cv.destroyAllWindows()
    