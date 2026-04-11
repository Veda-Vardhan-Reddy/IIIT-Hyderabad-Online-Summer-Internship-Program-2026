from ultralytics import YOLO

model = YOLO("yolov8n.pt")

results = model(r"C:\Users\apple\Desktop\IIITH_OSIP\sample.jpg", save=True)

print("Done!")