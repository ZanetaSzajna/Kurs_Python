"""
Oblicz koszt wyprawy znając dystans, spalanie na 100km i cenę litra benzyny.
Załóżmy, że spalanie na 100km wynosi 6,4 l, trasa to 120km, litr benzyny kosztuje 5,04 zł.
"""

dys=120
spal=6.4
paliwo=5.04

zuzycie=dys/100
koszt=zuzycie*paliwo*spal

print("koszt wynosi:",(koszt,))


"""
Zmodyfikuj skrypt tak, by przyjmował wartości od użytkownika.


"""
dystans = float(input("Podaj ile kilomterów masz do przejechania --> "))
spalamie =float(input("ile Twoje auto spali paliwa na 100km --> "))
cena_paliwa=float(input("Ile kosztuje paliwo --> "))

zuzyte_litry=(spalamie*dystans)/100
koszt_wyprawy=zuzyte_litry*cena_paliwa

print("Koszt wyprawy to ", round(koszt_wyprawy,2))