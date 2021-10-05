# zad 1
print("Zad1")
plik = open('dane_6_1.txt')
w = [x.replace('\n', '') for x in plik.readlines()]
plik.close()
print(w)


def szyfrowanie(w, n):
    lower = ord("A")
    upper = ord("Z") + 1
    count = upper - lower
    for i in range(len(w)):
        g = ""
        for j in range(len(w[i])):
            g += chr(((ord(w[i][j]) + n - lower % count) % count) + lower)            # lecimy do przodu
          # g += chr(((ord(w[i][j]) + n - (lower % count) + count) % count) + lower)  # działa tak samo
        w[i] = g
    return w


print(szyfrowanie(w, 107))
print("Zad2")

# zad 2
plik = open('dane_6_2.txt')
w = plik.readlines()
plik.close()

for i in range(len(w)):
    w[i] = w[i].strip("\n").split(" ")
    for j in range(len(w[i])):
        if w[i][1]:
            w[i][1] = int(w[i][1])
        else:
            w[i][1] = 0

def odszyfrowanie(x):
    A = []
    lower = ord("A")
    upper = ord("Z") + 1
    count = upper - lower
    for i in range(len(w)):
        n = w[i][1]
        g = ""
        for j in range(len(w[i][0])):
            g += chr(((ord(w[i][0][j]) - n - lower % count) % count) + lower)# lecimy do tyłu
            #g += chr(((ord(w[i][0][j]) - n - (lower % count) + count) % count) + lower)  # działa tak samo
        A.append(g)
    return A


print(odszyfrowanie(w))
print("Zad3")
# zad 3
plik = open('dane_6_3.txt')
w = [y.split(" ") for y in (x.replace('\n', '') for x in plik.readlines())]
plik.close()

print(w)


def odl(w):
    g = []
    for i in range(len(w)):
        for j in range(len(w[i][0])):
            if ord(w[i][0][j]) > ord(w[i][1][j]):
                przesuniecie = ord(w[i][1][j]) + 26 - ord(w[i][0][j])
            else:
                przesuniecie = ord(w[i][1][j]) - ord(w[i][0][j])
            if j > 0 and maxp != przesuniecie:
                g.append(w[i][0])
                break
            maxp = przesuniecie
    return g

print(odl(w))
