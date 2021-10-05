def szczyt(X, Y):
    n = len(X)
    for i in range(n):
        zmienna = False
        for j in range(0, n - i - 1):
            if (X[j] / Y[j]) > (X[j + 1] / Y[j + 1]):
                zmienna = True
                X[j + 1], X[j] = X[j], X[j + 1]
                Y[j + 1], Y[j] = Y[j], Y[j + 1]
        if not zmienna:
            break
    return X, Y


X = [1, 3, 2, 1, -2]
Y = [3, 4, 1, 3, 2]
print(szczyt(X, Y))

def szczyty(X,Y):
    n = len(X)
