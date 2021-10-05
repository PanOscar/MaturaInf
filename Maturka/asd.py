
def znaki1(y):
    roz = 1
    tab = list(y)
    tab1 = sorted(tab)
    if  not tab1:
        roz = 0
    else:
        for i in range(len(tab1)):
            if i > 0:
                if tab1[i] != tab1[i-1]:
                    roz += 1
    return print(roz)

znaki1(["00","00","09"])

def znaki(x):
    a = []
    for i in range(len(x)):
        if x[i] not in a:
            a.append(x[i])
    return print(len(a))

znaki(["00","00","00"])
