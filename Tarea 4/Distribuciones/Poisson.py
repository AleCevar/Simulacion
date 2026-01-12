from scipy.stats import poisson

def calc(val, prob):
    exp = sum([val[i] * prob[i] for i in range(len(val))])
    exp = 4.2
    fun=[poisson.pmf(val[i], exp) for i in range(len(val))]
    return [exp, fun]


