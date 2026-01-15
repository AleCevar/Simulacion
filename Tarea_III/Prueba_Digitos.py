import random
from math import pow
from scipy.stats import chi2

def continua(muestra):
    # concatenación de los números
    tam=0
    for e in muestra:
        tam=max(tam, len(e)-2)
    s = ""
    for e in muestra:
        assert(e[0]=='0' and e[1]=='.')
        s+=e[2:]
        for _ in range(tam - len(e)):
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
    if obs < cri:
        print("Se tolera la hipotesis de Digitos 🥳: ", end=" ", flush = True)
    print(obs,cri)

def discreta(muestra, base):
    # concatenacion y conteo
    mxN = base-1
    huecos = [0 for _ in range(base)]
    pos = [-1 for _ in range(base)]
    for i in range(len(muestra)):
        e=muestra[i]-1
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
    if obs < cri:
        print("Se tolera la hipotesis de Digitos 🥳: ", end=" ", flush = True)
    print(obs,cri)
