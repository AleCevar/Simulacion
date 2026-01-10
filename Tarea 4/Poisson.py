from scipy.stats import poisson

def calc(val, prob):
    exp = sum([val[i] * prob[i] for i in range(len(val))])
    fun=[poisson.pmf(val[i], exp) for i in range(len(val))]
    print(prob)
    return [exp, fun]


