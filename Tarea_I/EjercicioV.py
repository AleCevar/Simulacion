import random

print("Punto a) 26/52 = 0.5")

tot=int(1e5)
sum=0

for _ in range(tot):
    if random.randint(0, 51)<26:
        sum+=1

print(f"Punto b) {sum/tot}")