plik = open('gra.txt')
liczby = [list(x.replace('\n', '').replace('X', '1').replace('.', '0'))for x in plik.readlines()]
plik.close()
liczbyint = [list(map(int, i))for i in liczby]

for i in range(len(liczby)):
    print(liczbyint[i])
print()
def suma(tablica, i, j):
    sum = 0
    dlrows = len(tablica)
    dlcols = len(tablica[0])
    for y in range(-1, 2):
        for x in range(-1, 2):
            rows = (i + y) % dlrows
            cols = (j + x) % dlcols
            sum += tablica[rows][cols]
    sum -= tablica[i][j]
    return sum

def gra(x, pokolenie, ktore = 1):
    if pokolenie == 1:
        return x
    tab = [[x[i][j] for j in range(len(x[0]))]for i in range(len(x))]
    for i in range(len(x)):
        for j in range(len(x[i])):
            if x[i][j] == 1 and (suma(x,i,j) < 2 or suma(x,i,j) > 3):
                tab[i][j] = 0
            elif x[i][j] == 0 and suma(x,i,j) == 3:
                tab[i][j] = 1
            else:
                tab[i][j] = x[i][j]
    ktore+=1
    if tab == x:
        return tab,ktore
    if ktore == pokolenie:
        return tab
    return gra(tab,pokolenie,ktore)

#5.1
gra2d1 = gra(liczbyint,100)

print(suma(gra2d1, 1, 18))

#5.2
gra2d2 = gra(liczbyint,2)
roz = 0
for y in range(len(gra2d2)):
    for x in range(len(gra2d2[y])):
        roz += gra2d2[y][x]
print(roz)

#5.3
roz = 0
gra2d3,ile = gra(liczbyint,100)
for y in range(len(gra2d3)):
    for x in range(len(gra2d3[y])):
        roz += gra2d3[y][x]
print(ile,roz)