from ultralytics import YOLO
import os

model = YOLO("yolov8n.pt")

input_folder = "frames"
output_folder = "detected_frames"
os.makedirs(output_folder, exist_ok=True)

for img in os.listdir(input_folder):
    model.predict(source=f"{input_folder}/{img}", save=True, project=output_folder, name="")