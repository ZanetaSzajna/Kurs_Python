"""
Zapytaj użytkownika o numer od 1 do 100,
jeśli użytkownik zgadnie liczbę ukrytą przez programistę wyświetl komunikat “gratulacje!”,
 w przeciwnym razie wyświetl “pudło!”.
"""
number=int(input("Please enter number from 1 to 100 --> "))
my_number=28

if 0 > number or number > 100:
    print("Your number must be  between 1 and 100 ")
elif number == my_number:
    print("Congratulation, You win ")
else:
    print("Mishit, Try Again ")