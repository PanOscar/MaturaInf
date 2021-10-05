import math

def nwd_optymalny(a, b):
    while b != 0:
        temp = b
        b = a%b
        a = temp
    return a

def nww(a,b):
    return (a*b)//nwd_optymalny(a,b)

print(nww(10,6))


print((10*6)//math.gcd(10,6))