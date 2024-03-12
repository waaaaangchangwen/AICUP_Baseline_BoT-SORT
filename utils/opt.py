import argparse

def arg_parse():
    parser = argparse.ArgumentParser()

    parser.add_argument('--data_path', type=str, required=True, help='data path')
    parser.add_argument('--yolo_path', type=str, required=True, help='yolo path')
    parser.add_argument('--out_file_path', type=str, default='runs/tracking_res', help='data path')
    
    parser.add_argument('--devices', nargs='+', type=str, default='0', help='gpu number')
    
    parser.add_argument('--video_shape', type=tuple, default=(720, 1280), help='original video resolution')
    parser.add_argument('--imgsz', type=tuple, default=(720, 1280), help='yolo input size')
    
    parser.add_argument('--save_res', type=bool, default=True, help='save submit file')

    opt = parser.parse_args()
    return opt

if __name__ == '__main__':
    args = arg_parse()
    print(args.imgsz)