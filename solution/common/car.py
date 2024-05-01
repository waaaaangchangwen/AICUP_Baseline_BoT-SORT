from dataclasses import dataclass
import numpy as np
from typing import List, Union, Dict

@dataclass
class BoundingBox:
    """
    Represents a bounding box with x, y, width, and height attributes.
    The x, y, width, and height attributes represent the coordinates and dimensions of the bounding box.
    These values are normalized to float, following the format used in YOLO's output.
    """
    x: float
    y: float
    width: float
    height: float

@dataclass
class CroppedCarImage:
    """
    Represents a cropped car image
    """
    video_name: str
    frame_name: str
    bounding_box: BoundingBox
    image: np.ndarray


class Car:
    """
    Represents a car object.

    Attributes:
        global_id (int): The global ID of the car.
        final_matched_id (int): The final matched ID of the car.
        cropped_images (List[CroppedCarImage]): A list of cropped car images.
        features (Dict[str, Union[float, np.ndarray]]): A dictionary of car features.
    """
    def __init__(self, global_id: int):
        self.global_id: int = global_id
        self.final_matched_id: int = -1
        self.cropped_images: List[CroppedCarImage] = []
        self.features: Dict[str, Union[float, np.ndarray]] = {}

