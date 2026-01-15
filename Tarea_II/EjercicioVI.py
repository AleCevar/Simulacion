def calc(a,b,m,x):
    vis = [0 for _ in range(m)]
    while vis[x] == 0:
        print(x, end=" ")
        vis[x] = 1
        x = (a * x + b) % m
    print()
    if vis.count(0) == 0:
        return "Cumple con todo el periodo"
    return "No cumple con todo el periodo"


print(calc(16,11,15, 4))
print(f"a = 16 , c = 11, m = 15, x0 = 4")
