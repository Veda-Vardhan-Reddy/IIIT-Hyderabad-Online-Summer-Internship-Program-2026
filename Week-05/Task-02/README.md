# Week 5 Task 2 — Image Preprocessing and Dataset Preparation

## Overview

This task focuses on preprocessing annotated images before training the object detection model.

The original extracted frames were large in size, so they were resized using FFmpeg while preserving aspect ratio. Since YOLO annotations are stored in normalized format, resizing images while maintaining aspect ratio ensures that the existing label coordinates remain valid.

---

# Objectives

* Resize training and validation images
* Preserve aspect ratio
* Maintain compatibility with YOLO label files
* Prepare optimized dataset for training

---

# Tools Used

* Python
* FFmpeg
* YOLO Dataset Format

---

# Dataset Structure

```text id="7t1h8g"
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

```text id="gk4f2l"
0 → person
1 → car
```

---

# Why Image Resizing Was Needed

The extracted frames were high-resolution images, which:

* increase training time
* consume more memory
* reduce training efficiency on CPU systems

To optimize training performance, images were resized to smaller dimensions.

---

# Aspect Ratio Preservation

Images were resized using:

```text id="bztjlwm"
384:-1
```

This means:

* width = 384 pixels
* height adjusted automatically

This preserves aspect ratio.

Since YOLO label coordinates are normalized between:

* 0 and 1

the existing `.txt` label files remain valid after resizing.

Therefore:

* no modification of label files was required

---

# FFmpeg Command Used

Example resizing command:

```bash id="w7c6dg"
ffmpeg -i input.jpg -vf scale=384:-1 output.jpg
```

Batch processing was performed for:

* training images
* validation images

---

# Preprocessing Workflow

1. Extracted video frames
2. Annotated images using Label Studio
3. Organized train and validation datasets
4. Resized images using FFmpeg
5. Preserved annotation compatibility
6. Prepared dataset for training

---

# Output

Resized images were stored inside:

```text id="1b8o7j"
train/images/
val/images/
```

Existing labels inside:

```text id="4j3a4t"
train/labels/
val/labels/
```

were reused directly.

---

# Learning Outcomes

This task helped in understanding:

* image preprocessing
* dataset optimization
* aspect ratio preservation
* YOLO normalized annotations
* efficient training preparation

---

# Conclusion

The dataset was successfully optimized for training by resizing images while preserving aspect ratio and maintaining compatibility with YOLO annotation files.

The processed dataset is now ready for transfer learning and object detection model training.

---

# Acknowledgement

Thanks to:

* IIIT Hyderabad
* iHub-Data
* My Institution

for providing the opportunity to work on practical Computer Vision tasks.

