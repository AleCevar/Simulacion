from scipy.stats import chi2
from scipy.stats import poisson

def fix(fe, fo, m) :
    afe = [0]
    afo = [0]
    for i in range(m-1,-1,-1):
        if fe[i] < 5 or afe[-1] < 5:
            afe[-1] += fe[i]
            afo[-1] += fo[i]
        else:
            afe.append(fe[i])
            afo.append(fo[i])
    afe.reverse()
    afo.reverse()
    return afe, afo

def test(fo, pe, est):
    n = sum(fo)
    fe = [n * x for x in pe]
    fe, fo = fix(fe, fo, len(fe))
    assert all(f >= 5 for f in fe)
    m = len(fe)
    assert(len(fo)==m)
    obs = sum([((fo[i]-fe[i])**2)/fe[i] for i in range(m)])
    cri = chi2.ppf(1-0.05,m-1-est)
    if obs < cri:
        print("Se tolera:", end=" ")
    print(obs, cri)
    # print(fo)
    # print(fe)
    print(m)
    return obs,cri
#
# fo = [25,55,65,35,20,10]
# pe = [poisson.pmf(i, 2) for i in range(6)]
#
# test(fo,pe,2)