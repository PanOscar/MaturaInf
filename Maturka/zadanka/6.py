"""Zliczanie zmian
Stwórz algorytm zwracający liczbę zmian by posortować daną tablicę
od najmniejszej do największej liczby

zlicz([1,2,3,4]) // 0 zmiany

zlicz([1,3,2,4]) // 1 zmiana: 3 z 2

zlicz([4,1,2,3]) // 3 zmiany: 4 z 1, 4 z 2, 4 z 3

zlicz([4,3,2,1]) // 6 zmian: 4 z 3, 4 z 2, 4 z 1, 3 z 2, 3 z 1, 2 z 1

"""


def zlicz(arr):
    n = len(arr)
    licz = 0
    for i in range(n):
        zmienna = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                licz +=1
                zmienna = True
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
        if zmienna == False:
            return licz
    return licz

print(zlicz([3,1,4,2]) )