from scipy.stats import t

def calc(val, prob, cor):
    exp = sum([val[i] * prob[i] for i in range(len(val))])
    var = sum([((val[i]-exp)**2)*prob[i] for i in range(len(val))])
    lib = (2 * var) / (var - 1)
    fun=[t.cdf(val[i]+cor, lib)-t.cdf(val[i], lib) for i in range(len(val))]
    return [lib, fun]