import random
from math import comb

pp=comb(52, 5)
sum=comb(48, 5)+4*comb(48, 4)
print((pp-sum)/pp)

print(f"Punto a) 0.04168436605411395")

deck = [(i%13)+1 for i in range(52)]

tot=int(5e5)
sum=0


for _ in range(tot):
    for i in range(5):
        pos = random.randint(i,51)
        deck[i],deck[pos] = deck[pos],deck[i]
    c = 0
    for i in range(5):
        if deck[i] == 1:
            c+=1
    if c > 1:
        sum+=1

print(f"Punto b) {sum/tot}")