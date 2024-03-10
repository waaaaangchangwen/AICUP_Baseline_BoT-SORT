from ultralytics import YOLO

    
if __name__ == '__main__':
    pretrain_weight = 'runs/detect/yolov8l_AICup_MCMOT_1280_batch_32_/weights/best.pt'
    model = YOLO(model=pretrain_weight)

    # valid
    results = model.val(
        data='/datasets/AI_CUP_MCMOT_dataset/MCMOT.yaml',
        imgsz=1280,
        device='0',
        batch=8,
        name='yolov8l_batch_32_valid_'
    )

