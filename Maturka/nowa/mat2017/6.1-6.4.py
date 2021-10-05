plik = open('dane.txt')
liczby = [x.replace('\n', '').split() for x in plik.readlines()]
plik.close()

print(liczby)
result = [list(x) for x in liczby]
result = [list(map(int,i) ) for i in result]
print(result)
#1.MinMax


def minmax(x):
    min = 256
    max = -1
    for i in range(len(x)):
        for j in range(len(x[i])):
            if x[i][j] > max:
                max = x[i][j]
            elif x[i][j] < min:
                min = x[i][j]
    return print(min, max)
minmax(result)

#2.Palindrom

def palindrom(x):
    roz = 0
    pal = [list(reversed(x[i])) for i in range(len(x))]
    for i in range(len(x)):
        if x[i] != pal[i]:
            roz += 1
    return print(roz)

palindrom(result)

#3. Sąsiadujące piksele

def sasiad(x):
    roz = 0
    w = len(x)
    for i in range(w):
        k = len(x[i])
        for j in range(k):
            """if j < 319 and i < 199:
                if abs(x[i][j] - x[i][j + 1]) > 128 or :
                    roz += 1
                    
                elif abs(x[i][j] - x[i + 1][j]) > 128:
                    roz += 1
            elif i == 199 and j < 319:
                if abs(x[i][j] - x[i][j + 1]) > 128:
                    roz += 1
            elif i < 199 and j == 319:
                if abs(x[i][j] - x[i + 1][j]) > 128:
                    roz += 1"""
            #####################
            if i == 0:
                if j==0:
                    if abs(x[i][j] - x[i][j+1]) >128 or abs(x[i][j] - x[i+1][j]) >128:
                        roz+= 1
                elif j==k-1:
                    if abs(x[i][j] - x[i][j-1]) >128 or abs(x[i][j] - x[i+1][j]) >128:
                        roz+= 1
                else:
                    if abs(x[i][j] - x[i][j+1])>128 or abs(x[i][j] - x[i][j-1]) >128 or abs(x[i][j] - x[i+1][j])>128:
                        roz+= 1
            elif i == w-1:
                if j==0:
                    if abs(x[i][j] - x[i][j+1]) >128 or abs(x[i][j] - x[i-1][j]) >128:
                        roz+= 1
                elif j==k-1:
                    if abs(x[i][j] - x[i][j-1]) >128 or abs(x[i][j] - x[i-1][j]) >128:
                        roz+= 1
                else:
                    if abs(x[i][j] - x[i][j+1]) >128 or abs(x[i][j] - x[i][j-1]) >128 or abs(x[i][j] - x[i-1][j])>128:
                        roz+= 1
            else:
                if j==0:
                    if abs(x[i][j] - x[i][j+1]) >128 or abs(x[i][j] - x[i+1][j]) >128 or abs(x[i][j] - x[i-1][j]) >128:
                        roz+= 1
                elif j==k-1:
                    if abs(x[i][j] - x[i][j-1]) >128 or abs(x[i][j] - x[i+1][j]) >128 or abs(x[i][j] - x[i-1][j]) >128:
                        roz+= 1
                else:
                    if abs(x[i][j] - x[i][j+1]) >128 or abs(x[i][j] - x[i][j-1]) >128 or abs(x[i][j] - x[i+1][j])>128 or abs(x[i][j] - x[i-1][j])>128:
                        roz+= 1

    return print(roz)

sasiad(result)

#4. Najdłuższa linia pionowa
def linia(x):
    max = 0
    w = 200
    k = 320
    for i in range(k):
        ile = 1
        for j in range(w-1):
            if x[j+1][i] == x[j][i]:
                ile +=1
                if ile > max:
                    max = ile
            else:
                ile = 1

    return print(max)
linia(result)
