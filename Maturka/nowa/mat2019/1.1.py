n = 10
A = [ None, 9,3,1,5,11,15,3,2,10,18]

# wyszukiwanie binarne
def szukaj_binarnie_i(A):
    n = len(A) - 1
    lewy, prawy = 1, n
    while lewy < prawy:
        srodkowy = (lewy+prawy)//2
        if A[srodkowy]%2 != 0:  # jeśli środkowy jest nieparzysty
            lewy = srodkowy + 1
        else:                   # jeśli środkowy jest parzysty
            prawy = srodkowy 
    return A[prawy]

print(szukaj_binarnie_i(A))

def szukaj_binarnie(B,x):
    n = len(B) - 1
    lewy, prawy = 0, n
    while lewy <= prawy:
        srodkowy = (lewy+prawy) // 2
        if B[srodkowy] == x:
            return srodkowy + 1
        if B[srodkowy] < x: # jeśli środkowy jest nieparzysty
            lewy = srodkowy + 1
        else:  # jeśli środkowy jest parzysty
            prawy = srodkowy
    return False

print(szukaj_binarnie([1,2,3,6,7,8,9,10,12],12))

