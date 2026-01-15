from scipy.stats import nbinom

def calc(val, prob):
    exp = sum([val[i] * prob[i] for i in range(len(val))])
    var = sum([((val[i]-exp)**2)*prob[i] for i in range(len(val))])
    p=exp/var
    r=exp*p/(1-p)
    fun=[nbinom.pmf(val[i], int(r), p) for i in range(len(val))]
    return r,p,fun


