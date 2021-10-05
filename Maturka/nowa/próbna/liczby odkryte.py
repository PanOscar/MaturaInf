#Czy cyfra dzieli się przez wszystkie wykładniki liczby z pominięciem zera

def odkryte(n):
    tekst = str(n)
    dl = len(tekst)
    log = True
    for i in range(dl):
        if int(tekst[i]) == 0:
            continue
        if n % int(tekst[i]) != 0:
            return False
    return log


print(odkryte(2436))
