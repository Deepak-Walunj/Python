import cv2 as cv
import mediapipe as mp
import numpy as np

# Initialize MediaPipe Face Mesh
mp_face_mesh = mp.solutions.face_mesh
face_mesh = mp_face_mesh.FaceMesh(static_image_mode=False, max_num_faces=1, refine_landmarks=True, min_detection_confidence=0.5, min_tracking_confidence=0.5)

# Function to calculate gaze direction
def calculate_gaze(landmarks, image_width, image_height):
    # Eye landmarks: Left (33, 133) and Right (362, 263)
    left_eye = [landmarks[33], landmarks[133]]
    right_eye = [landmarks[362], landmarks[263]]

    # Calculate midpoints for each eye
    left_mid = np.mean(left_eye, axis=0)
    right_mid = np.mean(right_eye, axis=0)

    # Normalize points (0 to 1 scale)
    left_mid_normalized = (left_mid[0] / image_width, left_mid[1] / image_height)
    right_mid_normalized = (right_mid[0] / image_width, right_mid[1] / image_height)

    # Simple heuristic for gaze direction
    if left_mid_normalized[0] < 0.4 and right_mid_normalized[0] < 0.4:
        return "Looking Left"
    elif left_mid_normalized[0] > 0.6 and right_mid_normalized[0] > 0.6:
        return "Looking Right"
    elif left_mid_normalized[1] < 0.4 and right_mid_normalized[1] < 0.4:
        return "Looking Up"
    elif left_mid_normalized[1] > 0.6 and right_mid_normalized[1] > 0.6:
        return "Looking Down"
    else:
        return "Looking Center"

# Start webcam feed
cap = cv.VideoCapture(0, cv.CAP_DSHOW)

print("Starting Eye Gaze Tracking. Press 'q' to quit.")
while cap.isOpened():
    success, frame = cap.read()
    if not success:
        print("Failed to capture image. Exiting...")
        break

    # Flip and convert the image to RGB
    frame = cv.flip(frame, 1)
    rgb_frame = cv.cvtColor(frame, cv.COLOR_BGR2RGB)

    # Get image dimensions
    image_height, image_width, _ = frame.shape

    # Process the image with MediaPipe Face Mesh
    results = face_mesh.process(rgb_frame)

    if results.multi_face_landmarks:
        for face_landmarks in results.multi_face_landmarks:
            # Extract landmark coordinates
            landmarks = [
                (int(landmark.x * image_width), int(landmark.y * image_height))
                for landmark in face_landmarks.landmark
            ]

            # Visualize landmarks
            for x, y in landmarks:
                cv.circle(frame, (x, y), 1, (0, 255, 0), -1)

            # Calculate gaze direction
            gaze_direction = calculate_gaze(landmarks, image_width, image_height)
            cv.putText(frame, f"Gaze: {gaze_direction}", (10, 30), cv.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255), 2, cv.LINE_AA)

    # Display the output
    cv.imshow("Eye Gaze Tracking", frame)

    # Exit on pressing 'q'
    if cv.waitKey(1) & 0xFF == ord('q'):
        break

# Release resources
cap.release()
cv.destroyAllWindows()
face_mesh.close()
