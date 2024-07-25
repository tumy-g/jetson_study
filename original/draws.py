import cv2
import numpy as np

green = (0,255,0)
thickness = 2
font = cv2.FONT_HERSHEY_SIMPLEX
font_scale = 0.8
black = (0,0,0)
thickness = -1

def draw_result(image, calc, x1, y1, x2, y2)->None:
    pt = (x1, y1)

    pt1b = (x1, y1+10)
    pt2b = (x2, y2+10)

    cv2.putText(image, "Calc:"+str(calc)[0:5], pt, font, font_scale, black, thickness=1)
    cv2.rectangle(image, pt1b, pt2b, green, thickness)

def draw_finger_angle(image, name:str,angle, x1, y1, x2, y2)->None:
    pt = (x1, y1)

    pt1b = (x1, y1+10)
    pt2b = (x2, y2+10)
    
    cv2.putText(image, name + ":" + str(angle)[0:5], pt, font, font_scale, black, thickness=1)
    cv2.rectangle(image, pt1b, pt2b, green, thickness)