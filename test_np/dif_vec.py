# -*- coding:utf-8

import numpy as np
import math
def get_angle_vec(vec1:np.ndarray,vec2:np.ndarray):
    '''
    2つのベクトルからなす角を求めて返す
    Arges:
        vec1,vec2:ベクトル np.array([1,0,0])のような形式
    '''
    #内積を計算
    dot = np.inner(vec1,vec2)
    
    #各ベクトルの長さを計算
    s = np.linalg.norm(vec1)
    t = np.linalg.norm(vec2)

    #なす角の計算
    theta = np.arccos(dot/(s*t))

    return theta

A = np.array([5,0])
B = np.array([0,1])
C = np.array([10,10])

hoge1 = B - A
hoge2 = B - C

theta_rad = get_angle_vec(A,B)
theta_deg = math.degrees(theta_rad)

print(theta_deg)