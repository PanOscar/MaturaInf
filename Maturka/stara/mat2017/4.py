plik = open('binarnie.txt')
liczby = [x.replace('\n','')for x in plik.readlines()]
plik.close()

def cykl(x):
    slowa = 0
    mroz = 0
    roz = 0
    jakie = ""
    for i in range(len(x)):
        if len(x[i]) %2 == 0:
            granica = 0
            A = []
            B = []
            for j in range(len(x[i])):
                if granica < len(x[i])/2:
                    A.append(x[i][j])
                else:
                    B.append(x[i][j])
                granica += 1
            if A == B:
                roz = len(x[i])
                slowa +=1
            if roz > mroz:
                jakie = x[i]
                mroz = roz
    return mroz,slowa,jakie

print(cykl(liczby))

def drugie(x):
    zle = 0
    dobre = 0
    mini = 9999
    for i in range(len(x)):
        zlel = 0
        for j in range(0,len(x[i]),4):
            if int(x[i][j:j+4],base=2) >9:
                zle +=1
                zlel+=1
                break
        if zlel>0:
            if len(x[i])<mini:
                mini = len(x[i])
            continue
        dobre+=1
    return dobre,zle,mini


print(drugie(liczby))

def trzecie(x):
    maxi = -1
    for i in range(len(x)):
        if 65535 > int(x[i],base=2) > maxi:
            maxi = int(x[i],base=2)
            A = x[i]
    return maxi,A,

print(trzecie(liczby))