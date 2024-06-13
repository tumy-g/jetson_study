import numpy as np

def calc_vectors(input_list:list):
    '''
    lists2D形式のリストから、それぞれの座標をベクトル化し、計20個のベクトルをリストにまとめ、リターンする
    '''
    vectors = [np.array(coord) for coord in input_list]

    return vectors

def calc_angles(vectors):
    '''
    calc_vectorsによってベクトル化されたベクトルたちから指定されたインデックスの指ベクトルのなす角を返す
    '''
    dots = []#内積達
    thetas = []#なす角たち

    for i in range(len(vectors)-1):
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

def main_function():
    test_list = [
 [0.3927159607410431, 0.37190449237823486],
 [0.3384940028190613, 0.3625722825527191],
 [0.30138999223709106, 0.3885597586631775],
 [0.27090194821357727, 0.4090009331703186],
 [0.22865509986877441, 0.43009957671165466],
 [0.4008617699146271, 0.44493186473846436],
 [0.4225102365016937, 0.5078729391098022],
 [0.43870100378990173, 0.5531333088874817],
 [0.4637891352176666, 0.5848085284233093],
 [0.448871910572052, 0.4403536319732666],
 [0.4924505949020386, 0.4873035252094269],
 [0.5273154973983765, 0.5123393535614014],
 [0.568734347820282, 0.5198787450790405],
 [0.48464328050613403, 0.42508283257484436],
 [0.5331290364265442, 0.45819219946861267],
 [0.5682750344276428, 0.4719351828098297],
 [0.6056236624717712, 0.4714403450489044],
 [0.5104908347129822, 0.3960573375225067],
 [0.5564172863960266, 0.4164128601551056],
 [0.5920981168746948, 0.4148552715778351],
 [0.6310437321662903, 0.4031316041946411]
]
    dots, thetas = calc_angles(calc_vectors(test_list))

    print(len(thetas))
    print(thetas)

main_function()