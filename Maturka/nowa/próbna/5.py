plik = open("dziennik.txt", "r")
w = plik.readlines()
plik.close()

for i in range(len(w)):
    w[i] = int(w[i].strip('\n'))

def dluzsze(x):
    wynik = 0
    roz = 1
    for i in range(len(x)-1):
        mroz = 1
        if x[i+1] > x[i]:
            roz +=1
            if i == len(x)-2:
                mroz = roz
        else:
            mroz = roz
            roz = 1
        if mroz > 3:
            wynik +=1
    return wynik

print(dluzsze(w))

def naj(x):
    max = x[0]
    min = x[0]
    jmin = 1
    jmax = 1
    for i in range(len(x)):
        if x[i] > max:
            max = x[i]
            jmax = i+1
        if x[i] < min:
            min = x[i]
            jmin = i +1
    return jmax, jmin

print(naj(w))

def seria(x):
    mroz = 1
    roz = 1
    A = []
    A.append(x[0])
    roznica = 0
    for i in range(len(x)-1):
        if x[i+1] > x[i]:
            roz +=1
            A.append(x[i+1])
        else:
            A = []
            A.append(x[i+1])
            roz = 1
        if roz > mroz:
            roznica = A[-1] - A[0]
            mroz = roz
    return mroz, roznica

print(seria(w))