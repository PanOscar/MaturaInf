plik = open('liczby.txt', 'r')
liczby = plik.readlines()
for i in range(len(liczby)):
    liczby[i] = int(liczby[i].replace("\n", ''))

plik.close()

import math

najdluzszy_zbior = []
mozliwe_zbiory = []

poprzednie = 0


for i in liczby:
    if len(mozliwe_zbiory) == 0:
        mozliwe_zbiory.append(i)
    else:
        licznik = mozliwe_zbiory[0]
        for x in mozliwe_zbiory:
            licznik = math.gcd(licznik, x)
        if math.gcd(licznik, i) > 1:
            mozliwe_zbiory.append(i)
        else:
            poprzednie = mozliwe_zbiory[-1]
            if len(mozliwe_zbiory) > len(najdluzszy_zbior):
                najdluzszy_zbior = mozliwe_zbiory.copy()
                mozliwe_zbiory = [i]
            else:
                mozliwe_zbiory = [i]
            if math.gcd(i, poprzednie) > 1:
                mozliwe_zbiory = [poprzednie, i]


print(najdluzszy_zbior)
NWD = najdluzszy_zbior[0]
for x in najdluzszy_zbior:
    NWD = math.gcd(NWD, x)


wynik_3 = "Pierwsza liczba: {}, Dlugosc: {}, NWD: {}".format(najdluzszy_zbior[0], len(najdluzszy_zbior), NWD)
print(wynik_3)

plik = open("wyniki4.txt", "w")
plik.write("4.3: {}\n".format(wynik_3))
plik.close()