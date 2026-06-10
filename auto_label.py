from ultralytics import YOLO
import os

# Load pretrained YOLO model
model = YOLO("yolov8n.pt")

input_folder = "frames"
image_output = "dataset/images"
label_output = "dataset/labels"

os.makedirs(image_output, exist_ok=True)
os.makedirs(label_output, exist_ok=True)

# Only keep these classes (aligned with data.yaml)
# 0: car, 1: bike, 2: person
wanted_classes = {"car", "bicycle", "motorcycle", "person"}

image_exts = {".jpg", ".jpeg", ".png", ".bmp", ".tif", ".tiff"}

for img_name in os.listdir(input_folder):
    ext = os.path.splitext(img_name)[1].lower()
    if ext not in image_exts:
        continue

    img_path = os.path.join(input_folder, img_name)

    # YOLO inference
    results = model(img_path)

    label_file = os.path.join(label_output, os.path.splitext(img_name)[0] + ".txt")

    # Ensure image is in dataset/images
    new_img_path = os.path.join(image_output, img_name)
    if not os.path.exists(new_img_path):
        import shutil
        shutil.copy(img_path, new_img_path)

    with open(label_file, "w") as f:
        for r in results:
            if r.boxes is None or len(r.boxes) == 0:
                continue

            # YOLOv8 returns xywh normalized when using xywhn
            boxes = r.boxes.xywhn.cpu().numpy()  # [N, 4]
            classes = r.boxes.cls.cpu().numpy()  # [N]
            names = r.names

            for box, cls_id in zip(boxes, classes):
                class_name = names[int(cls_id)]

                if class_name not in wanted_classes:
                    continue

                if class_name == "car":
                    new_class = 0
                elif class_name in {"bicycle", "motorcycle"}:
                    new_class = 1
                elif class_name == "person":
                    new_class = 2
                else:
                    continue

                # YOLO label format: class x_center y_center width height
                f.write(f"{new_class} {box[0]} {box[1]} {box[2]} {box[3]}\n")

print("✅ Auto labeling completed!")

