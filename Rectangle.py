from typing import Tuple

import cv2
from Resolution import *


def createRectagle(frame_rectagle):
    """
    :param frame_rectagle: frame
    """
    TARGET_LOCKING_AREA_STOP_POINT = int(((width / 100) * 25)), int(((height / 100) * 10))
    TARGET_LOCKING_AREA_START_POINT = int(((width / 100) * 75)), int(((height / 100) * 90))
    TARGET_LOCKING_AREA_COLOR = (0, 0, 255)
    cv2.rectangle(frame_rectagle, TARGET_LOCKING_AREA_START_POINT, TARGET_LOCKING_AREA_STOP_POINT,
                  TARGET_LOCKING_AREA_COLOR, 2)
