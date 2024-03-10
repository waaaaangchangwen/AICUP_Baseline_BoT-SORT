import os
import cv2
import glob

from tqdm import tqdm

def visualize_boxes_from_txt(txt_file, data_path, vis_res_path):
    
    frame = sorted(
        glob.glob(
            os.path.join(data_path, '*.jpg')
        )
    )
    
    frame_num = 0
    with open(txt_file, 'r') as f:
        for line in tqdm(f, desc='vis bbox'):
            parts = line.strip().split(',')
            new_frame_num, track_id, bb_left, bb_top, bb_width, bb_height, conf, _, _, _ = map(float, parts)
            
            if new_frame_num > frame_num:
                if frame_num > 0:
                    cv2.imwrite(os.path.join(vis_res_path, f'frame_{frame_num}.jpg'), img)
                    
                img = cv2.imread(frame[int(new_frame_num)])
                frame_num = new_frame_num
            
            bb_left, bb_top, bb_width, bb_height = map(int, [bb_left, bb_top, bb_width, bb_height])
            cv2.rectangle(img, (bb_left, bb_top), (bb_left + bb_width, bb_top + bb_height), (0, 255, 0), 2)
            cv2.putText(img, f"{int(track_id)}", (bb_left, bb_top - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
            

if __name__ == '__main__':
    txt_file = "runs/tracking_res/0.txt"
    data_path = "/datasets/AI_CUP_MCMOT_dataset/test/Images/0"
    vis_res_path = "runs/vis_tracking_res/"
    
    os.makedirs(vis_res_path, exist_ok=True)
    visualize_boxes_from_txt(txt_file, data_path, vis_res_path)
