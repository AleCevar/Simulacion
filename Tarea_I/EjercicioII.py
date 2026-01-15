import random


print(f"Punto a) 0.375")

def flipCoin():
    return random.randint(0, 1)

def experimentar(n, m):
    sum = 0
    for _ in range(m):
        r = flipCoin() + flipCoin() + flipCoin()
        if r==n:
            sum+=1
    return sum / m

print(f"Punto b) {experimentar(0,int(1e5))}")
print(f"Punto c) {experimentar(1,int(1e5))}")
print(f"Punto d) {experimentar(2,int(1e5))}")
print(f"Punto e) {experimentar(3,int(1e5))}")
print(f"Punto f) Binomial")