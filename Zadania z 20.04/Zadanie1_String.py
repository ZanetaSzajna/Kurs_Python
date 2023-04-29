"""
Stwórz zmienną przechowującą wyraz o długości nieparzystej
większej niż 7 i zwróć łańcuch złożony z trzech środkowych znaków danego ciągu.
"""

wyraz= "samochody"
l=len(wyraz)
print(l)
print("Środkowe trzy litery to: ",wyraz[(l//2)-1:((l//2-1)+3)])
