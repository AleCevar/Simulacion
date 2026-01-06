from random import random, randint

with open("Muestras/muestra_python_float.txt", "w", encoding="utf-8") as f:
    for _ in range(int(1e6)):
        f.write(str(random()) + "\n")

with open("Muestras/muestra_python_int.txt", "w", encoding="utf-8") as f:
    for _ in range(int(1e6)):
        f.write(str(randint(1, 6)) + "\n")