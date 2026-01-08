from scipy.stats import chi2
import random

def continua(mm, st=0.2, c=5):
    muestra = [float(e) for e in mm]
    cuad = [[0 for _ in range(c)] for _ in range(c)]
    lim=[st*x for x in range(c)]
    for i in range(len(muestra)-1):
        x, y=[muestra[i], muestra[i+1]]
        ar=[-1, -1]
        for j in range(c):
            if x>=lim[j]:
                ar[0]=j
            if y>=lim[j]:
                ar[1]=j
        assert (ar[0] != -1 and ar[1] != -1)
        cuad[ar[0]][ar[1]]+=1
    fe = (len(muestra) - 1) / (c*c)
    ans = [[((fe - cuad[i][j]) ** 2)/fe for i in range(c)] for j in range(c)]
    obs = sum([sum(row) for row in ans])
    cri = chi2.ppf(1 - 0.05, (c*c) - 1)
    if obs<cri:
        print("Se tolera la hipotesis de Serie 🥳: ", end=" ", flush = True)
    print(obs,cri)

def discreta(muestra, base):
    assert(base%2==0)
    mm = [e - 1 for e in muestra]
    continua(mm, 2, base // 2)
