import cv2 as cv
import Capture

width: int
height: int
def setResolution(standart):
    """
    :param str standart: NTSC of PAL

    """
    global width, height
    if standart == "NTSC":
        width = 720
        height = 576
    elif standart == "PAL":
        width = 640
        height = 480
    Capture.capture.set(cv.CAP_PROP_FRAME_WIDTH(width))
    Capture.capture.set(cv.CAP_PROP_FRAME_HEIGHT(height))
