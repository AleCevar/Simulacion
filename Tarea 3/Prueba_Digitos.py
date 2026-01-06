from math import pow
from scipy.stats import chi2
from random import randint

def continua(muestra):
    # concatenación de los números
    tam=0
    for e in muestra:
        xx=str(e)
        assert(xx[0]=='0' and xx[1]=='.')
        tam=max(tam, len(xx)-2)
    s = ""
    for e in muestra:
        xx = str(e)[2:]
        s+=xx
        for _ in range(tam - len(xx)):
            s += '0'
    # conteo de huecos
    mxN=7
    huecos = [0 for _ in range(mxN+1)]
    pos = [-1 for _ in range(10)]
    for i in range(len(s)):
        c = int(s[i])
        if pos[c] != -1:
            huecos[min(i - pos[c] - 1, mxN)]+=1
        pos[c] = i
    # calculos
    pe = [0.1 * pow(0.9, i) for i in range(mxN+1)]
    pe[mxN] = pow(0.9, mxN)
    n = sum(huecos)
    fe = [n * pe[i] for i in range(mxN+1)]
    ans = [pow(fe[i] - huecos[i], 2) / fe[i]  for i in range(mxN+1)]
    obs = sum(ans)
    cri = chi2.ppf(1-0.05,9)
    print(obs,cri)

def discreta(muestra, base):
    # concatenacion y conteo
    mxN = base-1
    huecos = [0 for _ in range(mxN+1)]
    pos = [-1 for _ in range(base)]
    for i in range(len(muestra)):
        e=muestra[i]
        if e==base:
            e=0
        if pos[e]!=-1:
            huecos[min(mxN, i-pos[e]-1)]+=1
        pos[e]=i
    # calculos
    pe = [(1 / base) * pow((base - 1) / base, i) for i in range(mxN + 1)]
    pe[mxN]=pow((base-1)/base, mxN)
    n=sum(huecos)
    fe = [n * pe[i] for i in range(mxN+1)]
    ans = [pow(fe[i] - huecos[i], 2) / fe[i]  for i in range(mxN+1)]
    obs = sum(ans)
    cri = chi2.ppf(1-0.05,base-1)
    print(obs,cri)

ar=[]
for i in range(30):
    ar.append(randint(1, 10))
discreta(ar, 10)