# Task-2: YOLOv26 Dataset Preparation  
This task involves preparing a complete custom dataset for training the YOLOv26 model. The dataset is organized using the standard YOLO structure with three folders: train, val, and test. Each of these contains an images directory with extracted video frames. The train and val folders also include a labels directory containing YOLO-format annotation files. Each annotation file follows the format: class_id x_center y_center width height, with all values normalized between 0 and 1. The dataset also includes a data.yaml file which defines paths for train, val, test, number of classes, and class names. The format used is:  
train: ../train/images  
val: ../val/images  
test: ../test/images  
nc: <number_of_classes>  
names: [<class1>, <class2>, ...]  
Additionally, train.txt and val.txt files are included, each containing the absolute paths of all images in their respective sets, which helps YOLOv26 correctly load data during training. The Task-2 folder contains: extracted frames, annotation label files, data.yaml, train.txt, val.txt, and the complete YOLO dataset structure required for training.
