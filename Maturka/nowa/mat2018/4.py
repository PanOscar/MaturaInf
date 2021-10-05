plik = open('przyklad.txt')
w = [x.replace('\n', '') for x in plik.readlines()]
plik.close()
#1
def niech(x):
    word = ""
    for i in range(39,len(x),40):
        word += x[i][9]

    return word

print(niech(w))

#2
def rozne(x):
    maxz = 0
    for i in range(len(x)):
        A = []
        roz = 0
        for j in range(len(x[i])):
            if x[i][j] not in A:
                A.append(x[i][j])
                roz +=1
            if roz > maxz:
                maxz = roz
                slowo = i
    return x[slowo],maxz

print(rozne(w))

#3
def oddalenie(x):
    A = []
    roz = 0
    for slowo in x:
        x = sorted(slowo)
        if (ord(x[-1])-ord(x[0])) <= 10:
            A.append(slowo)
            roz +=1
    return roz,A

print(oddalenie(w))