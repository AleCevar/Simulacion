import Graficador.Grafico_Chi_Cuadrado as gchi
import Graficador.Graficador_Distribuciones as grf
import Pruebas.Chi_Cuadrado as chi
import Pruebas.Kolmogorov_Smirnov as kol

import Distribuciones.Normal as norm
import Distribuciones.Binomial_Negativa as nbinom
import Distribuciones.Chi_Square as chi2
import Distribuciones.Gamma as gamma
import Distribuciones.Poisson as poiss
import Distribuciones.Weibull as wei

name = "Muestras/m4.txt"
freq= dict()
n=0

with open(name, "r", encoding="utf-8") as f:
    for l in f:
        n+=1
        num = int(l)
        freq[num] = freq.get(num, 0) + 1

x=[]
y=[]
for a, b in sorted(freq.items()):
    x.append(a)
    y.append(b)

prob = [j / n for j in y]

grf.relativa(x, prob)
grf.absoluta(x, y)

lamb, fun = poiss.calc(x,prob)
grf.distribucion(x,fun,rf"Histograma de X $\sim$ Poi({lamb})")
grf.comparacion(x,prob,fun,rf"Densidad de X $\sim Poi(\lambda)$",r"Comparación con X $\sim Poi(\lambda)$")
obs, cri, df = chi.test(y,fun,1)
kol.test(y,fun)
gchi.mostrar(obs,df - 1 - 1)

r, p, fun = nbinom.calc(x,prob)
grf.distribucion(x,fun,rf"Histograma de X $\sim$ BN({r}, {p})")
grf.comparacion(x,prob,fun,rf"Densidad de X $\sim BN(r,p)$",rf"Comparación con X $\sim BN(r,p)$")
obs, cri, df = chi.test(y,fun,2)
kol.test(y,fun)
gchi.mostrar(obs,df - 1 - 2)

v, fun = chi2.calc(x,prob,1)
grf.distribucion(x,fun,rf"Histograma de X $\sim \chi^2$ (" + str(v) + ")")
grf.comparacion(x,prob,fun,rf"Densidad de X $\sim \chi^2(\nu)$",rf"Comparación con X $\sim \chi^2(\nu)$")
obs, cri, df = chi.test(y,fun,1)
kol.test(y,fun)
gchi.mostrar(obs,df - 1 - 1)

a,b,fun = gamma.calc(x,prob,1)
grf.distribucion(x,prob,rf"Histograma de $X \sim \Gamma({a}, {b})$")
grf.comparacion(x,prob,fun,r"$Densidad de X \sim \Gamma(\alpha,\beta)$", r"$Comparación con X \sim \Gamma(\alpha,\beta)$")
obs, cri, df = chi.test(y,fun,2)
kol.test(y,fun)
gchi.mostrar(obs,df - 1 - 2)

mu,sigma,fun = norm.calc(x,prob,1)
grf.distribucion(x,fun,"Histograma de " +  r"$X\sim \mathcal{{N}}$ (" + str(mu) + " , " + str(sigma) + ")")
grf.comparacion(x,prob,fun,rf"Densidad $X \sim \mathcal{{N}}(\mu,\sigma)$","Comparación con " + r"$X \sim \mathcal{{N}}$ (" + str(mu) + " , " + str(sigma) + ")")
obs, cri, df = chi.test(y,fun,2)
kol.test(y,fun)
gchi.mostrar(obs,df - 1 - 2)

a, l , fun = wei.calc(x,prob,1)
grf.distribucion(x,fun,rf"Histograma de $X \sim Weibull({a},{l})$")
grf.comparacion(x,prob,fun,r"$Densidad de X \sim Weibull(\alpha,\lambda)$",r"$Comparación con X \sim Weibull(\alpha,\lambda)$")
obs, cri, df = chi.test(y,fun,2)
kol.test(y,fun)
gchi.mostrar(obs,df - 1 - 2)