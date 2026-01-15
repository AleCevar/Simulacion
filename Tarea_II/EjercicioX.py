
print("""
\n
a) La probabilidad de la paridad es 0.5 \n
Por lo que se puede mapear como x%2=0 es cara y x%2=1 es escudo \n
donde x es el número generado.\n
\n
\n
b) Los eventos de a, sería si sale 0, los eventos de b si sale un número del 1 al 4,\n
y los eventos de c, sería si sale del 5 al 9.\n
\n
c) Asumiendo que el dado solo se tira una vez, no es posible realizar estos eventos asignando un número a cada cara \n
y que el resultado sea uniforme. Pero una posible forma, sería asignar las caras 1,2,3,4,5,6 a los números \n
0,1,2,3,4,5, respectivamente, y si se obtiene un número mayor al 5, se vuelve a generar un número. La media de \n
intentos tiende a 1. \n
\n
d)\n
    A) La probabilidad de la paridad es 0.5.\n
    Por lo que se puede mapear como x%2=0 es cara y x%2=1 es escudo\n
    donde x es el número generado.\n
\n
    B) Los eventos de a, sería si sale del 0 al 9,\n
    los eventos de b si sale un número del 10 al 49,\n
    y los eventos de c, sería si sale del 50 al 99.\n
\n
    C) Igualmente asumiendo que el dado solo se tira una vez, no es posible realizar estos eventos asignando \n
    un número a cada cara y que el resultado sea \n
    uniforme. Pero una posible forma, sería asignar los números del 0 al 15 a la cara 1, del 16 al 31 a la cara 2, \n
    del 32 al 47 a la cara 3, del 48 al 63 a la cara 4, del 64 al 79 a la cara 5 y del 80 al 95 a la cara 6. Si se \n
    obtiene un numero superior a 95, se vuelve a generar otro número. \n
\n
    D) De esta forma se podrían simular todos los dados que son poliedros regulares. \n
    Con caras n igual a 4, 6, 8, 12, 20. Con una asignación de [0, x), [x, 2*x), 
    [2*x, 3*x), [3*x, 4*x), [4*x, 5*x), [5*x, 6*x) asignado para 1, 2, 3, 4, 5, 6 respectivamente
    con x=100/n. Los rangos de aceptación serían [0, 100), [0, 96), [0, 96), [0, 96), [0, 100)
    para los diferentes n respectivamentes.
""")