from ultralytics import YOLO

if __name__ == '__main__':
    # Parameter
    pretrain_weight = 'pretrain_weight/yolov8l.pt'
    imgsz = 1280
    batch_size = 80

    name = 'yolov8l_AICup_MCMOT_' + str(imgsz) + '_batch_' + str(batch_size) + '_'

    # Training.
    model = YOLO(model=pretrain_weight)

    results = model.train(
        data='/datasets/AI_CUP_MCMOT_dataset/yolo/MCMOT.yaml',
        imgsz=imgsz,
        # rect = True, # if input not square set this true
        mosaic=True,
        device=[0, 1, 2, 3],
        epochs=100,
        batch=batch_size,
        name=name
    )