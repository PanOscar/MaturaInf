licznik = 0
plik = open('liczby.txt', 'r')

liczby = plik.readlines()
for i in range(499):
    liczby[i] = int(liczby[i].rstrip("\n"))

plik.close()

for i in liczby:
    for dzielnik in potegi_3:
        if i == dzielnik:
            licznik += 1

wynik_1 = licznik

plik = open("wyniki4.txt", "a")
plik.writelines("4.1: {}\n".format(wynik_1))
plik.close()