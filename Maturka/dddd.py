import math
x = "123"
x = int(x) # 123

def sortuj(k):
    tekst = str(k)
    n = len(tekst)
    tab_cyfr = list(tekst[::-1])
    for i in range(n):
        tab_cyfr[i] = int(tab_cyfr[i])
    return n
math.pow()
print(sortuj(54321))
