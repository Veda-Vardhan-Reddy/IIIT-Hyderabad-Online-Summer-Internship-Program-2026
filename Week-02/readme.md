# IIITH OSIP – Week 02 Submission

This repository contains all tasks completed for Week 02 of the IIITH Online Summer Internship Program.

---

## Task 01 – Create Virtual Environment

### Commands Used
cd C:\Users\apple\Desktop\IIITH_OSIP
python -m venv osip_env
osip_env\Scripts\activate

---

## Task 02 – Install Ultralytics YOLO

### Command Used
pip install -U ultralytics

---

## Task 03 – Object Detection on Single Image

### detect.py
from ultralytics import YOLO

model = YOLO("yolov8n.pt")
results = model(r"C:\Users\apple\Desktop\IIITH_OSIP\bus.jpg", save=True)

print("Detection completed!")

### Run Command
python detect.py

---

## Bonus Task – Frame Extraction from Video

### extract_frames.py
import cv2
import os

video_path = "input.mp4"
output_folder = "frames"
os.makedirs(output_folder, exist_ok=True)

cap = cv2.VideoCapture(video_path)
count = 0

while count < 1800:
    ret, frame = cap.read()
    if not ret:
        break
    cv2.imwrite(f"{output_folder}/frame_{count:04d}.jpg", frame)
    count += 1

cap.release()
print("Frames extracted")

### Run
python extract_frames.py

---

## Bonus Task – YOLO Detection on All Frames

### detect_frames.py
from ultralytics import YOLO
import os

model = YOLO("yolov8n.pt")

input_folder = "frames"
output_folder = "predicted_frames"

os.makedirs(output_folder, exist_ok=True)

for img in sorted(os.listdir(input_folder)):
    model(os.path.join(input_folder, img), save=True, project=output_folder, name=img.split('.')[0])

print("All frames processed")

### Run
python detect_frames.py

---

## Bonus Task – Create Video from Frames

### make_video.py
import cv2
import os

main_folder = "predicted_frames"
folders = []

for f in os.listdir(main_folder):
    if f.startswith("det") and f[3:].isdigit():
        folders.append(f)

folders = sorted(folders, key=lambda x: int(x[3:]))

images = []

for folder in folders:
    folder_path = os.path.join(main_folder, folder)
    for file in os.listdir(folder_path):
        if file.endswith(".jpg"):
            images.append(os.path.join(folder_path, file))
            break

frame = cv2.imread(images[0])
h, w, _ = frame.shape

video = cv2.VideoWriter("final_output.mp4", cv2.VideoWriter_fourcc(*"mp4v"), 30, (w, h))

for img in images:
    video.write(cv2.imread(img))

video.release()
print("Video created")

### Run
python make_video.py

---

## Bonus Task – Add Music using FFmpeg

ffmpeg -i final_output.mp4 -i music.mp3 -c:v copy -c:a aac -shortest final_video_with_audio.mp4

---

## Final Output

Final Video:
https://www.youtube.com/watch?v=Wx9f1Mr0Hi4

Source Video:
https://www.youtube.com/watch?v=RFb6wbsffY0

---

## Summary

- Created Python virtual environment  
- Installed YOLOv8  
- Performed object detection on image  
- Extracted 1800 frames from video  
- Applied YOLO detection on all frames  
- Reconstructed video from frames  
- Added background music  
- Uploaded final video  

---

# End of Week 02 Submission
