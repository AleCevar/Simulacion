from scipy.stats import uniform
from scipy.stats import norm
from math import sqrt

def calc(val, prob, dif):
    mx=max(prob)
    exp=0
    for i in range(len(prob)):
        if prob[i]>=mx:
            exp=val[i]
    des=0.37
    fun = [2*(norm.cdf(val[i] + dif, exp, des) - norm.cdf(val[i], exp, des)) for i in range(len(val))]
    for i in range(len(val)):
        if val[i]<=1:
            fun[i]=0.00065
    print(exp, des)
    return [exp, fun]
    # exp = sum([val[i] * prob[i] for i in range(len(val))])
    # var = sum([((val[i]-exp)**2)*prob[i] for i in range(len(val))])
    # a = (2*exp - sqrt(12*var)) / 2
    # b = sqrt(12*var) + a
    # fun=[uniform.cdf(val[i]+dif, loc = a, scale = b - a) - uniform.cdf(val[i], loc = a, scale = b - a) for i in range(len(val))]
    # print(exp, var)
    # return [exp, fun]


# v = (b-a)^2 / 12
# e = (a+b) / 2
#
# 12v = (b - a)^2
#
# sqrt(12v) = b - a
#
# sqrt(12v) + a = b
#
# e = a + sqrt(12v) + a / 2
# 2e = 2a + sqrt(12v)
# 2e - sqrt(12v) / 2 = a
