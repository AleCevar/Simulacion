from scipy.stats import gamma

def calc(val, prob, dif):
    exp = sum([val[i] * prob[i] for i in range(len(val))])
    var = sum([((val[i]-exp)**2)*prob[i] for i in range(len(val))])
    b = exp / var
    a = exp * b
    fun=[gamma.cdf(val[i]+dif, a , scale = (1 / b))-gamma.cdf(val[i], a, scale = (1/b)) for i in range(len(val))]
    return [a,b,fun]