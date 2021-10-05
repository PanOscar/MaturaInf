""" ANAGRAM SOLVER
Mam problem z pisaniem słowa z odpowiednią kolejnoscią liter
Znajdź słowo które może pasować do mojego przez przestawienie liter

Wprowadzamy literki w stringu i proponowane słowa w tablicy
Napisz funkcję która będzie wypisywać nam w tablicy słowa które pasują do naszych
wypisanych liter z naszej propozycji słów

x - niezrozumiałe słowo
A - tablica prawdopodobnych słów

anagram("orpt", ["port", "trop","ortp","ananas"]) -> ["port","trop","ortp"]
anagram("taat", ["tata", "takt","taaat","atak"]) -> ["tata"]
anagram("oob", ["bob", "baobab"]) -> []
"""


def anagram(x, A):
    M = []
    moje = list(x)
    moje.sort()
    for i in range(len(A)):
        obce = list(A[i])
        obce.sort()
        if obce == moje:
            M.append(A[i])
    return M


print(anagram("orpt", ["port", "trop", "ortp", "ananas"]))
