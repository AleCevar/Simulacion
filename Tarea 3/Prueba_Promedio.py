from math import sqrt
from numpy.ma.extras import average
from scipy.stats import norm

def desviacionDis(l, r):
    sum=0
    for i in range(l, r+1):
        sum+=i*i-i+0.25
    return sqrt(sum)

def desviacionCon():
    return sqrt(1/12)

def discretaU(l ,r):
    res = 0
    for i in range(l,r+1):
        res += i * (1 / r-l+1)
    return res

def contiU():
    return 1/2

def continua(muestra):
    n=len(muestra)
    aux = norm.ppf(0.05/2)*(desviacionCon() / sqrt(n))
    media = contiU()
    Linf = media + aux
    Lsup = media - aux
    mean = average(muestra)
    print(Linf, mean, Lsup)

def discreta(l, r, muestra):
    n = len(muestra)
    aux = norm.ppf(0.05 / 2) * (desviacionDis(l,r) / sqrt(n))
    media = discretaU(l, r)
    Linf = media + aux
    Lsup = media - aux
    mean = average(muestra)
    print(Linf, mean, Lsup)
