def rozne_znaki(s=):
    r = 0
    A = []
    for i in range(len(s)):
        if s[i] not in A:
            A.append(s[i])
            r+=1
    return r

def whilee(s):
    r = 0
    A=[]
    i=0
    while i < len(s):
        j = 0
        while j < 100:

print(rozne_znaki("czesc"))