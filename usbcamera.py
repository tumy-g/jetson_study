import time
import sys
import cv2
import mediapipe as mp
mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands

video_source = "/dev/video0"
def gstreamer_pipeline(
    capture_width=3264,
    capture_height=2464,
    display_width=3264,
    display_height=2464,
    framerate=21,
    flip_method=0,
):
    return (
        "nvarguscamerasrc ! "
        "video/x-raw(memory:NVMM), "
        "width=(int)%d, height=(int)%d, "
        "format=(string)NV12, framerate=(fraction)%d/1 ! "
        "nvvidconv flip-method=%d ! "
        "video/x-raw, width=(int)%d, height=(int)%d, format=(string)BGRx ! "
        "videoconvert ! "
        "video/x-raw, format=(string)BGR ! appsink"
        % (
            capture_width,
            capture_height,
            framerate,
            flip_method,
            display_width,
            display_height,
        )
    )


# ウェブカメラのキャプチャを開始
print("capture start")
cap = cv2.VideoCapture(1)
time.sleep(2)
# キャプチャがオープンしている間続ける
while(cap.isOpened()):
    # フレームを読み込む
    ret, frame = cap.read()
    if not ret:
        print("Camera Error.")
        continue
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
