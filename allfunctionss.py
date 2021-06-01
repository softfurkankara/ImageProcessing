import cv2
import numpy as np


def divideOfScreen(frame):
    cv2.line(frame,(320,0),(320,480),(0,255,255),1)
    cv2.line(frame,(0,240),(640,240),(0,255,255),1)
    return frame






    
    