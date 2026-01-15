def mixto(a,b,m,x):
    vis = [0 for _ in range(m)]
    while True:
        print(x, end=" ")
        vis[x] = 1
        x = (a * x + b) % m
        if vis[x] == 1:
            break
    print()
    if vis.count(0) == 0:
        print("Recorrido Completo")
        return True
    return False

def multi(a,m,x):
    vis = [0 for _ in range(m)]
    while True:
        # print(x, end=" ")
        vis[x] = 1
        x = (a * x) % m
        if vis[x] == 1:
            break
    # print()
    if vis.count(0) == 0:
        print("Recorrido Completo")
        return True
    return False

def addi(x,y,m):
    vis = [[0 for _ in range(m)] for _ in range(m)]
    aper = [0 for _ in range(m)]
    a1=x
    a2=y
    vis[a1][a2] = 1
    while True:
        k = (a1 + a2) % m
        aper[k] = 1
        print(k, end=" ")
        if aper.count(0) == 0 or vis[a2][k]:
            break
        a1 = a2
        a2 = k
    print()
    if aper.count(0) == 0:
        print("Recorrido Completo")
        return True
    return False


mixto(21, 7, 10, 1)
print(f"Mixto : a = 21, b = 7, m = 10, x0 = 1")
print(f"Multiplicativo : NO existe una a y x0 tal que recorra todos los números del 0 al 9. Ya que no todos los números menores a 9 son coprimos con el")
addi(1,1,10)
print(f"Aditivo : x0 = 1, x1 = 1, m = 10")