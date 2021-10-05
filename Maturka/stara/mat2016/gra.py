from copy import deepcopy


plik = open("gra.txt", "r")
w = plik.readlines()
for i in range(len(w)):
    w[i] = list(w[i].replace("X", "1").replace(".", "0").strip("\n"))
    for j in range(len(w[i])):
        w[i][j] = int(w[i][j])
plik.close()


def suma(A, y, x):
    sum = 0
    rows = len(A)
    cols = len(A[y])
    for i in range(-1, 2):
        for j in range(-1, 2):
            col = (x + j) % cols
            row = (y + i) % rows
            sum += A[row][col]
    sum -= A[y][x]
    return sum

def jeden(current, n,ktory=1):
    # next = deepcopy(current)
    next = [[current[x][y] for y in range(len(current[0]))] for x in range(len(current))]
    y = len(current)
    if n == 1:
        return current
    for i in range(y):
        x = len(current[i])
        for j in range(x):
            element = current[i][j]
            # krawedzie
            neighbors = suma(current, i, j)
            # Zliczanie
            if element == 0 and neighbors == 3:
                next[i][j] = 1
            elif element == 1 and (neighbors < 2 or neighbors > 3):
                next[i][j] = 0
            else:
                next[i][j] = element
    ktory += 1
    if next == current:
        return current,ktory

    if ktory == n:
        return next
    return jeden(next, n,ktory)


# 5.1
jedenx = jeden(w, 1)

print(suma(jedenx, 1, 18))
for i in range(len(jedenx)):
    print(jedenx[i])
# 5.2

ile = 0
dwa = jeden(w, 2)
for i in range(len(dwa)):
    for j in range(len(dwa[i])):
        if dwa[i][j] == 1:
            ile += 1
print(ile)

"""for i in range(len(jedenx)):
    print(jedenx[i])"""

#5.3
ile = 0
trzy,ktory = jeden(w,100)
for i in range(len(trzy)):
    for j in range(len(trzy[i])):
        if trzy[i][j] == 1:
            ile += 1
print("jedynek jest",ile,"|| z kolei: ",ktory)

