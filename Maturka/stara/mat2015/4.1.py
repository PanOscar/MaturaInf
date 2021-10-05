plik = open('slowa.txt')
liczby = [x.replace('\n', '') for x in plik.readlines()]
plik.close()


def zera(x):
    n = len(x)
    wyrazy = 0
    for i in range(n):
        roz0 = 0
        roz1 = 0
        for j in range(len(x[i])):
            if x[i][j] == "0":
                roz0 +=1
            if x[i][j] == "1":
                roz1 += 1
        if roz0 > roz1:
            wyrazy +=1
    return wyrazy
print(zera(liczby))

def slowa(x):
    n = len(x)
    wyrazy = 0
    for i in range(n):
        kolejnosc = 0
        for j in range(len(x[i])-1):
            if x[i][0] == "1":
                break
            else:
                if x[i][j+1] == "1" and x[i][j]=="0":
                    kolejnosc +=1
                elif x[i][j+1] == "0" and x[i][j]=="1":
                    kolejnosc +=1
        if kolejnosc == 1:
            wyrazy += 1
    return wyrazy

print(slowa(["0001"]))

def bloki(x):
    n = len(x)
    maks= 0
    wyrazy = 0
    odp = ''
    for i in range(n):
        roz = 1
        mroz = 0
        for j in range(len(x[i])-1):
            if x[i][j] == "0" and x[i][j+1] == x[i][j]:
                roz +=1
                if roz > maks:
                    wyrazy= 0
                    odp = ''
                    maks = roz
                if roz == maks:
                    mroz = roz
            else:
                roz = 1
        if mroz == maks:
            odp += x[i] + " "
            wyrazy += 1

    return maks,wyrazy,odp

print(bloki(liczby))
