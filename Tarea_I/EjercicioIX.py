import random

tot = int(5e6)

def calc(TS1, TS2, S1F, S2F) :
    s1Y=TS1*S1F
    s1N=1-s1Y
    s2Y=TS2*S2F
    s2N=1-s2Y

    c1 = s1Y * s2N
    c2 = s2Y * s1N
    c3 = s1Y * s2Y

    sum = 0
    for _ in range(tot):
        r1 = random.random()
        r2 = random.random()
        r3 = random.random()
        r4 = random.random()
        flag = 1
        if r1 < TS1  and r2 < S1F  :
            flag = 0
        if r3 < TS2 and r4 < S2F  :
            flag = 0
        if not flag:
            sum+=1
    # print(sum / tot)

    return c1 + c2 + c3

print(f"Punto a) {calc(0.9,0.9,0.8,0.7)}")
print(f"Punto b) {calc(0.9,0.9,0.8,0.8)}")

def calc(TS1, TS2, S1F, S2F, S1S2) :
    sum = 0
    for _ in range(tot):
        r1 = random.random()
        r2 = random.random()
        r3 = random.random()
        r4 = random.random()
        r5= random.random()
        flag = 1
        if r1 < TS1 and r2 < S1F:
            flag = 0
        if r3 < TS2 and r4 < S2F:
            flag = 0
        if r5 < S1S2 and ((r1<TS1 and r4<S2F) or (r2<TS2 and r3<S1F)) :
            flag = 0
        if not flag:
            sum += 1
    return sum / tot

print(f"Punto c) {calc(0.9,0.9,0.8,0.7, 0.8)}")