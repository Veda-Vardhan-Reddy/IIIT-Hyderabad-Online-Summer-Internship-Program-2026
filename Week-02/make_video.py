import cv2
import os

main_folder = "predicted_frames"

folders = []

# Collect only folders like det1, det2, det3 ... det1800
for f in os.listdir(main_folder):
    if f.startswith("det") and f[3:].isdigit():   # ensure after 'det' is a number
        folders.append(f)

# Sort numerically (det1, det2, ..., det1800)
folders = sorted(folders, key=lambda x: int(x[3:]))

images = []

# Loop through each detX folder
for folder in folders:
    folder_path = os.path.join(main_folder, folder)
    
    # get first image inside folder
    for file in os.listdir(folder_path):
        if file.lower().endswith((".jpg", ".jpeg", ".png")):
            images.append(os.path.join(folder_path, file))
            break

# Read first frame to get video size
frame = cv2.imread(images[0])
height, width, layers = frame.shape

# Create video writer (30 FPS)
video = cv2.VideoWriter("final_output.mp4", cv2.VideoWriter_fourcc(*"mp4v"), 30, (width, height))

# Add all frames
for img_path in images:
    img = cv2.imread(img_path)
    video.write(img)

video.release()
print("🎉 Video created: final_output.mp4")