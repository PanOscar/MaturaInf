def skojarzone(a):
    x = []
    sumA = 0
    sumB = 0
    for i in range(1,a):
        if a%i==0:
            sumA += i
    b = sumA - 1
    for j in range(1,b):
        if b%j==0:
            sumB += j
    if a == sumB-1 and b == sumA-1:
        return sumA-1
    else:
        return "Nie"

for i in range(1,100):
    if isinstance(skojarzone(i), int):
        print("dla",i,"jest",skojarzone(i))