import random
from scipy.stats import chi2
import numpy as np

def varianzaDis(l, r):
    n = r - l + 1
    return (n*n-1) / 12

def varianzaCon():
    return 1/12

def continua(mm):
    muestra=[float(e) for e in mm]
    n = len(muestra)
    aux = varianzaCon() / (n-1)
    Linf = chi2.ppf(0.05/2,n-1)*aux
    Lsup = chi2.ppf(1-(0.05/2),n-1)*aux
    mean = np.var(np.array(muestra))
    if Linf < mean < Lsup:
        print("Se tolera la hipotesis de varianza 🥳: ", end=" ", flush = True)
    print(Linf, mean, Lsup)

def varMues(x):
    z=sum(x)/len(x)
    ss=0
    for e in x:
        ss+=(e-z)**2
    return ss/(len(x)-1)

def discreta(l,r,muestra):
    n = len(muestra)
    Linf = chi2.ppf(0.05 / 2, n-1)
    Lsup = chi2.ppf(1-(0.05/2), n-1)
    obs = varMues(muestra)*(n-1)/varianzaDis(l, r)
    if Linf < obs < Lsup:
        print("Se tolera la hipotesis de varianza 🥳: ", end=" ",  flush = True)
    print(Linf, obs, Lsup)
