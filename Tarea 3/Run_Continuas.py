import Prueba_Promedio as pe
import Prueba_Varianza as pv
import Prueba_Digitos as pd
import Prueba_Numeros as pn
import Prueba_Corrida as pc
import Prueba_Poker as pp
import Prueba_Series as ps

names=["muestra_erlang_float.txt","muestra_java_float.txt","muestra_python_float.txt"]

for name in names:
    with open("Generadores/Muestras/" + name, "r", encoding="utf-8") as f:
        print(name, flush=True)
        muestra = []
        for l in f:
            muestra.append(l[:-1])
        pe.continua(muestra)
        # pv.continua(muestra)
        # pd.continua(muestra)
        # pn.continua(muestra)
        # pc.continua(muestra)
        # pp.continua(muestra)
        # ps.continua(muestra)
        print()