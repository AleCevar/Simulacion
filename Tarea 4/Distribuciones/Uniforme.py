from scipy.stats import uniform

def calc(val, prob, dif):
    # exp = sum([val[i] * prob[i] for i in range(len(val))])
    # var = sum([((val[i]-exp)**2)*prob[i] for i in range(len(val))])
    # a = 1 / 2
    # b = 1 / 12
    fun=[uniform.cdf(val[i]+dif, loc = 0, scale = 1) - uniform.cdf(val[i], loc = 0, scale = 1) for i in range(len(val))]
    # print(exp, var)
    return [1, fun]