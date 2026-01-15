from scipy.stats import geom
def calc(val, prob):
    exp = sum([val[i] * prob[i] for i in range(len(val))])
    var = sum([((val[i]-exp)**2)*prob[i] for i in range(len(val))])
    p=1/(exp+1)
    fun=[geom.pmf(val[i], p) for i in range(len(val))]
    return [p, fun]
