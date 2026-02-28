import cv2 as cv
import matplotlib.pyplot as plt
def imageTakenAndReturned():
    cam = cv.VideoCapture(0, cv.CAP_DSHOW)
    width,height=640,480
    cam.set(cv.CAP_PROP_FRAME_WIDTH, width)
    cam.set(cv.CAP_PROP_FRAME_HEIGHT, height)
    cam.set(cv.CAP_PROP_FPS, 90)
    cam.set(cv.CAP_PROP_FOURCC, cv.VideoWriter_fourcc(*'MJPG'))
    if not cam.isOpened():
        print("Error: Unable to access the camera")
        return

    face_cascade = cv.CascadeClassifier(cv.data.haarcascades + 'haarcascade_frontalface_default.xml')
    
    while True:
        ret, frame = cam.read()
        if not ret:
            print("Error: Unable to read from the camera")
            break
        clean_frame= frame.copy()
        height, width, _ = frame.shape
        font_scale = 0.5  
        thickness = 2
        top_left_x = int(width * 0.05)
        top_left_y = int(height * 0.05)
        bottom_right_x = int(width * 0.6)
        bottom_right_y = int(height * 0.9)
        
        box_x, box_y, box_w, box_h = int(width * 0.3), int(height * 0.2), int(width * 0.4), int(height * 0.6)
        cv.putText(frame, "Press 'ENTER' to capture photo when your face is inside the box", 
                    (top_left_x, top_left_y), cv.FONT_HERSHEY_SIMPLEX, font_scale, (255, 255, 255), thickness)
        cv.putText(frame, "Press 'ESC' to quit", 
                   (top_left_x, top_left_y + int(height * 0.03)), cv.FONT_HERSHEY_SIMPLEX, font_scale, (255, 255, 255), thickness)
        cv.rectangle(frame, (box_x, box_y), (box_x + box_w, box_y + box_h), (0, 0, 255), 2)

        # Detect faces in the frame
        faces = face_cascade.detectMultiScale(frame, 1.3, 5)
        face_inside_box = False
        for (x, y, w, h) in faces:
            if x > box_x and y > box_y and (x + w) < (box_x + box_w) and (y + h) < (box_y + box_h):
                face_inside_box = True
                cv.putText(frame, "Face detected inside the box", 
                           (top_left_x, top_left_y + int(height * 0.08)), cv.FONT_HERSHEY_SIMPLEX, font_scale, (0, 255, 0), thickness)
                break
            else:
                cv.putText(frame, "Face not in the box", 
                           (top_left_x, top_left_y + int(height * 0.08)), cv.FONT_HERSHEY_SIMPLEX, font_scale, (0, 0, 255), thickness)

        cv.imshow("Camera", frame)
        key = cv.waitKey(1)
        if key == 13:  # Enter key
            if face_inside_box:
                cv.putText(frame, "Photo taken successfully", 
                        (bottom_right_x, bottom_right_y), cv.FONT_HERSHEY_SIMPLEX, font_scale, (0, 255, 0), thickness)
                cv.imwrite('test13.jpg', clean_frame)
                print("Photo saved as 'captured_image.jpg'")
                return clean_frame
            else:
                cv.putText(frame, "Face must be inside the box", 
                   (bottom_right_x, bottom_right_y + int(height * 0.03)), cv.FONT_HERSHEY_SIMPLEX, font_scale, (0, 0, 255), thickness)
                print("Face must be inside the box to capture the photo")
            cv.imshow("Camera", frame)
            cv.waitKey(2000)
        elif key == 27:  # ESC key
            print("Exiting the program")
            break

    cam.release()
    cv.destroyAllWindows()

def main():
    frame=imageTakenAndReturned()
    plt.title("Image taken and returned")
    plt.imshow(frame)
    plt.show()
if __name__ == '__main__':
    main()


######################################### Limitations ################################

# Lighting Conditions:
# Bright or dim lighting can cause the face detection to fail.
# Recommendation: Include prompts to guide students to use appropriate lighting, e.g., "Ensure a well-lit environment."

# Face Alignment:
# Tilted faces or partially visible faces may not be detected.
# Recommendation: Add instructions like "Keep your face straight and fully visible inside the box."

# Background Clutter:
# Busy or cluttered backgrounds might interfere with face detection.
# Recommendation: Ask users to sit against a plain background.

# Pose Variation:
# The model may fail if the user turns their head significantly.
# Recommendation: Specify that the user should look directly into the camera.