from scipy.stats import kstwobign
from math import sqrt
from scipy.stats import poisson

def imprimir(ar):
    m=len(ar)
    n=min(len(ar[0]), 25)
    for i in range(n):
        for j in range(m):
            print(f"{ar[j][i]:2.f}",end=" ")
        print()

def test(pfo, ppe):
    fo = pfo.copy()
    pe= ppe.copy()
    pea = pe
    m = len(fo)
    n = sum(fo)
    for i in range(1, m):
        pea[i] += pea[i-1]
    foa = fo
    for i in range(1, m):
        foa[i] += foa[i-1]
    poa = [x/n for x in foa]
    abs_oe = [abs(poa[i]-pea[i]) for i in range(m)]
    obs = max(abs_oe)
    cri = kstwobign.ppf(1-0.05) / sqrt(n)
    if obs < cri:
        print("Se tolera:",end=" ")
    print(obs,cri)
    #imprimir([fo, foa, pe, pea, poa, abs_oe])

# fo = [25,55,65,35,20,10]
# pe = [poisson.pmf(i, 2) for i in range(6)]
#
# test(fo,pe)
