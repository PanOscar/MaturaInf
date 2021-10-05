""" Choinka
Przyjmujemy liczbę n
w zależności od tego n będziemy budować choinkę

n = 3  ----> ["  *  ",
              " *** ",
              "*****"]
n = 5  ----> ["    *    ",
              "   ***   ",
              "  *****  ",
              " ******* ",
              "*********"]
"""
def choinka(n):
    list = []
    for i in range(n):
        word = " " * (n - i - 1) + "*" * (i * 2 + 1) + " " * (n - i - 1)
        list.append(word)
        print(word)
    return list

print(choinka(4))