from scipy.stats import norm
from math import sqrt

def less(a, b):
    if a<=b:
        return 1
    return 0

def continua(muestra):
    n = len(muestra)
    h = 0
    ant=-1
    for i in range(1, n):
        if ant!=less(muestra[i-1],muestra[i]):
            h+=1
        ant = less(muestra[i-1], muestra[i])
    e = (2 * n - 1) / 3
    d = sqrt((16*n - 29) / 90)
    z0 = (h - e) / d
    inf = norm.ppf(0.05/2)
    sup = norm.ppf(1-0.05/2)
    print(inf, z0, sup)

def discreta(muestra):
    continua(muestra)
