from deepface import DeepFace
import json

result=DeepFace.verify(img1_path="test12.jpg", img2_path="test13.jpg")
print(json.dumps(result, indent=2))