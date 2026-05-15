# Week 5 Task 3 — Custom YOLO Model Training using Transfer Learning

## Overview

This task focuses on training a custom object detection model using transfer learning.

A pre-trained YOLOv8 model was fine-tuned on a custom annotated dataset containing:

* person
* car

classes.

The training process generated a new set of learned weights capable of detecting custom objects on unseen images.

---

# Objectives

* Use transfer learning on a pre-trained YOLO model
* Train custom object detector
* Monitor training and validation performance
* Generate optimized custom weights

---

# Tools Used

* Python
* YOLOv8
* PyTorch
* FFmpeg
* Label Studio

---

# Dataset Structure

```text id="cyn0h7"
dataset/
│
├── train/
│   ├── images/
│   └── labels/
│
├── val/
│   ├── images/
│   └── labels/
│
├── data.yaml
├── train.txt
└── val.txt
```

---

# Classes Used

```text id="bh20a5"
0 → person
1 → car
```

---

# Data Configuration File

Example `data.yaml`:

```yaml id="r5afku"
path: C:/Users/apple/Desktop/dataset

train: train/images
val: val/images

names:
  0: person
  1: car
```

---

# Model Used

Pre-trained model:

```text id="ojt8u5"
yolov8n.pt
```

YOLOv8 Nano was selected because:

* lightweight
* faster training
* suitable for CPU systems

---

# Training Command

Virtual environment activation:

```bash id="h2ptuj"
ls_env\Scripts\activate
```

Training command:

```bash id="s2gwjg"
yolo detect train data=data.yaml model=yolov8n.pt epochs=100 imgsz=384
```

---

# Training Process

During training:

* training loss
* validation loss
* precision
* recall
* mAP metrics

were monitored.

Initially:

* both training loss and validation loss decreased

After certain epochs:

* validation loss started increasing

This indicated:

* overfitting of the model

The best epoch weights were automatically saved.

---

# Generated Files

Training outputs were generated inside:

```text id="t1g5qf"
runs/detect/
```

Important files:

```text id="5lc0mx"
weights/best.pt
weights/last.pt
results.png
confusion_matrix.png
results.csv
```

---

# Best Model Weights

```text id="8byd12"
weights/best.pt
```

This file contains the optimized trained model weights based on validation performance.

---

# Training Analytics

`results.png` contains:

* training loss curves
* validation loss curves
* precision
* recall
* mAP metrics

`confusion_matrix.png` shows:

* prediction accuracy
* class-wise performance

---

# Transfer Learning

Instead of training from scratch:

* a pre-trained YOLO model was reused
* existing learned features were adapted to custom classes

This reduced:

* training time
* dataset requirements

while improving detection performance.

---

# Learning Outcomes

This task helped in understanding:

* transfer learning
* deep learning model training
* object detection pipeline
* training analytics
* overfitting analysis
* custom weight generation

---

# Conclusion

A custom YOLOv8 object detection model was successfully trained for detecting:

* persons
* cars

using transfer learning techniques.

The training process generated optimized weights capable of performing inference on unseen datasets.

---

# Acknowledgement

Thanks to:

* IIIT Hyderabad
* iHub-Data
* My Institution

for providing the opportunity to work on practical Computer Vision applications.

