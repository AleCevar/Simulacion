import matplotlib.pyplot as plt
import math
import Pruebas.Chi_Cuadrado as chi
import Pruebas.Kolmogorov_Smirnov as kol
import Calculos.Regresion_Lineal as reg
import Distribuciones.Uniforme as unif
import Graficador.Graficador_Distribuciones as grf
import Graficador.Grafico_Chi_Cuadrado as gchi

name = "Muestras/m15.txt"
freq1= dict()
freq2= dict()
cantDig=100
with open(name, "r", encoding="utf-8") as f:
    for l in f:
        num = float(l)
        if num>1:
            freq2[num] = freq2.get(num, 0) + 1
        else:
            num2 = math.trunc(num * cantDig) / cantDig
            freq1[num2] = freq1.get(num2, 0) + 1

def part2(freq):
    x=[]
    y=[]
    for a, b in sorted(freq.items()):
        x.append(a)
        y.append(b)
    n = sum(y)
    prob = [j / n for j in y]
    [_, _, fun] = reg.calc(x, prob)
    clases=dict()
    claori=dict()
    for i in range(len(x)):
        num=math.trunc(float(x[i]) * cantDig) / cantDig
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
    print("Prueba Chi2 para la Segunda Parte:")
    obs,cri, df = chi.test(fo, pe, 0)
    gchi.mostrar(obs,df - 1)
    print("Prueba Kolmogorov para la Primera Parte:")
    kol.test(fo, pe)
    fe=[n*z for z in pe]
    return xmod, fo, fe

def part1(freq):
    x=[]
    y=[]
    for a, b in sorted(freq.items()):
        x.append(a)
        y.append(b)
    n = sum(y)
    prob = [j / n for j in y]
    un = unif.calc(x, 1/cantDig)
    print("Prueba Chi2 para la Primera Parte:")
    obs,cri,df = chi.test(y, un, 0)
    gchi.mostrar(obs, df - 1)
    print("Prueba Kolmogorov para la Primera Parte:")
    kol.test(y, un)
    fe= [n*z for z in un]
    return x, y, fe

x1, fo1, fe1 = part1(freq1)
x2, fo2, fe2 = part2(freq2)

x=x1+x2
y1=fo1+fo2
y2=fe1+fe2

grf.absoluta(x,y1)

# plt.plot(x,prob)
# plt.xlabel('Valores')
# plt.ylabel('Frecuencia relativa')
# plt.title('Histograma de Frecuencias Relativa')
# plt.show()

grf.distribucion(x,y2,"Histograma de la función por partes")
# grf.comparacion(x,y1,y2,"Densidad por partes","Comparación con la función por partes")

plt.plot(x, y1, alpha=0.4, color='yellow', label="Muestra")
plt.plot(x, y2, alpha=0.4, color='cyan', label="Estimación")
plt.xlabel('Valores')
plt.ylabel('Densidad')
plt.title(r"Comparación con la función por partes Uniforme y Exponencial")
plt.legend()
plt.show()
