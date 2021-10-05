plik = open('dzialka.txt')
liczby = plik.readlines()

plik.close()

for i in range(len(liczby)):
    liczby[i]=liczby[i].strip('\n')


def kwadrat(x):
    wynik = 0
    for n in range(len(x)+1):
        for i in range(n+1):
            for j in range(n+1):
                if x[i][j]=="x":
                    return wynik

        wynik+=1
    return wynik

print(kwadrat(liczby))