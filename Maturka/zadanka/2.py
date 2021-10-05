"""
Generator Hasztagów

-Musi zaczynać się (#) hasztagiem.
-Wszystkie słowa muszą mieć wielką pierwszą literę
-Jeżeli ostateczny wynik ma więcej niz 140 znaków to zwróci False.
-Jeżeli nic nie wpiszemy w input to też zwróci False

Przykłady:
"czesć To JA i moje jedzenie" -> "#CzesćToJaIMojeJedzenie"
"     na       urolpie    " ->  "#NaUrolpie"
"""

def generate_hashtag(s):
    word = '#'
    s = s.lower()
    x = list(s)
    a = []
    if 140 > len(x) > 0:
        if x[0].isalpha():
            x[0] = x[0].upper()
        for k,i in enumerate(x):
            if i.isspace():
                try:
                    x[k+1] = x[k+1].upper()
                except:
                    continue
            if i.isalpha():
                word += i
        return word
    else:
        return False

x = generate_hashtag(input("wpisz slowo"))
print(x)