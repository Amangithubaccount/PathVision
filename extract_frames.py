import cv2
import os

video_folder = "videos"
output_folder = "frames"

os.makedirs(output_folder, exist_ok=True)

video_exts = {".mp4", ".avi", ".mov", ".mkv", ".webm"}

videos = []
if os.path.isdir(video_folder):
    for f in os.listdir(video_folder):
        fp = os.path.join(video_folder, f)
        if not os.path.isfile(fp):
            continue
        ext = os.path.splitext(f)[1].lower()
        if ext in video_exts:
            videos.append(f)

print("Videos found:", videos)

for video_file in videos:
    video_path = os.path.join(video_folder, video_file)

    print(f"\nProcessing: {video_file}")

    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        print(f"❌ Cannot open: {video_file}")
        continue

    count = 0
    saved = 0

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        if count % 5 == 0:
            filename = f"{video_file}_{count}.jpg"
            save_path = os.path.join(output_folder, filename)
            cv2.imwrite(save_path, frame)
            saved += 1

        count += 1

    cap.release()
    print(f"✅ Saved {saved} frames from {video_file}")

print("\n🎯 DONE")
