file = open("przyklad.txt", "r")
w = file.readlines()
file.close()

for i in range(len(w)):
    w[i] = w[i].split(" ")
    for j in range(len(w[i])):
        w[i][j] = int(w[i][j].strip("\n"))

# zadanie 1
def maksimum(w):
    max = -1
    min = 256
    for i in range(len(w)):
        for j in range(len(w[i])):
            if w[i][j] > max:
                max = w[i][j]
            if w[i][j] < min:
                min = w[i][j]
    return min, max


print(maksimum(w))

# zadanie 2
def palindrom(w):
    wynik = 0
    for i in range(len(w)):
        if w[i][::-1] != w[i]:
            wynik += 1
    return wynik

print(palindrom(w))

# zadanie 3
def suma(A, y, x):
    wynik = 0
    for i in range(-1, 2, 2):
        try:
            if abs(A[y][x] - A[y][x + i]) > 128:
                wynik += 1
        except:
            pass
        try:
            if abs(A[y][x] - A[y + i][x]) > 128:
                wynik += 1
        except:
            pass
    return wynik


def sasiad(w):
    wynik = 0
    for i in range(len(w)):
        for j in range(len(w[i])):
            if suma(w, i, j) >= 1:
                wynik += 1
    return wynik


print(sasiad(w))
