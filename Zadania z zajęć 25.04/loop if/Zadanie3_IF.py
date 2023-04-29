"""
Stwórz skrypt, który przyjmuje 3 opinie użytkownika o książce.
Oblicz średnią opinię o książce. W zależności od wyniku dodaj komunikaty.
Jeśli uzytkownik ocenił książkę na ponad 7 - bardzo dobry, ocena 5-7 przeciętna, 4 i mniej - nie warta uwagi.
"""
review1 = int(input("Rate the book ona scale of 1-10 --> "))
review2 = int(input("Rate the book ona scale of 1-10 --> "))
review3 = int(input("Rate the book ona scale of 1-10 --> "))
average=(review1+review3+review2)/3
if average > 7:
    print("Book rating is very good")
elif 5 <= average <= 7:
    print("Book rating is average")
else:
    print("Book rating is not worth attention ")