
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

print(f"Punto a) {calc(5,24,32,7)}")
print(f"Punto b) {calc(9,13,32,8)}")
print(f"Punto c) {calc(50,17,64,13)}")
print(f"Punto d) {calc(8,16,100,15)}")
print(f"Punto e) {calc(5,21,100,3)}")