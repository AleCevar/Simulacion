
def calc(seed, pos):
    k = seed
    ar=[]
    tot=(1<<(pos+1))-1
    vis = [0 for _ in range(tot+1)]
    while True:
        b = bool(k & 1) ^ bool(k & 4)
        k>>=1
        if b:
            k|=(b<<pos)
        ar.append(k)
        if vis[k]:
            break
        vis[k] = 1
    if vis.count(0)==1:
        print("Recorrido Completo")
    else :
        print("No hay recorrido completo")
    return ar

print("Punto a)")
print(calc(6, 2))
print("Punto b)")
print(calc(15, 3))
