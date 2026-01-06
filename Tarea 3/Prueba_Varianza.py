from scipy.stats import chi2
import numpy as np

def varianzaDis(l, r):
    sum=0
    for i in range(l, r+1):
        sum+=i*i-i+0.25
    return sum

def varianzaCon():
    return 1/12

def continua(muestra):
    n = len(muestra)
    aux = varianzaCon() / (n-1)
    Linf = chi2.ppf(0.05/2,n-1)*aux
    Lsup = chi2.ppf(1-(0.05/2),n-1)*aux
    mean = np.var(np.array(muestra))
    print(Linf, mean, Lsup)

def discreta(l,r,muestra):
    n = len(muestra)
    aux = varianzaDis(l,r) / (n - 1)
    Linf = chi2.ppf(0.05 / 2, n - 1) * aux
    Lsup = chi2.ppf(1-(0.05/2),n-1)*aux
    mean = np.var(np.array(muestra))
    print(Linf, mean, Lsup)

ar = []
for _ in range(30):
    ar.append(float(input()))

continua(ar)