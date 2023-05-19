"""
Napisz program, który będzie sprawdzał, czy nasz samochód kwalifikuje się do zarejestrowania jako zabytek.
Program zacznie ze stworzonym słownikiem o trzech kluczach: marka (str) model (str) rocznik (int)
Wypisze ten słownik na ekran (bez żadnego formatowania)
Sprawdzi, czy samochód ma minimum 25 lat. Jeśli tak, wypisze komunikat:
“Gratulacje! Twój samochód (tutaj_marka) może być zarejestrowany jako zabytek.”
Jeśli nie spełnia powyższego warunku, wypisze komunikat:
“Twój samochód (tutaj_marka) jest jeszcze zbyt młody.”
Gdy program będzie poprawnie działał, pozmieniaj wartości słownika (ale nie klucze!), aby zobaczyć, czy progam również zmienia swoje zachowanie.
Kolejnym warunkiem, aby dostać “żółte tablice”, jest to, aby samochód posiadał co najmniej 75% oryginalnych części.
W naszym zadaniu zakładamy, że rzeczoznawca określił jego oryginalność w kategorii tak/nie.
Poniżej stworzenia i wyświetlenia słownika w zadaniu powyżej:
dopisz do słownika nowy klucz czy_oryginalny i ustaw jego wartość (typ: bool) wedle uznania.
ponownie wyświetl zmieniony słownik
Zmodyfikuj program tak, aby uwzględnił decyzję o możliwości zarejestrowania samochodu również od jego oryginalności. Dopisz odpowiednie komunikaty.
"""
import datetime

brand = input("Enter the brand of your car --->  ")
model = input("Enter your car model --> ")
year_first_registration = int(input("enter the date of first registration of your car--> "))
original = input(" Is it original  True/False -->  ")

dict_car = {"car": [brand, model, year_first_registration, original]}
print(dict_car)

Y = datetime.datetime.now()
year =Y.year
print(year)
def is_a_vintage_car(year, year_first_registration, original):
    if int(year)-year_first_registration >=25 and original == "True":
        print(f"Congratulations! Your car {brand} can be registered as a vintage ")
    elif int(year)-year_first_registration >=25 and original == "False":
        print("Your car", brand, "has", year-year_first_registration,"But doesn't has 75% original components")
    else:
        print(f"Your car {brand} is still too young ")
is_a_vintage_car(year, year_first_registration,original)