import cv2
import numpy as np

def draw_result(image, x1, y1, x2, y2):
    pt1a = (x1, y1)
    pt2a = (x2, y2)

    pt1b = (x1 + 50, y1)
    pt2b = (x2 + 50, y2)

    green = (0,255,0)
    thickness = 2
    font = cv2.FONT_HERSHEY_SIMPLEX
    font_scale = 0.8
    black = (0,0,0)
    thickness = 1

    cv2.putText(image, "計算結果:", pt1a, font, font_scale, black, thickness)
    cv2.rectangle(image, pt1b, pt2b, green, thickness)