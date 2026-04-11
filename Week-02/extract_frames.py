import cv2
import os

video_path = "video.mp4"   # your 5:35 min video
output_folder = "frames"
max_frames = 1800

os.makedirs(output_folder, exist_ok=True)

cap = cv2.VideoCapture(video_path)
frame_count = 0

while True:
    ret, frame = cap.read()
    if not ret or frame_count >= max_frames:
        break
    cv2.imwrite(f"{output_folder}/frame_{frame_count:04d}.jpg", frame)
    frame_count += 1

cap.release()
print("Done! Extracted", frame_count, "frames")