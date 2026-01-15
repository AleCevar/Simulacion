import math
import Pruebas.Chi_Cuadrado as chi
import Pruebas.Kolmogorov_Smirnov as kol
import Calculos.Regresion_Lineal as reg
import Graficador.Graficador_Distribuciones as grf
import Graficador.Grafico_Chi_Cuadrado as gchi
import matplotlib.pyplot as plt

name = "Muestras/m16.txt"
freq= dict()
n=0

with open(name, "r", encoding="utf-8") as f:
    for l in f:
        n+=1
        num = float(l)
        freq[num] = freq.get(num, 0) + 1


x=[]
y=[]
for a, b in sorted(freq.items()):
    x.append(a)
    y.append(b)

prob = [j / n for j in y]

al,be, fun = reg.calc(x, prob)
clases=dict()
claori=dict()
for i in range(len(x)):
    num=math.trunc(float(x[i]) * 100) / 100
    clases[num] = clases.get(num, 0) + fun[i]
    claori[num] = claori.get(num, 0) + y[i]

pe=[]
fo=[]
xmod=[]

for a, b in sorted(clases.items()):
    pe.append(b)
    xmod.append(a)

for a, b in sorted(claori.items()):
    fo.append(b)

aux = [z/n for z in fo]

grf.relativa(xmod, aux)
grf.absoluta(xmod,fo)

grf.distribucion(xmod,pe,rf"Histograma de $f(x) = {al} \times x^{{{be}}}$")
grf.comparacion(xmod, aux, pe, r"Densidad $f(x) = \alpha \times x^{\beta}$", r"Comparación con $f(x) = \alpha \times x^{\beta}$")

plt.plot(xmod, aux, alpha=0.4, color='yellow', label="Muestra")
plt.plot(xmod, pe, alpha=0.4, color='cyan', label="Estimación")
plt.xlabel('Valores')
plt.ylabel('Densidad')
plt.title(r"Comparación con la función Exponencial")
plt.legend()
plt.show()

obs,cri,df = chi.test(fo,pe,0)
kol.test(fo,pe)
gchi.mostrar(obs,df)