import time
import sys
import cv2
import mediapipe as mp
mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands

video_source = "/dev/video0"# or /dev/vdieo1

# ウェブカメラのキャプチャを開始
print("capture start")
cap = cv2.VideoCapture(video_source)
time.sleep(2)
# キャプチャがオープンしている間続ける
while(cap.isOpened()):
    # フレームを読み込む
    ret, frame = cap.read()
    if not ret:
        print("Camera Error.")
        
    if ret == True:
        # フレームを表示
        cv2.imshow('Webcam Live', frame)

        # 'q'キーが押されたらループから抜ける
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

# キャプチャをリリースし、ウィンドウを閉じる
cap.release()
cv2.destroyAllWindows()