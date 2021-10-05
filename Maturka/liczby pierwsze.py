n = int(input("Wpisz liczbe: "))

"""
def siema (x):
    if x < 1:
        return "Ta liczba jest mniejsza od 1!"
    for i in range(2,x):
       if x%i == 0:
           return "To nie jest liczba pierwsza!"
       else:
           return "To liczba pierwsza!"

print (siema(n))
"""



asd = True

if n < 1:
    print("Ta liczba jest mniejsza od 0!")

else:
    for i in range(2, n):
        if n%i == 0:
            asd = False
            break

if asd:
    print ("To jest liczba pierwsza!")
else:
    print ("To nie jest liczba pierwsza!")


