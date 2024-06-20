import numpy as np

def dif_vector(vec1:np.ndarray, vec2:np.ndarray):
    '''
    2つのベクトルの差ベクトルを算出
    Args:
        vec1:始点のベクトル
        vec2:終点のベクトル
    '''
    return vec2 - vec1

A = np.array([5,5])
B = np.array([1,1])

hoge = dif_vector(A, B)

print(hoge)