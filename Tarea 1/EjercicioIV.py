import random

print(f"Punto a) 4/52 * 3/51 = 0,004524886878")

deck = [(i%13)+1 for i in range(52)]

pairs = []

for i in range(52):
    for j in range(i+1,52):
        pairs.append([deck[i],deck[j]])

tot=int(1e5)
sum=0
for _ in range(tot):
    ind = random.randint(0,len(pairs)-1)
    if pairs[ind][0]==pairs[ind][1] and pairs[ind][0]==1:
        sum += 1

print(f"Punto b) {sum/tot}")
