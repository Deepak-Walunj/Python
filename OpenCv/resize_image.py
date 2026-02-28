import cv2 as cv

def main():
    width, height= 640,480
    cam= cv.VideoCapture(0, cv.CAP_DSHOW)
    cam.set(cv.CAP_PROP_FRAME_WIDTH, width)
    cam.set(cv.CAP_PROP_FRAME_HEIGHT, height)
    cam.set(cv.CAP_PROP_FPS, 90)
    cam.set(cv.CAP_PROP_FOURCC, cv.VideoWriter_fourcc(*'MJPG'))
    if not cam.isOpened():
        print('Error opening the camera')
    
    while True:
        ret ,frame=cam.read()
        if not ret:
            print("Error: Unable to read from the camera")
            break
        cv.imshow("frame", frame)
        key=cv.waitKey(1)
        if key==13:
            frame=cv.resize(frame, (320,320))
            cv.imwrite('captured_image.jpg', frame)
            print("Photo saved as 'captured_image.jpg'")
        elif key==27:
            print('Exiting')
            break
    cam.release()
    cv.destroyAllWindows()
    
if __name__ == '__main__':
    main()