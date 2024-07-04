import time
import numpy as np
import cv2
import copy
import mediapipe as mp

#local files
import hand_tracker
import angles
import calc_equation

#初期設定
mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands

cap = cv2.VideoCapture("/dev/video0")
print("success capture")
time.sleep(2)

#引数によって検出する手の数、信頼度等を設定する
detector = hand_tracker.HandTracker(
    min_detection_confidence=0.7,
    min_tracking_confidence=1,
    max_num_hands=1
)

print("suceess handtrack")

while cap.isOpened():
    ret, image = cap.read()
    if not ret:
        print("Can't open camera")
        break

    tmp_image = copy.deepcopy(image)

    if detector.detect(image):
        tmp_image, tmp_landmark_dict = detector.draw(tmp_image)
        cv2.putText(tmp_image,
            text=str(calc_equation.formula(angles.get_angles(tmp_landmark_dict)[6],angles.get_angles(tmp_landmark_dict)[10],angles.get_angles(tmp_landmark_dict)[18]))[0:5],
            org=(10,30),
            fontFace=cv2.FONT_HERSHEY_SIMPLEX,
            fontScale=0.8,
            color=(0,0,0),
            thickness=1,
            lineType=cv2.LINE_4)
        #print(calc_equation.formula(angles.get_angles(tmp_landmark_dict)[6],angles.get_angles(tmp_landmark_dict)[10],angles.get_angles(tmp_landmark_dict)[18]))
    
    cv2.imshow('hand_tracker', cv2.resize(tmp_image, (960, 720)))

    key = cv2.waitKey(1) & 0xFF
    if key == ord('s'):
        cv2.imwrite('../img_sacrifice/screenshot.png', tmp_image)
    if key == ord('q'):
        print("Quit program")
        print("landmarks:",len(tmp_landmark_dict),tmp_landmark_dict)
        print("vectors",angles.calc_vectors(tmp_landmark_dict))
        print("angles:",len(angles.get_angles(tmp_landmark_dict)),angles.get_angles(tmp_landmark_dict))
        break

cap.release()
cv2.destroyAllWindows()