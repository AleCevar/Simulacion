def calc(a,b,m,x):
    vis = [0 for _ in range(m)]
    while vis[x] == 0:
        print(x, end=" ")
        vis[x] = 1
        x = (a * x + b) % m
    print()
    if vis.count(0) == 0:
        print("Recorrido Completo")
        return True
    return False


calc(20, 13, 19, 1)
print(f"a = 20, b = 13, m = 19, x_0 = 1")