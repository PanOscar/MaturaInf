import math
plik = open('liczby.txt', 'r')
liczby = plik.readlines()
plik.close()

liczby = [int(x) for x in liczby]
plik = open('liczby.txt')
liczby = [x.replace('\n', '') for x in plik.readlines()]
plik.close()
liczbyint = list(map(int,liczby))


#1.
def pow(x):
    a = 1
    tab = []
    for i in range(12):
        a = x**i
        if a < 100000:
            tab.append(a)
        i += 1
    return tab

roz = 0
for i in range(len(liczbyint)):
    for j in range(len(pow(3))):
        if liczbyint[i] == pow(3)[j]:
            roz += 1
print(roz)

#2.
def silnia(x):
    silnia = 1
    if x == 0:
        return 1
    else:
        for i in range(1, x+1):
            silnia *= i
        return silnia

def liczba(x,y):
    sil = 0
    tab = []
    for i in range(len(x)):
        sil = 0
        for j in range(len(x[i])):
            sil += silnia(int(x[i][j]))
        if sil == y[i]:
            tab.append(y[i])
    return tab

print(liczba(liczby, liczbyint))

#3.
def ciag(x):
    n = len(x)
    roz = 1
    temp = 0
    maks_d = 0
    maks_temp = 0
    maks_r = 1
    dzielnik = 0
    for i in range(n-1):
        if i == 0 or dzielnik <= 1:
            if roz > maks_r:
                maks_temp = temp
                maks_r = roz
            dzielnik = math.gcd(x[i], x[i+1])
            temp = x[i]
            roz = 1
        else:
            dzielnik = math.gcd(dzielnik, x[i + 1])
            if  dzielnik > maks_d:
                maks_d = dzielnik
            roz += 1
    return maks_temp,maks_r,maks_d

print(ciag(liczby))