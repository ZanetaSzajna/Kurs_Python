"""
Stwórz zmienną password.
Hasło powinno składać z liter i cyfr, zwierać conajmniej 1 małą literę, 1 dużą literę i mieć długość conajmniej 8 znaków.
Poinformuj użytkownika, jeśli wpisane hasło jest nie poprawne. Wyświetl różne komunikaty w zależności od rodzaju błędu.
"""
password=input("Enter your password --> ")
lenght_word=len(password)

if lenght_word <= 8:
    print("Your password must contain 8 characters")
elif password.isalpha() == True:
    print("Your password must contain at least one digit")
elif password.islower() == True:
    print(" Your password must contain at least one capital letter")
else:
    print("Your password is correct")
