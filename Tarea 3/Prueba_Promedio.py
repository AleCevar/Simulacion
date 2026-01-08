import random
from math import sqrt
from numpy.ma.extras import average
from scipy.stats import norm

def desviacionDis(l, r):
    n = r - l + 1
    sum = (n * n - 1) / 12
    return sqrt(sum)

def desviacionCon():
    return sqrt(1/12)

def discretaU(l ,r):
    res = 0
    for i in range(l,r+1):
        res += i
    return res/(r-l+1)

def contiU():
    return 1/2

def continua(mm):
    muestra = [float(e) for e in mm]
    n=len(muestra)
    aux = norm.ppf(0.05/2)*(desviacionCon() / sqrt(n))
    media = contiU()
    Linf = media + aux
    Lsup = media - aux
    mean = average(muestra)
    if Linf < mean < Lsup:
        print("Se tolera la hipotesis de Promedio 🥳: ", end=" ", flush = True)
    print(Linf, mean, Lsup)

def discreta(l, r, muestra):
    n = len(muestra)
    aux = norm.ppf(0.05 / 2) * (desviacionDis(l,r) / sqrt(n))
    media = discretaU(l, r)
    Linf = media + aux
    Lsup = media - aux
    mean = average(muestra)
    if Linf < mean < Lsup:
        print("Se tolera la hipotesis de Promedio 🥳: ", end=" ", flush = True)
    print(Linf, mean, Lsup)

