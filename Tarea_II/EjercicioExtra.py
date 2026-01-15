print("""
    \n
    a) \n
        m = 1e9+7 \n
        Si se toma a = m + 1, cuando se aplique la operación : (a * x_n + c) % m, si se distribuye el modulo,\n
        se obtiene:\n
        \n
            (a * x_n) % m + c % m
        \n
        Se puede observar que el a % m va a ser 1, por lo cual el resultado será x_n + c % m. Por lo tanto \n
        se puede seleccionar cualquier c (que sea coprimo de m), y fungirá como el desplazamiento. \n
        De la misma forma, seleccionar un x_0 variará el orden presentado, pero el ejercicio en cuestión es indiferente.\n
        \n
        Por motivos de dar una respuesta se selecciona:
        a = 1e9 + 8, c = 11 y x_0 = 1
        
    b) \n
        m = 1e9 + 9 \n
        Con el mismo procedimiento anterior y como m es primo se puede elegir
        a= 1e9+10, c=13 y x_0=1
""")