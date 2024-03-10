# AICup_MCMOT_Baseline

## Dataset_File_Tree
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

frame_id| track_id | bb_left|  bb_top | bb_width |bb_height|3d_x|3d_y|3d_z|
--------| -------- | -------| --------| ---------|-------- |----|----|----|
1       |1         |843     |742      | 30       |30       |-1  |-1  |-1  |