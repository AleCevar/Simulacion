from scipy.stats import chi2

def calc(val, prob, dif):
    exp = sum([val[i] * prob[i] for i in range(len(val))])
    fun=[chi2.cdf(val[i]+dif, exp)-chi2.cdf(val[i], exp) for i in range(len(val))]
    print(exp)
    return [exp, fun]