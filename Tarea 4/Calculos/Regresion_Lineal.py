import numpy as np
from math import log, pow

def calc(x, y):
    x_ = np.array([log(z) for z in x])
    y_ = np.array([log(z) for z in y])
    b,m = np.polyfit(x_,y_,1)
    a = np.exp(m)
    fun = [a*pow(z,b) for z in x]
    print(a,b)
    return a,b,fun