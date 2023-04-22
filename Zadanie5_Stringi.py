"""
Palindrom to wyrażenie brzmiące tak samo czytane od lewej do prawej i od prawej do lewej
np.: Kobyła ma mały bok. Pozwól użytkownikowi wprowadzić dowolne
"""
zdanie=input("Podaj zdanie--> ")
zdanie1=zdanie.lower()
polacz=zdanie1.replace(" ","")
polacz_od_konca=polacz[::-1]
print(polacz)
print(polacz_od_konca)

czy_palindrom = polacz==polacz_od_konca
print(czy_palindrom)

""""
Rozbudowane wersja
"""

zdanie=input("Podaj zdanie--> ")
zdanie1=zdanie.lower()
polacz=zdanie1.replace(" ","")
polacz_od_konca=polacz[::-1]
if polacz==polacz_od_konca:
    print("Podane przez Ciebie zdanie jest palindormem")
else:
    print("Podane przez Ciebie zdanie nie jest palindromem")
