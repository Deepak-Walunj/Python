import cv2
import mediapipe as mp
import numpy as np

class EyeTracker:
    def __init__(self):
        # MediaPipe Face Mesh initialization
        self.mp_face_mesh = mp.solutions.face_mesh
        self.face_mesh = self.mp_face_mesh.FaceMesh(
            min_detection_confidence=0.5, 
            min_tracking_confidence=0.5,
            refine_landmarks=True
        )

        # Left eye key landmarks
        self.LEFT_EYE_CENTER_IDX = 468  # Refined mesh iris center
        self.LEFT_EYE_CORNER_LEFT = 33   # Left eye outer corner
        self.LEFT_EYE_CORNER_RIGHT = 133 # Left eye inner corner

        # Right eye key landmarks
        self.RIGHT_EYE_CENTER_IDX = 473  # Refined mesh iris center
        self.RIGHT_EYE_CORNER_LEFT = 263  # Right eye inner corner
        self.RIGHT_EYE_CORNER_RIGHT = 362 # Right eye outer corner

        # Tracking variables
        self.left_eye_position = 0.0
        self.right_eye_position = 0.0

    def calculate_eye_position(self, landmarks, img_width, eye_center_idx, 
                                corner_left_idx, corner_right_idx):
        """
        Calculate eye position relative to eye corners
        
        Args:
            landmarks: Face mesh landmarks
            img_width: Width of the image
            eye_center_idx: Landmark index for eye center
            corner_left_idx: Landmark index for left eye corner
            corner_right_idx: Landmark index for right eye corner
        
        Returns:
            Float representing eye position
        """
        # Get eye center and corner landmarks
        eye_center = landmarks[eye_center_idx]
        corner_left = landmarks[corner_left_idx]
        corner_right = landmarks[corner_right_idx]

        # Convert to pixel coordinates
        eye_center_x = int(eye_center.x * img_width)
        corner_left_x = int(corner_left.x * img_width)
        corner_right_x = int(corner_right.x * img_width)

        # Calculate eye width and center
        eye_width = corner_right_x - corner_left_x
        eye_mid_x = (corner_left_x + corner_right_x) / 2

        # Normalize eye position
        # Positive means looking right, negative means looking left
        position = (eye_center_x - eye_mid_x) / (eye_width / 2)

        return position

    def track_eyes(self):
        cap = cv2.VideoCapture(0)

        while cap.isOpened():
            success, image = cap.read()
            if not success:
                break

            # Preprocessing
            image = cv2.cvtColor(cv2.flip(image, 1), cv2.COLOR_BGR2RGB)
            image.flags.writeable = False
            results = self.face_mesh.process(image)
            image.flags.writeable = True
            image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

            if results.multi_face_landmarks:
                for face_landmarks in results.multi_face_landmarks:
                    landmarks = face_landmarks.landmark
                    img_height, img_width, _ = image.shape

                    # Calculate eye positions
                    self.left_eye_position = self.calculate_eye_position(
                        landmarks, 
                        img_width, 
                        self.LEFT_EYE_CENTER_IDX, 
                        self.LEFT_EYE_CORNER_LEFT, 
                        self.LEFT_EYE_CORNER_RIGHT
                    )

                    self.right_eye_position = self.calculate_eye_position(
                        landmarks, 
                        img_width, 
                        self.RIGHT_EYE_CENTER_IDX, 
                        self.RIGHT_EYE_CORNER_LEFT, 
                        self.RIGHT_EYE_CORNER_RIGHT
                    )

                    # Visualization
                    text = (
                        f"Left Eye: {self.left_eye_position:.2f} | "
                        f"Right Eye: {self.right_eye_position:.2f}"
                    )
                    cv2.putText(
                        image, 
                        text, 
                        (10, 30), 
                        cv2.FONT_HERSHEY_SIMPLEX, 
                        0.7, 
                        (0, 255, 0), 
                        2
                    )

            cv2.imshow('Eye Position Tracking', image)

            if cv2.waitKey(5) & 0xFF == 27:  # ESC key
                break

        cap.release()
        cv2.destroyAllWindows()

# Run the eye tracker
if __name__ == "__main__":
    eye_tracker = EyeTracker()
    eye_tracker.track_eyes()