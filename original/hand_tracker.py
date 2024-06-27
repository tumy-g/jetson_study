# -*- coding:utf-8
import time
import cv2
import numpy as np
import mediapipe as mp

#ローカルファイル
import angles

#配列の整理などができる
from pprint import pprint

#local
from abst_detector import AbstDetector

class HandTracker(AbstDetector):
    def __init__(self, max_num_hands: int, min_detection_confidence: float, min_tracking_confidence: float) -> None:
        """初期化処理

        Args:
            max_num_hands (int): 最大検出手数
            min_detection_confidence (float): 手検出モデルの最小信頼値
            min_tracking_confidence (float): ランドマーク追跡モデルからの最小信頼値
        """
        self.tracker = mp.solutions.hands.Hands(
            max_num_hands=max_num_hands,
            min_detection_confidence=min_detection_confidence,
            min_tracking_confidence=min_tracking_confidence,
        )

    def detect(self, image: np.ndarray) -> bool:
        """手検出処理

        Args:
            image (np.ndarray): 入力イメージ

        Returns:
            bool: 手が検出できたか
        """
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        try:
            self.results = self.tracker.process(image)
        except Exception as e:
            print("Error: hand_tracker.py 39line")
        # finally:
        #     print("?座標",self.results.multi_hand_landmarks)
        return True if self.results.multi_hand_landmarks is not None else False

    def draw(self, image: np.ndarray) -> tuple:
        """一枚のフレーム画像に対して手の検出(描画)し，ランドマーク情報を返す．

        Args:
            image (np.ndarray): ベースイメージ

        Returns:
            np.ndarray: 描画済みイメージ
            dict      : ランドマークを右手と左手別々に保存する．
        """
        base_width, base_height = image.shape[1], image.shape[0]
        

        landmark_dict = {'Left':[], 'Right':[]}  # landmark_listをdict型で左手右手を取り出しやすいようにする
        landmark_color = {'Left':(205,205,205), 'Right':(205,205,205), "stress":(0,0,255)}

        for i, (hand_landmarks, handedness) in enumerate(zip(self.results.multi_hand_landmarks, self.results.multi_handedness)):
            landmark_buf = []
            # 画像を左右反転していなく右手と左手が逆になるので修正する
            hand_label = 'Left' if (handedness.classification[0].label)=='Right' else 'Right'

            for j, landmark in enumerate(hand_landmarks.landmark):
                landmark_buf.append([landmark.x, landmark.y, landmark.z])

                # 円を描く用の座標
                x = min(int(landmark.x * base_width), base_width - 1)
                y = min(int(landmark.y * base_height), base_height - 1)
                cv2.circle(image, (x, y), 4, landmark_color[hand_label], 5)
            
            for con_pair in mp.solutions.hands.HAND_CONNECTIONS:
                # 節点の始点と終点の座標を計算する．
                #u:小指の始点？　v:小指の終点？
                u = (int(np.array(landmark_buf)[con_pair[0]][0]*base_width), int(np.array(landmark_buf)[con_pair[0]][1]*base_height))
                v = (int(np.array(landmark_buf)[con_pair[1]][0]*base_width), int(np.array(landmark_buf)[con_pair[1]][1]*base_height))
                cv2.line(image, u, v, landmark_color[hand_label], 2)#手のラインを描画
                if con_pair in [(5,6), (6,7), (9,10), (10,11) ,(17,18), (18,19)]:
                    if hand_label == 'Left':
                        continue
                    cv2.line(image, u, v, landmark_color["stress"], 8)
                    if con_pair in [(6,7)]:
                        cv2.putText(image,
                                text=str(angles.get_angles(landmark_buf)[6])[0:5],
                                org=u,
                                fontFace=cv2.FONT_HERSHEY_SIMPLEX,
                                fontScale=0.3,
                                color=(0,0,0),
                                thickness=1,
                                lineType=cv2.LINE_4)
                    if con_pair in [(10,11)]:
                        cv2.putText(image,
                                text=str(angles.get_angles(landmark_buf)[10])[0:5],
                                org=u,
                                fontFace=cv2.FONT_HERSHEY_SIMPLEX,
                                fontScale=0.3,
                                color=(0,0,0),
                                thickness=1,
                                lineType=cv2.LINE_4)
                    if con_pair in [(18,19)]:
                        cv2.putText(image,
                                text=str(angles.get_angles(landmark_buf)[18])[0:5],
                                org=u,
                                fontFace=cv2.FONT_HERSHEY_SIMPLEX,
                                fontScale=0.3,
                                color=(0,0,0),
                                thickness=1,
                                lineType=cv2.LINE_4)

            # ランドマークが欠損している場合は例外処理
            if len(landmark_buf) % 21 != 0:
                print("ランドマーク欠損の恐れあり")
            
            #正規化表現のまま使用するならこっち
            landmark_dict[hand_label] = landmark_buf

        #return (image, angles.change_2D(landmark_buf))
        return (image, landmark_buf)