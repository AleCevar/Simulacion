

def cal(seed):
    k=seed
    ar=[]
    for _ in range(50):
        k=k*k
        st=str(k)
        r = (len(st) - 4 + 1) // 2
        k //= 10**r
        k %= 10**4
        ar.append(k)
    return ar

print(f"Punto a) {cal(3567345)}")
print(f"Punto b) {cal(1234500012)}")
print(f"Punto c) {cal(4567234902)}")