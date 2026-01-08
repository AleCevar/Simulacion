from scipy.stats import norm
from math import sqrt
import random

def less(a, b):
    if a<=b: return 1
    return 0

def continua(mm):
    muestra = [float(e) for e in mm]
    n = len(muestra) - 1
    h = 0
    ant=-1
    for i in range(1, len(muestra)):
        if ant!=less(muestra[i-1],muestra[i]):
            h+=1
        ant = less(muestra[i-1], muestra[i])
    e = (2 * n - 1) / 3
    d = sqrt((16*n - 29) / 90)
    z0 = (h - e) / d
    inf = norm.ppf(0.05/2)
    sup = norm.ppf(1-(0.05/2))
    if inf < z0 < sup:
        print("Se tolera la hipotesis de Corrida 🥳: ", end=" ", flush = True)
    print(inf, z0, sup)


def chg(med , x) :
    return med < x

def discreta(muestra , base):
    med = (base + 1) / 2
    mn = 0
    my = 0
    h = 0
    ant = -1
    m = len(muestra)
    for i in range(0, len(muestra)):
        if ant != chg(med, muestra[i]):
            h += 1
        ant = chg(med, muestra[i])
        if ant : my+=1
        else : mn += 1
    e = 2 * mn * my / m  + 1
    d = sqrt( (2 * mn * my * (2 * mn * my - m)) / (m*m*(m-1)) )
    z0 = (h - e) / d
    inf = norm.ppf(0.05 / 2)
    sup = norm.ppf(1 - (0.05 / 2))
    if inf < z0 < sup:
        print("Se tolera la hipotesis de Corrida 🥳: ", end=" ", flush=True)
    print(inf, z0, sup)
