def potegowanie(a,b):
    suma = 1
    for i in range(0,b):
        suma *= a
    return suma

print(potegowanie(2,2))

def potegowanie_rek(a,b):
    if b==0:
        return 1
    else:
        return a*potegowanie_rek(a, b-1)

print(potegowanie_rek(2,2))