import time
import numpy as np
import cv2
import copy
import mediapipe as mp

#local files
import hand_tracker
import angles

#初期設定
mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands

cap = cv2.VideoCapture("/dev/video0")
print("success capture")
time.sleep(2)

#引数はとりあえず適当 (1, 0.5, 0.5)
detector = hand_tracker.HandTracker(1, 1, 1)
print("suceess handtrack")

while cap.isOpened():
    ret, image = cap.read()
    if not ret:
        print("Can't open camera")
        break

    tmp_image = copy.deepcopy(image)

    if detector.detect(image):
        tmp_image, tmp_landmark_dict = detector.draw(tmp_image)
    
    cv2.imshow('hand_tracker', cv2.resize(tmp_image, (960, 720)))

    print(len(angles.get_angles(tmp_landmark_dict)))
    print(angles.get_angles(tmp_landmark_dict)[6])

    key = cv2.waitKey(1) & 0xFF
    if key == ord('s'):
        cv2.imwrite('../img_sacrifice/screenshot.png', tmp_image)
    if key == ord('q'):
        print("quit program")
        print("lanfmarks:",tmp_landmark_dict)
        print("angles:",angles.get_angles(tmp_landmark_dict))
        break

cap.release()
cv2.destroyAllWindows()