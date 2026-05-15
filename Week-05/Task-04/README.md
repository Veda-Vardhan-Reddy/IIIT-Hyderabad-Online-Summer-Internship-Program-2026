# Task 4 — Detection Using Custom YOLO Weights

## Activate Virtual Environment

```bash
ls_env\Scripts\activate
```

## Train YOLO Model

```bash
yolo detect train data=data.yaml model=yolov8n.pt epochs=100 imgsz=384
```

## Run Detection on Test Images

```bash
yolo detect predict model=C:\Users\apple\runs\detect\weights\best.pt source=test
```

## Output Location

```text
C:\Users\apple\runs\detect\predict\
```

## Classes Used

* person
* car

```
```

