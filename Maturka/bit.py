def siema(v,t,bity):
    tekst = ''
    for i in range(len(v)):
        while len(v[i]) < 8:
            x = v[i][::-1]
            x +="0"
            v[i] = x[::-1]
        tekst += v[i]
    nowytekst = ""
    granice = 0
    odp = ""
    for i in range(len(tekst)-1):
        nowytekst += tekst[i]
        granice += 1
        if granice == bity:
            for j in range(len(t)):
                 for k ,v in t[j].items():
                    if v == nowytekst:
                        odp += k
                        granice = 0
                        nowytekst = ''
    return print(odp)

siema(['101001', '11000100'],[{'H':'001'},{'A':'010'},{'N':'011'},{'I':'100'}], 3)