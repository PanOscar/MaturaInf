"""
Funkcja będzie zwracać największą wartość mnożenia
5 kolejnych po sobie liczb
greatestProduct("123834539327238239583") --> 3240 ponieważ 3*9*5*8*3 = 3240
"""
def greatestProduct(x):
    max = 0
    for i in range(len(x) - 4):
        roz = int(x[i]) * int(x[i + 1]) * int(x[i + 2]) * int(x[i + 3]) * int(x[i + 4])
        if roz > max:
            max = roz
    return max

print(greatestProduct("123834539327238239583"))