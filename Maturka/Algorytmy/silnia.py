def silnia(n): return n*silnia(n-1) if n > 1 else 1

def silnia_r(n):
    if n > 1:
        return n*silnia(n-1)
    return 1

def silnia_i(n):
    s = 1
    for i in range(2, n+1):
        s *= i
    return s

print(silnia(5))
print(silnia_r(5))
print(silnia_i(5))