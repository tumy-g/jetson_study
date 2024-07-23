import cv2
import numpy as np

def draw_rectangle(image, x1, y1, x2, y2):
    pt1 = (x1, y1)
    pt2 = (x2, y2)

    color = (0,255,0)
    thickness = 2
    cv2.rectangle(image, pt1, pt2, color, thickness)