# -*- coding:utf-8

def formula(angle1,angle2,angle3)->float:
    '''
    3つのなす角をLassoの回帰直線式にあてはめ、その結果をリターンする
    '''
    y = 1.457 - 0.001138*angle1 - 0.001883*angle2 - 0.002875*angle3
    return y