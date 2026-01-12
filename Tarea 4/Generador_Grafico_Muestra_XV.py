import matplotlib.pyplot as plt
import math
import Pruebas.Chi_Cuadrado as chi
import Pruebas.Kolmogorov_Smirnov as kol
import Distribuciones.Normal_Ajustada as dis
import Distribuciones.Uniforme as unif

name = "Muestras/m15.txt"
freq= dict()
n=0

with open(name, "r", encoding="utf-8") as f:
    for l in f:
        n+=1
        num = math.trunc(float(l) * 1000) / 1000
        # num=int(float(l))
        freq[num] = freq.get(num, 0) + 1

x=[]
y=[]
for a, b in sorted(freq.items()):
    x.append(a)
    y.append(b)

prob = [j / n for j in y]

[lamb, fun] = dis.calc(x, prob, 0.001)

plt.plot(x,prob)
plt.xlabel('Valores')
plt.ylabel('Frecuencia relativa')
plt.title('Histograma de Frecuencias Relativa')
plt.show()
# #
# plt.bar(x,y, color="green")
# plt.xlabel('Valores')
# plt.ylabel('Frecuencia observada')
# plt.title('Histograma de Frecuencias Absolutas')
# plt.show()
# #
# plt.bar(x, fun,color='red')
# plt.xlabel('Valores')
# plt.ylabel('Frecuencia absoluta')
# plt.title(f"Histograma de la Distribución X~poiss({lamb})")
# plt.show()
# #
# plt.bar(x,prob, alpha=0.1, color='yellow', label="Densidad Relativa")
# plt.bar(x,fun, alpha=0.2, color='cyan', label=rf"Densidad Poisson $\lambda = $ {lamb}")
plt.bar(x,prob, alpha=0.1, color='yellow', label="Densidad Relativa")
plt.xlabel('Valores')
plt.ylabel('Densidad')
plt.title(f"Comparación Datos Esperados y Observados para la Distribución X~pois")
plt.legend()
plt.show()

chi.test(y,fun,2)
kol.test(y,fun)