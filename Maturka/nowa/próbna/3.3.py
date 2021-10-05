def dekodowanie(V, t, bity):
    a = [bin(x).lstrip("0b") for x in V]

    tekst = ""
    for j, i in enumerate(a):
        while len(i) < 8:
            x = i[::-1]
            x += "0"
            i = x[::-1]
        V[j] = i
        tekst += i
    n = len(tekst)
    s = ""
    A = ""
    l = 0
    for i in range(n):
        l += 1
        A += tekst[i]
        if l == bity:
            for i in t:
                for k, v in i.items():
                    if k == A:
                        s += v
            l = 0
            A = ""

    return s


print(dekodowanie([110, 64], [{"01": "K"}, {"10": "A"}, {"11": "J"}], 2))
