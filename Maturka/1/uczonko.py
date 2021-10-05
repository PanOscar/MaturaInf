x = 6
# Liczba x u góry jest równa 6

x = "jakiś napis"

"""
Oooo tam góry 
jest jakis napis
"""
# typy logiczne
x = False
x = True

#lista
x = [1,2,3,"czesc", False]

x = input("Wprowadź tekst\n") # wprowadzanie danych STRING
# \n przejscie do następnej lini
print(x)

y = int(input("wprowadź liczbę"))
print(y*y)

text = "Pies domowy (Canis lupus familiaris) – udomowiona forma wilka szarego, ssaka drapieżnego z rodziny " \
    "psowatych (Canidae), uznawana przez niektórych za podgatunek wilka, a przez innych za odrębny " \
    "gatunek[potrzebny przypis], opisywany pod synonimicznymi nazwami Canis lupus " \
    "familiaris lub Canisfamiliaris. Od czasu jego udomowienia powstało wiele ras, znacznie różniących się morfologią " \
    "i cechami użytkowymi. Rasy pierwotne powstawały głównie w wyniku presji środowiskowej. Rasy " \
    "współczesne uzyskano w wyniku doboru sztucznego.".lower()
x = input("8. Sprawdź czy występuje podany tekst w zdaniu ").lower()
if x in text:
    print("Wystepuje")
else:
    print("Ni ma")
