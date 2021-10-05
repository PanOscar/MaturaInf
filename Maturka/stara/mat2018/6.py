plik = open('slowa.txt')
x = [y.split(" ") for y in (x.replace('\n','')for x in plik.readlines())]
plik.close()

print(x)

def zad1(x):
    wynik = 0
    for i in range(len(x)):
        for j in range(len(x[i])):
            if x[i][j][-1] == "A":
                wynik +=1
    return wynik

print(zad1(x))

print(x)
def zad2(x):
    wynik = 0
    print(x)
    for i in range(len(x)):
        if len(x[i][0]) <= len(x[i][1]):
            if x[i][0] in x[i][1]:
                wynik +=1
    return wynik

print(zad2(x))
print(zad2([["ADC","ADCDC"]]))