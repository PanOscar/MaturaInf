from copy import deepcopy

plik = open("gra.txt","r")
w = plik.readlines()
plik.close()

for i in range(len(w)):
    w[i] = list(w[i].strip("\n").replace("X","1").replace(".","0"))
    for j in range(len(w[i])):
        w[i][j] = int(w[i][j])

def suma(w,y,x):
    suma = 0
    rows = len(w)
    cols = len(w[y])
    for i in range(-1,2):
        for j in range(-1,2):
            suma += w[(y+i)% rows][(x+j)%cols]
    suma -= w[y][x]
    return suma

def core(w,n,k=1):
    nowa = deepcopy(w)
    if n == 1:
        return w
    for i in range(len(w)):
        for j in range(len(w[i])):
            sasiad = suma(w,i,j)
            if w[i][j]==1 and (sasiad<2 or sasiad>3):
                nowa[i][j] = 0
            elif w[i][j] == 0 and sasiad == 3:
                nowa[i][j] =1
            else:
                nowa[i][j] = w[i][j]
    k +=1
    if n == k:
        return nowa
    return core(nowa,n,k)

x = core(w,2)

for i in range(len(x)):
    print(x[i])