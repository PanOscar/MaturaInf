def insetion(x):
    n = len(x)
    for i in range(1, n):
        aktualny = x[i]
        inny = i-1
        while inny >= 0 and aktualny < inny:
            x[inny+1] = x[inny]
            inny -= 1
        x[inny+1] = aktualny
