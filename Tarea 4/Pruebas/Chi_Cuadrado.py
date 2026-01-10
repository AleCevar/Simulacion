from scipy.stats import chi2
import Pruebas.Grafico_Chi_Cuadrado as gchi
from scipy.stats import poisson

def test(fo, pe):
    n = sum(fo)
    m = len(fo)
    fe = [n * x for x in pe]
    obs = sum([((fo[i]-fe[i])**2)/fe[i] for i in range(m)])
    cri = chi2.ppf(1-0.05,m-2)
    if obs < cri:
        print("Se tolera:", end=" ")
    print(obs, cri)
    gchi.mostrar(obs,m-2)

# fo = [25,55,65,35,20,10]
# pe = [poisson.pmf(i, 2) for i in range(6)]
#
# test(fo,pe)