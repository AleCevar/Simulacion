
from scipy.special import gamma
from scipy.optimize import fsolve
from scipy.stats import weibull_min

def eq_k(k, mu, var):
    lhs = var / mu**2
    rhs = gamma(1 + 2/k) / gamma(1 + 1/k)**2 - 1
    return rhs - lhs

def weibull_params(mu, var):
    k0 = 1.5
    k = fsolve(eq_k, k0, args=(mu, var))[0]

    lam = mu / gamma(1 + 1/k)
    return k, lam

def calc(val, prob, dif):
    exp = sum([val[i] * prob[i] for i in range(len(val))])
    var = sum([((val[i]-exp)**2)*prob[i] for i in range(len(val))])
    [k , l] = weibull_params(exp, var)
    fun=[weibull_min.cdf(val[i]+dif, k, scale = l )-weibull_min.cdf(val[i], k, scale = l) for i in range(len(val))]
    print(exp, var)
    return [k,l, fun]