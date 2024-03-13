import os
import glob
from ultralytics import YOLO

from utils.opt import arg_parse
from utils.axis_processing import out_of_range


def make_submission_file(args, file_name='out.txt'):
    """
    Yolo's output Docs:
        https://docs.ultralytics.com/zh/reference/engine/results/#ultralytics.engine.results.Results
        https://docs.ultralytics.com/zh/reference/engine/results/#ultralytics.engine.results.Boxes
        
    Submit format(same to MOT16):
        <frame>, <id>, <bb_left>, <bb_top>, <bb_width>, <bb_height>, <conf>, <x>, <y>, <z>
    """

    with open(file_name, 'a') as f:
        frame_num = 0
        for t in args.tracker:
            frame_num += 1
            
            if t.boxes.is_track:
                for b in t.boxes.data:
                    x1, y1, x2, y2, track_id, conf, label_id = b
                    
                    # Convert tensor values to Python scalars
                    x1, y1, x2, y2, track_id, conf, label_id = (
                        x1.item(), y1.item(), x2.item(), y2.item(),
                        int(track_id.item()), conf.item(), int(label_id.item())
                    )
                    x1, y1, w, h = out_of_range(x1, y1, x2, y2, t.orig_shape[1], t.orig_shape[0])
                    
                    f.write(
                        f"{frame_num},{track_id},{x1},{y1},{w},{h},{conf},-1,-1,-1\n"
                    )
                
    return 0


def main(args):
    """
        main func args: 
            see utils/opt.py
            
        yolo.track args:
            source (str, optional): The input source for object tracking. It can be a file path, URL, or video stream.
            stream (bool, optional): Treats the input source as a continuous video stream. Defaults to False.
            persist (bool, optional): Persists the trackers between different calls to this method. Defaults to False.
            **kwargs (dict): Additional keyword arguments for configuring the tracking process. These arguments allow
                for further customization of the tracking behavior.
                
        You need to custom your ReID feature extractor in ultralytics/ultralytics/trackers/bot_sort.py #L160
        see: https://github.com/ultralytics/ultralytics/blob/af6c02c39be4ee30e0119cc24468912257a3b529/ultralytics/trackers/bot_sort.py#L160
    """
    
    os.makedirs(args.out_file_path, exist_ok=True)
    
    # Path: /datasets/AI_CUP_MCMOT_dataset/train(valid, test)/images/timestemp_path
    for timestemp_path in sorted(glob.glob(os.path.join(args.data_path, '*'))):
        timestemp = timestemp_path.split('/')[-1]

        # tracking Using default tracker (without ReID)
        args.tracker = args.yolo.track(
            source=timestemp_path, # one folder for one prediction
            imgsz=args.imgsz,
            device=args.devices,
            stream=True,
            persist=True,
            conf = 0.0,
            save=True, # visualized your result at runs/detect/track
        )

        if args.save_res:
            make_submission_file(
                args, 
                file_name=os.path.join(args.out_file_path, f'{timestemp}.txt'),
            )
    
    return 0


if __name__ == '__main__':
    args = arg_parse()

    # # debug_args:
    # args.devices = '1'
    # args.data_path = '/datasets/AI_CUP_MCMOT_dataset/test/Images'
    # args.yolo_path = 'runs/detect/yolov8l_AICup_MCMOT_1280_batch_63_/weights/best.pt'
    # args.imgsz = (720, 1280)
    # args.save_res = True
    # args.out_file_path = 'runs/tracking_res'

    args.yolo = YOLO(args.yolo_path)
    main(args)
