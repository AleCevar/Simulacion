from scipy.stats import chi2

def continua(muestra, m):
    inf = 0.3 * m
    sup = 0.7 * m
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
    print(obs,cri)

def discreta(muestra, m):
    continua(muestra,m)
