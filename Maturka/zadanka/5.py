""" Format Numeru Telefonu
Zamień tablicę składającą się z 9 liczb na podany format
[1, 2, 3, 4, 5, 6, 7, 8, 9] => returns "+48 123-45-67-89"

Spróbuj zapisać kod funckji w jednej lini
"""


def telefon(A):
    return "+48 {}{}{}-{}{}-{}{}-{}{}".format(*A)

print(telefon([1, 2, 3, 4, 5, 6, 7, 8, 9]))