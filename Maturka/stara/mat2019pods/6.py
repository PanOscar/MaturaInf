plik = open('przyklad.txt')
liczby = [x.replace('\n','')for x in plik.readlines()]
plik.close()

print(liczby[::2][::-1])
def plec(x):
    kobiety= 0
    mezczyzna =0
    for i in range(len(x)):
        if int(x[i][9])%2 ==0:
            kobiety+=1
        else:
            mezczyzna+=1
    return kobiety,mezczyzna

print(plec(liczby))

def miesiac(x):
    wynik = 0
    for i in range(len(x)):
        if int(x[i][2:4]) == 11 or int(x[i][2:4]) == 31:
            wynik+=1
    return wynik

print(miesiac(liczby))

def sprawdz(x):
    A=[]

    for i in range(len(x)):
        wynik = int(x[i][0])+int(x[i][1])*3+int(x[i][2])*7+int(x[i][3])*9+int(x[i][4])+int(x[i][5])*3+int(x[i][6])*7+int(x[i][7])*9+int(x[i][8])+int(x[i][9])*3+int(x[i][10])
        if wynik %10 !=0:
            A.append(x[i])
    return A

print(sprawdz(liczby))