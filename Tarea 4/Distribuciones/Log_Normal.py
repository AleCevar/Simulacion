from math import sqrt
import numpy as np
from scipy.stats import lognorm

def calc(val, prob, dif):
    exp = sum([val[i] * prob[i] for i in range(len(val))])
    var = sum([((val[i]-exp)**2)*prob[i] for i in range(len(val))])
    des = sqrt(var)
    s = np.exp(exp)
    fun=[lognorm.cdf(val[i]+dif, des, scale = s)-lognorm.cdf(val[i],  des, scale = s) for i in range(len(val))]
    return exp, des, fun