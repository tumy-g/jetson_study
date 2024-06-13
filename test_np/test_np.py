import numpy as np

#ベクトルの用意
A = np.array(1,0)
B = np.array(0,1)

def get_angle_vec(vec1:np.ndarray,vec2:np.ndarray):
    '''
    2つのベクトル(2次元)からなす角を求めて返す
    Arges:
        vec1,vec2:ベクトル
    '''
    #内積を計算
    dot = np.inner(vec1,vec2)
    print(f"内積:{dot}")
    
    #各ベクトルの長さを計算
    s = np.linalg.norm(vec1)
    t = np.linalg.norm(vec2)
    print(f"各ベクトルの長さは1:{s},2:{t}")

    #なす角の計算
    theta = np.arccos(dot/(s*t))
    print(f"なす角:{theta}")