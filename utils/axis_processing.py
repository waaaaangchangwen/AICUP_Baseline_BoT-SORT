import cv2
import numpy as np
    

def vis_bbox(img, xywh, track_id):
    bb_left, bb_top, bb_width, bb_height = xywh
    bb_left, bb_top, bb_width, bb_height = int(bb_left), int(bb_top), int(bb_width), int(bb_height)
    
    cv2.rectangle(img, (bb_left, bb_top), (bb_left + bb_width, bb_top + bb_height), (0, 255, 0), 2)
    cv2.putText(img, f"{int(track_id)}", (bb_left, bb_top - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
    cv2.imwrite('test.jpg', img)
    
    return 0

    
def bbox_normalized(bbox, img_w, img_h):
    return bbox / np.array([img_w, img_h, img_w, img_h])


def norm_box_into_absolute(bbox, img_w, img_h):
    return bbox * np.array([img_w, img_h, img_w, img_h])


def bbox_change_axis(boxes, orig_shape, submit_shape):
    ori_h, ori_w = orig_shape
    new_h, new_w = submit_shape
    
    boxes = np.array([norm_box_into_absolute(bbox_normalized(box, ori_w, ori_h), new_w, new_h) for box in boxes])
    
    return boxes


def out_of_range(x1, y1, x2, y2, max_x, max_y):
    # Calculate width and height
    bb_width = x2 - x1
    bb_height = y2 - y1
    
    # Clip left and top to ensure within image bounds
    bb_left = max(min(x1, max_x), 0)
    bb_top = max(min(y1, max_y), 0)
    
    # Calculate width and height again after clipping
    bb_width = min(max_x - bb_left, bb_width)
    bb_height = min(max_y - bb_top, bb_height)
    
    return bb_left, bb_top, bb_width, bb_height


if __name__ == '__main__':
    # debug here
    pass