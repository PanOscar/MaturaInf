plik = open('przyklad.txt')
liczby = [x.replace('\n','')for x in plik.readlines()]
plik.close()

def zad1(x):
    gwiazdki = 0
    dzialka = 0
    for i in range(len(x)):
        for j in range(len(x[i])):
            if x[i][j] == "*":
                gwiazdki +=1
        if x[i] == "":
            if gwiazdki / (30*30) >= 0.7:
                dzialka +=1
            gwiazdki = 0
    return dzialka

print(zad1(liczby))

def zad2(x):
    dzialka = 0
    A = []
    print("haha",x.count("")+1)
    for n in range((len(x)-x.count("")+1)//30):
        for i in range(n+1,(len(x)-x.count("")+1)//30):
            wiersz = 0
            for j in range(0,30):
                if x[n*31+j][] == x[n-i][::-1]:
                    wiersz +=1
            if wiersz == 30:
                A.append(n)
                A.append(dzialka)
    return A

print(zad2(liczby))