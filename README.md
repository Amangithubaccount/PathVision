# PathVision
A pre-risk analyzer and detection system for visually blind ones



🚀 Overview
PathVision AI is an intelligent pre-risk detection system designed to enhance mobility and independence for visually impaired individuals. Unlike traditional obstacle detection systems that only identify nearby objects, PathVision AI predicts potential collision risks before they occur.
Using Computer Vision, Artificial Intelligence, Motion Analysis, and Risk Prediction algorithms, the system continuously monitors the surrounding environment, detects moving objects, analyzes their trajectories, and warns users about potential dangers through audio, vibration, or haptic feedback.
The ultimate vision of PathVision AI is to act as an intelligent digital guide capable of helping visually impaired users navigate roads, sidewalks, and crowded environments safely and confidently.


🎯 Problem Statement
Millions of visually impaired individuals face daily mobility challenges due to:
Fast-moving vehicles
Unexpected pedestrian movement
Blind intersections
Road-crossing hazards
Limited awareness of approaching objects
Most assistive devices focus on obstacle detection rather than risk prediction.
PathVision AI addresses this gap by introducing a Pre-Risk Detection System capable of predicting danger before an actual collision or hazardous situation occurs.


💡 Key Innovation
Traditional Systems:
Object Detected → Alert User

PathVision AI:
![image alt](https://github.com/Amangithubaccount/PathVision/blob/main/PathVision_Hardware.jpeg)

Instead of merely informing users about nearby objects, the system estimates:
1.Direction of movement
2.Relative speed
3.Collision probability
4.Risk level
5.Time-to-impact approximation

This enables proactive rather than reactive assistance.

![image alt](https://github.com/Amangithubaccount/PathVision/blob/main/PathVision_flow.jpeg)



🔄 Project Workflow
Phase 1 – Data Collection
Vehicle and street-environment videos are collected from:
.Roads
.Crosswalks
.Sidewalks
.Urban traffic areas
These videos provide realistic scenarios for model training.

Phase 2 – Frame Extraction
Video data is converted into image frames.

python extract_frames.py

Purpose:
.Generate training images
.Increase dataset size
.Capture object movement patterns

Phase 3 – Auto Labeling
Automatic annotation is performed to label:
.Cars
.Bikes
.Pedestrians

python auto_label.py
Generated labels are stored in YOLO format.

Phase 4 – Dataset Creation
Dataset Structure:

dataset/
│
├── images/
│
├── labels/
│
└── labels.cache
The dataset consists of images and corresponding annotations for supervised training. 
PathVisionAI_Project_Crux.pdf

Phase 5 – YOLOv8 Training
A custom YOLOv8 Nano model is trained on the prepared dataset. 

Training Command

yolo detect train \
model=yolov8n.pt \
data=data.yaml \
epochs=100 \
imgsz=640

Output:

runs/
└── detect/
    ├── train/
    ├── train2/
    ├── train3/
    ├── train4/
    ├── train5/
    └── train6/
    
Best-performing weights:

best.pt
or
last.pt
These models are later used for real-time inference. 




🧠 Pre-Risk Prediction Engine
Object detection alone is insufficient for ensuring safe navigation.

PathVision AI introduces a dedicated risk assessment layer that evaluates:
1. Object Direction
Determines whether an object is:
.Approaching
.Receding
.Moving laterally

3. Apparent Distance
Estimated through:
.Bounding box size
.Position changes
.Future depth-estimation modules

4. Relative Speed
Measured using frame-to-frame movement.

5. Collision Probability
The system predicts whether the object's trajectory intersects with the user's path.

6. Risk Score
Risk Score = Distance Weight + Speed Weight + Direction Weight

When the score exceeds a predefined threshold:

HIGH RISK → Alert User
This enables warnings before an actual collision event. 




🛡️ Multi-Zone Safety System
Advantages:
.Simple implementation
.Reduced processing
.Disadvantages:
.Misses side-approaching vehicles
.Unsafe at intersections

PathVision Multi-Zone Approach
Left Zone     Front Zone     Right Zone

    [L]           [F]           [R]
Benefits:
✅ Detects vehicles from multiple directions
✅ Better road-crossing awareness
✅ Improved situational understanding
✅ Reduced false alerts
The concept is inspired by the project's safety-zone design philosophy.




🔊 Alert System
When risk is detected, the system can notify users through:
Audio Alerts
Warning! Vehicle approaching ahead.

Voice Guidance
Pedestrian crossing from left.

Haptic Feedback
Low Risk  → Mild Vibration
High Risk → Strong Vibration

This ensures accessibility across different environments.



📂 Project Structure:
PATHVISION/
│
├── dataset/
│   ├── images/
│   ├── labels/
│   └── labels.cache
│
├── frames/
│
├── models/
│
├── runs/
│   └── detect/
│       ├── train/
│       ├── train2/
│       ├── train3/
│       ├── train4/
│       ├── train5/
│       └── train6/
│
├── videos/
│
├── auto_label.py
├── extract_frames.py
├── risk_system.py
├── data.yaml
├── yolov8n.pt
├── README.md
└── .gitignore





⚙️ Technology Stack
Technology              Purpose
Python              Core Development
YOLOv8 Nano         Object Detection
OpenCV              Image & Video Processing
NumPy               Numerical Computation
Ultralytics         model Training
Computer Vision     Scene Understanding
AI Risk Engine      Collision Prediction



🎯 Target Objects
Current detection classes include:
🚗 Cars
🏍️ Bikes
🚶 Pedestrians
Buses
Trucks



📈 Future Enhancements
Planned upgrades include: 
.DeepSORT Integration
Advanced object tracking and identity preservation.

.Depth Estimation
Accurate distance measurement for risk assessment.

.Raspberry Pi Deployment
Portable smart-stick implementation.

.GPS Navigation
Location-aware guidance and routing.

.Haptic Feedback
Enhanced tactile communication.

.Road & Sidewalk Detection
Safer navigation and path recommendation.



🌍 Social Impact
PathVision AI is more than a computer vision project.
It aims to:
.Improve independence
.Increase road safety
.Reduce mobility anxiety
.Enable confident navigation
.Enhance quality of life for visually impaired individuals

By combining artificial intelligence with assistive technology, PathVision AI moves toward a future where accessibility and safety are available to everyone.
