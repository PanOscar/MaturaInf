plik = open('liczby.txt')
liczby = [x.replace('\n', '') for x in plik.readlines()]
plik.close()


# 4.1 Podaj, ile liczb ma w swoim zapisia binarnym więcej zer niż jedynek.

def zera(y):
    roz = 0
    for liczba in y:
        zero = 0
        jedynka = 0
        for znak in liczba:
            if znak == '0':
                zero += 1
            else:
                jedynka += 1
        if zero > jedynka:
            roz += 1
    return print(roz)


zera(liczby)

# 4.2 Podaj, ile liczb w pliku liczby.txt jest podzielnych przez 2 oraz ile liczb jest podzielnych przez 8

liczbyint = [int(i, base=2) for i in liczby]
liczbyint = []
for i in range(len(liczby)):
    liczbyint.append(int(liczby[i], base=2))


def podzielnosc(a):
    przezosiem = 0
    przezdwa = 0
    for j in range(len(a)):
        if a[j] % 2 == 0:
            przezdwa += 1
    for k in range(len(a)):
        if a[k] % 8 == 0:
            przezosiem += 1
    return print(przezdwa, przezosiem)


podzielnosc(liczbyint)


# 4.3 Znajdź najmniejszą i największą liczbę w pliku liczby.txt. Jako odpowiedź podaj numery wierszy w których one się znajdują.

def minmax(s):
    min = s[0]
    max = s[0]
    minid = 0
    maxid = 0
    for i in range(len(s)):
        if max < s[i]:
            max = s[i]
            maxid = i
    for j in range(len(s)):
        if min > s[j]:
            min = s[j]
            minid = j
    return print(minid + 1, maxid + 1)


minmax(liczbyint)
