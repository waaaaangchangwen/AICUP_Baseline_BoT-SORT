# AICup_MCMOT_Baseline
- Our baseline is base on Ultralytics YOLOv8 framework, providing multiple object tracking (MOT) algorithms: BoT-SORT and Bytetrack. 
- In the BoT-SORT architecture, the ReID model used needs to be implemented and replaced independently. 
- For more details, you can refer to the following Repository: 
    - [Ultralytics YOLOv8](https://github.com/ultralytics/ultralytics)
    - [Offical BoT-SORT Implementation](https://github.com/NirAharon/BoT-SORT)

## Installation
**Step1.** Fork this Repository

**Step2.** Clone your Repository to your device

**Step3.** Create Conda environment and install `pytorch >= 2.0`
```bash
conda create -n AI_CUP python=3.9
conda activate AI_CUP
```

**Step4.** Install other requirement
```bash
cd AICup_MCMOT_Baseline
pip install -r requirements.txt
```

## Data Preparation
Download the AI_CUP dataset, And put them in the following structure:
```python
├── train
│   ├── Images
│   │   ├── 0 (Camera ID)
│   │   │  ├── 00001.jpg (Frame ID)
│   │   │  ├── 00002.jpg
│   │   │  ├── 00003.jpg
│   │   │  ├── ...
│   │   ├── 1 (Camera ID)
│   │   │  ├── 00001.jpg (Frame ID)
│   │   │  ├── 00002.jpg
│   │   │  ├── 00003.jpg
│   │   │  ├── ...
│   └── Labels
│       ├── 0.txt
│       ├── 1.txt
│       ├── 2.txt
│       ├── ...
--------------------------------------------------
├── test
│   ├── Images
│   │   ├── 0 (Camera ID)
│   │   │  ├── 00001.jpg (Frame ID)
│   │   │  ├── 00002.jpg
│   │   │  ├── 00003.jpg
│   │   │  ├── ...
│   │   ├── 1 (Camera ID)
│   │   │  ├── 00001.jpg (Frame ID)
│   │   │  ├── 00002.jpg
│   │   │  ├── 00003.jpg
│   │   │  ├── ...
```

## GroundTruth Format
Using same format on [py-motmetrics](https://github.com/cheind/py-motmetrics)

> [!WARNING]
> **The evulate images resolution is `1280 * 720`**

frame_id| track_id | bb_left|  bb_top | bb_width |bb_height|3d_x|3d_y|3d_z|
--------| -------- | -------| --------| ---------|-------- |----|----|----|
1       |1         |843     |742      | 30       |30       |-1  |-1  |-1  |

## Training Yolov8
You can see the how to used the training, valid, and predict function at 
- [YOLOv8 training docs](https://docs.ultralytics.com/zh/modes/train/#train-settings)
- [YOLOv8 valid docs](https://docs.ultralytics.com/zh/modes/val/)
- [YOLOv8 predict docs](https://docs.ultralytics.com/zh/modes/predict/)

```bash
cd AICup_MCMOT_Baseline
python train_YOLO/train_YOLOv8.py
python train_YOLO/val_YOLOv8.py
```

The Result will be save at `runs/detect` folder

## Tracking and create the submit file

You Can run our sample code: `detect.py` by following commend:
```bash
cd AICup_MCMOT_Baseline
python detect.py --data_path "your dataset path" --yolo_path "your model weight path" --devices "0, 1"
```

#### Config:
- `data_path`: Your dataset folder

- `yolo_path`: Your YOLO model's weight

- `out_file_path`: Where your output file save

- `devices`: 'cpu' or 'gpu number', support multi-GPU training

- `video_shape`: original video resolution

- `imgsz`: yolo input size

- `save_res`: bool, save submit file, default = True

## Where to add ReID model in Tracking algorithm
if you want to add ReID model in YOLOv8's tracking, you need to edit YOLOv8 source code at:
[ultralytics/ultralytics/trackers/bot_sort.py](https://github.com/ultralytics/ultralytics/blob/af6c02c39be4ee30e0119cc24468912257a3b529/ultralytics/trackers/bot_sort.py#L160)

For example, In the conda environment, the source code is locate at:
```bash
.conda/envs/(your_env_name)/lib/python3.9/site-packages/ultralytics/trackers/bot_sort.py
```

## Result
![](demo_pic/00040.jpg)
![](demo_pic/results.png)