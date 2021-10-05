def cyfra(x):
    wynik = 0
    for pesel in x:
        if pesel[-2] % 2 == 0:
            wynik += 1
    return print('kobiet:', wynik, "mężczyzn:", len(x)-wynik)

def drugie(x):
    wynik = 0
    for pesel in x:
        if pesel[2:4] == '31' or pesel[2:4] == '11':
            wynik += 1
    return print(wynik)

