import time
import sys
import cv2
import mediapipe as mp
mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands

video_source = "/dev/video0"

# Webカメラ入力の場合：
cap = cv2.VideoCapture(video_source)
print("start camera")
time.sleep(2)
with mp_hands.Hands(
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5) as hands:
  while cap.isOpened():
    ret, image = cap.read()
    if not ret:
      print("Ignoring empty camera frame.")
      # ビデオをロードする場合は、「continue」ではなく「break」を使用してください
      continue

    # 後で自分撮りビューを表示するために画像を水平方向に反転し、BGR画像をRGBに変換
    image = cv2.cvtColor(cv2.flip(image, 1), cv2.COLOR_BGR2RGB)
    # パフォーマンスを向上させるために、オプションで、参照渡しのためにイメージを書き込み不可としてマーク
    image.flags.writeable = False
    results = hands.process(image)

    # 画像に手のアノテーションを描画
    image.flags.writeable = True
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
    if results.multi_hand_landmarks:
      for hand_landmarks in results.multi_hand_landmarks:
        mp_drawing.draw_landmarks(
            image, hand_landmarks, mp_hands.HAND_CONNECTIONS)
    cv2.imshow('MediaPipe Hands', image)
    if cv2.waitKey(5) & 0xFF == 27:
      break
cap.release()