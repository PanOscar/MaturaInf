import math

def l_p(n):
    for i in range(2,int(math.sqrt(n))+1):
        if n % i == 0:
            return "Liczba nie jest pierwsza"
    return "Liczba jest pierwsza"

n = int(input("wczytaj n"))
print(l_p(n))

#################################  BEZ FUNKCJI

x = int(input("wczytaj x"))
prime = True #wartość logiczna
for i in range(2, int(math.sqrt(x)) + 1):
    if x % i == 0:
        prime = False
        break #słówko kluczowe do zatrzymania działania pętli
if prime:
    print("Liczba jest pierwsza")
else:
    print("Liczba nie jest pierwsza")
