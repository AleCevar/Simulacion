import Prueba_Promedio as pe
import Prueba_Varianza as pv
import Prueba_Digitos as pd
import Prueba_Numeros as pn
import Prueba_Corrida as pc
import Prueba_Poker as pp
import Prueba_Series as ps

# with open("Generadores/Muestras/muestra_c_4.txt", "r", encoding="utf-8") as f:
#     print("Pruebas de C - Base 4", flush = True)
#     muestra = []
#     for l in f:
#         muestra.append(int(l))
#     pe.discreta(1,4,muestra)
#     pv.discreta(1,4,muestra)
#     pd.discreta(muestra, 4)
#     pn.discreta(muestra, 4)
#     pc.discreta(muestra)
#     pp.discreta(muestra,4)
#     ps.discreta(muestra,4)

# with open("Generadores/Muestras/muestra_c_8.txt", "r", encoding="utf-8") as f:
#     print("Pruebas de C - Base 8")
#     muestra = []
#     for l in f:
#         muestra.append(int(l))
#     pe.discreta(1, 8, muestra)
#     pv.discreta(1, 8, muestra)
#     pd.discreta(muestra, 8)
#     pn.discreta(muestra, 8)
#     pc.discreta(muestra)
#     pp.discreta(muestra, 8)
#     ps.discreta(muestra, 8)
#
# with open("Generadores/Muestras/muestra_python_int.txt", "r", encoding="utf-8") as f:
#     print("Pruebas de Python")
#     muestra = []
#     for l in f:
#         muestra.append(int(l))
#     pe.discreta(1, 6, muestra)
#     pv.discreta(1, 6, muestra)
#     pd.discreta(muestra, 6)
#     pn.discreta(muestra, 6)
#     pc.discreta(muestra)
#     pp.discreta(muestra, 6)
#     ps.discreta(muestra, 6)

# with open("Generadores/Muestras/muestra_racket_int.txt", "r", encoding="utf-8") as f:
#     print("Pruebas de Racket")
#     muestra = []
#     for l in f:
#         muestra.append(int(l))
#     pe.discreta(1, 20, muestra)
#     pv.discreta(1, 20, muestra)
#     pd.discreta(muestra, 20)
#     pn.discreta(muestra, 20)
#     pc.discreta(muestra)
#     pp.discreta(muestra, 20)
#     ps.discreta(muestra, 20)
#
with open("Generadores/Muestras/muestra_c++_int.txt", "r", encoding="utf-8") as f:
    print("Pruebas de C++")
    muestra = []
    for l in f:
        muestra.append(int(l))
    pe.discreta(1, 10, muestra)
    pv.discreta(1, 10, muestra)
    pd.discreta(muestra, 10)
    pn.discreta(muestra, 10)
    pc.discreta(muestra)
    pp.discreta(muestra, 10)
    ps.discreta(muestra, 10)