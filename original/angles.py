import numpy as np

def change_2D(input_list:list):
    '''
    3次元座標をz座標を取り除いて2次元座標にして返す
    '''
    result = [sublist[:2] for sublist in input_list]
    return result

def resotore_list(input_list:list):
    '''
    change_2D関数で低次元化したリストは正規化されているので復元する
    '''


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

    return theta