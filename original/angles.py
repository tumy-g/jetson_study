import numpy as np

#いらないかも
def formatDict(inputList,width,height):
    result = {}
    for i, sublist in enumerate(inputList):
        result[str(i)] = {'x':sublist[0]*width,'y':sublist[1]*height}

    return result

def change_2D(input_list:list):
    '''
    3次元座標をz座標を取り除いて2次元座標にして返す
    '''
    result = [sublist[:2] for sublist in input_list]
    return result

def get_angle_vec(vec1:np.ndarray,vec2:np.ndarray):
    '''
    2つのベクトル(2次元)からなす角を求めて返す
    Arges:
        vec1,vec2:ベクトル np.array([1,0])のような形式
    '''
    #内積を計算
    dot = np.inner(vec1,vec2)
    
    #各ベクトルの長さを計算
    s = np.linalg.norm(vec1)
    t = np.linalg.norm(vec2)

    #なす角の計算
    theta = np.arccos(dot/(s*t))

    return theta

def calc_vectors(input_list:list):
    '''
    lists2D形式のリストから、それぞれの座標をベクトル化し、計20個のベクトルをリストにまとめ、リターンする
    Args:
        input_list: lists2D形式のリスト
    '''
    vectors = [np.array(coord) for coord in input_list]

    return vectors

def calc_angles(vectors):
    '''
    calc_vectorsによってベクトル化されたベクトルたちから指定されたインデックスの指ベクトルのなす角を返す
    Args:
        vectors: calc_vectors()の返り値
    Return:
        dots: 各ベクトルの内積
        thetas: 各ベクトルのなす角
    '''
    dots = []#内積達
    thetas = []#なす角たち

    for i in range((len(vectors)-1)):
        #内積
        dot = np.inner(vectors[i], vectors[i+1])
        dots.append(dot)
        #ベクトルの長さ(norm)
        norm1 = np.linalg.norm(vectors[i])
        norm2 = np.linalg.norm(vectors[i+1])
        #なす角
        theta = np.arccos(dot/(norm1*norm2))
        thetas.append(theta)

    return dots, thetas

def get_angles(landmarks:list):
    '''
    関数のネストになるのを回避するため、この関数を呼び出すだけでいいように
    Args:
        landmarks: list2D.txt形式のリスト。landmarks(2次元)の座標がまとめられている
    Return:
        result: 各ベクトルのなす角(計20個)をまとめたリスト
    '''
    hoge, result = calc_angles(calc_vectors(landmarks))

    return result