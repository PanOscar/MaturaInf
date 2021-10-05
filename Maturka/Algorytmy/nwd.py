def nwd_klasyczny(a, b):
    while a != b:
        if a > b:
            a -= b
        else:
            b -= a
    return a

def nwd_optymalny(a, b):
    while b != 0:
        temp = b
        b = a%b
        a = temp
    return a

print(nwd_klasyczny(10,8))
print(nwd_optymalny(10,8))