import cv2
import numpy as np
from ultralytics import YOLO
import pyttsx3

# Load your trained model
model = YOLO("runs/detect/train5/weights/best.pt")

# Voice alert system
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

# Start camera
cap = cv2.VideoCapture(0)

previous_objects = {}

while True:
    ret, frame = cap.read()
    if not ret:
        break

    results = model(frame)

    current_objects = {}

    for r in results:
        boxes = r.boxes.xyxy.cpu().numpy()

        for i, box in enumerate(boxes):
            x1, y1, x2, y2 = map(int, box[:4])

            # Center
            cx = (x1 + x2) // 2
            cy = (y1 + y2) // 2

            # Area (distance approx)
            area = (x2 - x1) * (y2 - y1)

            current_objects[i] = (cx, cy, area)

            # Draw box
            cv2.rectangle(frame, (x1,y1),(x2,y2),(0,255,0),2)

            if i in previous_objects:
                px, py, p_area = previous_objects[i]

                dx = cx - px
                dy = cy - py

                speed = np.sqrt(dx**2 + dy**2)

                # 🚨 RISK DETECTION
                if area > p_area and speed > 5:
                    speak("Warning! Vehicle approaching")

                    cv2.putText(frame, "RISK", (x1, y1-10),
                                cv2.FONT_HERSHEY_SIMPLEX,
                                0.7, (0,0,255), 2)

                # 🔮 PRE-RISK (Prediction)
                if dy > 0:
                    time_to_collision = cy / (dy + 1)

                    if time_to_collision < 20:
                        speak("High risk approaching")

    previous_objects = current_objects

    cv2.imshow("Path Vision AI", frame)

    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()