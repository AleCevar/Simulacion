
def calc(seed, pos, bit):
    k = seed
    ar=[]
    tot=(1<<(pos+1))-1
    vis = [0 for _ in range(tot+1)]
    while True:
        b = bool(k & (1 << 0)) ^ bool(k & (1<<bit))
        k>>=1
        if b:
            k|=(b<<pos)
        ar.append(k)
        if vis[k]:
            break
        vis[k] = 1
    if vis.count(0)==1:
        print("Recorrido Completo")
    return ar

print(calc(31, 4, 2))

print(f"Semilla = 31 y Operacion : b_0 ^ b_2, right-shift (b_i siendo el i-esimo bit)")