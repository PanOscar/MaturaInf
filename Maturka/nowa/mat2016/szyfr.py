# zad 1
print("Zad1")
plik = open('dane_6_1.txt')
w = [x.replace('\n', '') for x in plik.readlines()]
plik.close()
print(w)

def zad1(w):
    k = 107%26
    print(k)
    for i in range(len(w)):
        liczba = 0
        for j in range(len(w[i])):
            if ord(w[i[j]])+k >90 :
                liczba = 65 +k
                chr(liczba)

zad1(w)
print(ord("Z")-ord("A"))
print(chr(93))

