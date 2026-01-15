
from scipy.stats import chi2

def continua(mm):
    muestra = [float(e) for e in mm] # ojo aca para discretos
    inf = 0.3
    sup = 0.7
    t=0.4
    last = -1
    mxN = 3
    huecos = [0 for _ in range(mxN+1)]
    for i in range(len(muestra)):
        if inf <= muestra[i] <= sup:
            if last != -1 :
                huecos[min(i - last - 1, mxN)] += 1
            last = i
    pe=[t*pow(1 - t, i) for i in range(mxN+1)]
    pe[mxN] = pow(1 - t, mxN)
    n = sum(huecos)
    fe = [pe[i] * n for i in range(mxN+1)]
    ans = [pow(fe[i] - huecos[i], 2) / fe[i] for i in range(mxN+1)]
    obs = sum(ans)
    cri = chi2.ppf(1 - 0.05, mxN)
    if obs < cri:
        print("Se tolera la hipotesis de Numeros 🥳: ", end=" ",  flush = True)
    print(obs,cri)

def discreta(muestra, m):
    inf = 3
    sup = min(m, inf+m//3)
    t=(sup-inf+1)/m
    last = -1
    mxN = 3
    huecos = [0 for _ in range(mxN+1)]
    for i in range(len(muestra)):
        if inf <= muestra[i] <= sup:
            if last != -1 :
                huecos[min(i - last - 1, mxN)] += 1
            last = i
    pe=[t*pow(1 - t, i) for i in range(mxN+1)]
    pe[mxN] = pow(1 - t, mxN)
    n = sum(huecos)
    fe = [pe[i] * n for i in range(mxN+1)]
    ans = [pow(fe[i] - huecos[i], 2) / fe[i] for i in range(mxN+1)]
    obs = sum(ans)
    cri = chi2.ppf(1 - 0.05, mxN)
    if obs < cri:
        print("Se tolera la hipotesis de Numeros 🥳: ", end=" ",  flush = True)
    print(obs,cri)

