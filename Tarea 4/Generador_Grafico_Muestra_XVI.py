import matplotlib.pyplot as plt
import math
import Pruebas.Chi_Cuadrado as chi
import Pruebas.Kolmogorov_Smirnov as kol
import Calculos.Regresion_Lineal as reg

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

[a,b, fun] = reg.calc(x, prob)
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


# plt.plot(x,prob)
# plt.xlabel('Valores')
# plt.ylabel('Frecuencia relativa')
# plt.title('Histograma de Frecuencias Relativa')
# plt.show()
#
# plt.bar(xmod,fo, color="green")
# plt.xlabel('Valores')
# plt.ylabel('Frecuencia observada')
# plt.title('Histograma de Frecuencias Absolutas')
# plt.show()
# # #
# plt.bar(xmod,[z*n for z in pe],color='red')
# plt.xlabel('Valores')
# plt.ylabel('Frecuencia absoluta')
# plt.title(f"Histograma de la Distribución X~poiss({1})")
# plt.show()
# # # #
# plt.bar(xmod, [z/n for z in fo], alpha=0.4, color='yellow', label="Densidad Relativa")
# plt.bar(xmod,pe, alpha=0.4, color='cyan', label=rf"Densidad Poisson $\lambda = $ {1}")
# plt.xlabel('Valores')
# plt.ylabel('Densidad')
# plt.title(f"Comparación Datos Esperados y Observados para la Distribución X~pois")
# plt.legend()
# plt.show()

chi.test(fo,pe,0)
kol.test(fo,pe)