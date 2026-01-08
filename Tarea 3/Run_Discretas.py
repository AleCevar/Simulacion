import Prueba_Promedio as pe
import Prueba_Varianza as pv
import Prueba_Digitos as pd
import Prueba_Numeros as pn
import Prueba_Corrida as pc
import Prueba_Poker as pp
import Prueba_Series as ps

names = [
        "muestra_c_4.txt",
         "muestra_c_8.txt",
         "muestra_python_int.txt",
         "muestra_racket_int.txt",
         "muestra_c++_int.txt"
         ]
base = [4,8,6,20,10]

for i in range(len(names)):
    with open("Generadores/Muestras/" + names[i], "r", encoding="utf-8") as f:
        print(names[i] , flush = True)
        muestra = []
        for l in f:
            muestra.append(int(l))

        # pe.discreta(1, base[i], muestra)
        # pv.discreta(1, base[i], muestra)
        # pd.discreta(muestra, base[i])
        # pn.discreta(muestra, base[i])
        pc.discreta(muestra, base[i])
        # pp.discreta(muestra, base[i])
        # ps.discreta(muestra, base[i])
        print()


# python int digitos no paso
# c - 4 no paso poker