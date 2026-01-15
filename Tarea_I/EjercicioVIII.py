import random

tot = int(5e4)
def calc(k):
    sum=0
    for _ in range(tot):
        money = 100
        while 0 < money < 200:
            r = random.randint(1,100)
            if r <= 52 :
                money -= 10*k
            else:
                money += 10
        if money >= 200:
                sum+=1
    return sum

print(f"Punto a) {calc(1)/tot}")
print(f"Punto b) {calc(2)/tot}")