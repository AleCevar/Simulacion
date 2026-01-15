from scipy.stats import uniform

def calc(val, dif):
    fun=[uniform.cdf(val[i]+dif, loc = 0, scale = 1) - uniform.cdf(val[i], loc = 0, scale = 1) for i in range(len(val))]
    return fun