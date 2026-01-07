from math import comb, pow
from scipy.stats import chi2
import random

def clasi(s, base) :
    assert (len(s) == 5)
    ar = [0 for _ in range(base)]
    for e in s:
        ar[int(e)] += 1
    unos = ar.count(1)
    dos = ar.count(2)
    ceros = ar.count(0)
    tres = ar.count(3)
    cuatros = ar.count(4)
    cincos = ar.count(5)
    if dos == 1 and unos == 3: return 1
    if dos == 2 and unos == 1: return 2
    if tres == 1 and unos == 2: return 3
    if tres == 1 and dos == 1: return 4
    if cuatros == 1 and unos == 1 : return 5
    if cincos == 1 :  return 6
    assert(unos == 5)
    return 0

def continua(muestra) :
    manos = [0 for _ in range(7)]
    for e in muestra:
        xx = e
        for z in range(max(0, 7-len(xx))):
            xx+='0'
        xx=xx[2:7]
        manos[clasi(xx,10)] += 1
    pe = [0 for _ in range(7)]
    aux=int(1e5)
    pe[0] = (10 * 9 * 8 * 7 * 6) / aux
    pe[1] = (10 * 9 * 8 * 7) / aux * comb(5,2)
    pe[2] = (10 * 9 * 8) / aux * comb(5,2) * comb(3,2) / 2
    pe[3] = (10 * 9 * 8) / aux * comb(5,3)
    pe[4] = (10 * 9) / aux * comb(5,3)
    pe[5] = (10 * 9) / aux * comb(5,4)
    pe[6] = 10 / aux
    n = sum(manos)
    fe = [pe[i] * n for i in range(7)]
    ans = [pow(fe[i]-manos[i], 2)/fe[i] for i in range(7)]
    obs = sum(ans)
    cri = chi2.ppf(1-0.05, 6)
    if obs < cri:
        print("Se tolera la hipotesis de Poker 🥳: ", end=" ", flush = True)
    print(obs, cri)

def discreta(muestra, base) :
    s = []
    for e in muestra:
        s.append(e-1)
    manos = [0 for _ in range(7)]
    for i in range(0, len(muestra), 5):
        manos[clasi([s[i+j] for j in range(5)], base)] += 1
    pe = [0 for _ in range(7)]
    aux = pow(base,5)
    pe[0] = base *  (base - 1) * (base - 2) * (base-3) * (base - 4) / aux
    pe[1] = base * (base - 1) * (base - 2) * (base - 3) / aux * comb(5,2)
    pe[2] = base * (base - 1) * (base - 2) / aux * comb(5,2) * comb(3,2) / 2
    pe[3] = base * (base - 1) * (base - 2) / aux * comb(5,3)
    pe[4] = base * (base - 1) / aux * comb(5,3)
    pe[5] = base * (base - 1) / aux * comb(5,4)
    pe[6] = base / aux
    n = sum(manos)
    fe = [pe[i] * n for i in range(7)]
    ans = [pow(fe[i]-manos[i], 2)/fe[i] for i in range((fe[0] == 0),7)]
    obs = sum(ans)
    cri = chi2.ppf(1-0.05, len(ans)-1)
    if obs < cri:
        print("Se tolera la hipotesis de Poker 🥳: ", end=" ", flush = True)
    print(obs, cri)
