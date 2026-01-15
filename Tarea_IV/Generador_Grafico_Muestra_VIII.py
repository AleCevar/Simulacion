import math
import Graficador.Grafico_Chi_Cuadrado as gchi
import Graficador.Graficador_Distribuciones as grf
import Distribuciones.Normal as norm
import Pruebas.Chi_Cuadrado as chi
import Pruebas.Kolmogorov_Smirnov as kol

name = "Muestras/m8.txt"
freq= dict()
n=0

with open(name, "r", encoding="utf-8") as f:
    for l in f:
        n+=1
        num = math.trunc(float(l) * 100) / 100
        freq[num] = freq.get(num, 0) + 1

x=[]
y=[]
for a, b in sorted(freq.items()):
    x.append(a)
    y.append(b)

prob = [j / n for j in y]

grf.relativa(x,prob)
grf.absoluta(x,y)

[mu,sigma, fun] = norm.calc(x, prob, 0.01)

grf.distribucion(x,fun,"Histograma de " +  r"$X\sim \mathcal{{N}}$ (" + str(mu) + " , " + str(sigma) + ")")
grf.comparacion(x,prob,fun,rf"Densidad $X \sim \mathcal{{N}}(\mu,\sigma)$","Comparación con " + r"$X \sim \mathcal{{N}}$ (" + str(mu) + " , " + str(sigma) + ")")

obs, cri ,df = chi.test(y,fun,2)
kol.test(y,fun)
gchi.mostrar(obs, df - 1 -2)