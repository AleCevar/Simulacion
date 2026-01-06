import random
deck = [(i%13)+1 for i in range(52)]

tot=int(5e5)
sum=0


for _ in range(tot):
    for i in range(5):
        pos = random.randint(i,51)
        deck[i],deck[pos] = deck[pos],deck[i]
    c = 0
    cnt = 0
    for i in range(5):
        c+=deck[i]
        if deck[i]==1 :
            cnt+=1
    if c < 17 and cnt > 0:
        c += 13
    if 17 <= c <= 21:
        sum+=1

print(f"{sum/tot}")