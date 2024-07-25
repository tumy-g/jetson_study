import time
import numpy as np
import cv2
import copy
import mediapipe as mp

#local files
import hand_tracker
import angles
import calc_equation
import draws

#初期設定
mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands

cap = cv2.VideoCapture("/dev/video0")
print("success capture")
time.sleep(2)

#引数によって検出する手の数、信頼度等を設定する
detector = hand_tracker.HandTracker(
    min_detection_confidence=0.5,
    min_tracking_confidence=0.7,
    max_num_hands=1
)

w, h = 960, 720
font = cv2.FONT_HERSHEY_SIMPLEX
font_scale = 0.8
color = (0,0,0)
thickness = 1
lineType = cv2.LINE_4

while cap.isOpened():
    ret, image = cap.read()
    if not ret:
        print("Can't open camera")
        break

    tmp_image = copy.deepcopy(image)

    white_image = np.ones((h, w, 3), dtype=np.uint8)*255

    if detector.detect(image):
        print("success capture")
        tmp_image, tmp_landmark_dict = detector.draw(tmp_image)

        calc_result = calc_equation.formula(angles.get_angles(tmp_landmark_dict)[6],angles.get_angles(tmp_landmark_dict)[10],angles.get_angles(tmp_landmark_dict)[18])
        index_angle = angles.get_angles(tmp_landmark_dict)[6]
        middle_angle = angles.get_angles(tmp_landmark_dict)[10]
        pinky_angle = angles.get_angles(tmp_landmark_dict)[18]
        
        draws.draw_result(white_image, calc_result, 0, 50, int(calc_result*300), 100)
        draws.draw_finger_angle(white_image, "Index", index_angle,0, 140, int(index_angle*4), 190)
        draws.draw_finger_angle(white_image, "Middle", middle_angle,0, 230, int(middle_angle*2.5), 280)
        draws.draw_finger_angle(white_image, "Pinky", pinky_angle,0, 320, int(pinky_angle*4), 370)
        cv2.line(white_image, (300,20), (300, 500), color=(255,0,0))
    else:
        print("fatal capture")
    
    
    cv2.imshow('hoge',white_image)
    cv2.imshow('hand_tracker', cv2.resize(tmp_image, (960//2, 720//2)))
    

    key = cv2.waitKey(1) & 0xFF
    if key == ord('s'):
        cv2.imwrite('../img_sacrifice/screenshot.png', tmp_image)
    if key == ord('q'):
        print("Quit program")
        print("landmarks:",len(tmp_landmark_dict),tmp_landmark_dict)
        print("angles:",len(angles.get_angles(tmp_landmark_dict)),angles.get_angles(tmp_landmark_dict))
        break

cap.release()
cv2.destroyAllWindows()