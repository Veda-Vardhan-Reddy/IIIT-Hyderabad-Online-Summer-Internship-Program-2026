# Week 5 Task 1 — Dataset Annotation using Label Studio

## Overview

This task focuses on preparing a custom dataset for object detection using Label Studio.

Frames extracted from a video were manually annotated to create labeled datasets for training and validation of a Computer Vision model.

The objective was to identify and annotate:

* person
* car

objects in images.

---

# Objectives

* Install and configure Label Studio
* Create custom annotation project
* Define object classes
* Annotate training and validation images
* Generate YOLO compatible label files

---

# Tools Used

* Python
* Label Studio
* YOLO Annotation Format

---

# Dataset Structure

```text id="v47n6d"
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

```text id="mjlwmk"
0 → person
1 → car
```

---

# Label Studio Setup

Virtual environment activation:

```bash id="m1e4yf"
ls_env\Scripts\activate
```

Install Label Studio:

```bash id="o6m0wt"
pip install label-studio
```

Run Label Studio:

```bash id="jhf6s2"
label-studio
```

Open in browser:

```text id="7m3jko"
http://localhost:8080
```

---

# Annotation Process

* Imported training and validation images
* Created bounding box labels:

  * person
  * car
* Annotated all visible objects
* Exported annotations in YOLO format

Generated:

* `.txt` label files
* YAML configuration
* train/validation image lists

---

# Example YOLO Label Format

```text id="j91rmy"
class_id x_center y_center width height
```

Example:

```text id="3y95dg"
0 0.512 0.478 0.215 0.641
```

Where:

* `0` → person
* values are normalized coordinates

---

# Output Files Generated

```text id="9jy7jh"
train/labels/*.txt
val/labels/*.txt
data.yaml
train.txt
val.txt
```

---

# Learning Outcomes

This task helped in understanding:

* image annotation
* bounding box creation
* dataset organization
* YOLO annotation format
* dataset preparation for deep learning

---

# Conclusion

A fully annotated custom dataset was successfully prepared for training a Computer Vision object detection model capable of detecting:

* persons
* cars

using transfer learning techniques.

---

# Acknowledgement

Thanks to:

* IIIT Hyderabad
* iHub-Data
* My Institution

for providing the opportunity to work on practical Computer Vision applications.

