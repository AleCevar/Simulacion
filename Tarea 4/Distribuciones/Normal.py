from math import sqrt

from scipy.stats import norm

def calc(val, prob, dif):
    exp = sum([val[i] * prob[i] for i in range(len(val))])
    var = sum([((val[i]-exp)**2)*prob[i] for i in range(len(val))])
    des = sqrt(var)
    fun=[norm.cdf(val[i]+dif, exp, des)-norm.cdf(val[i], exp, des) for i in range(len(val))]
    print(exp, var)
    return [exp, fun]