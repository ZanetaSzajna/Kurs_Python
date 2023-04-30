"""
Napisz prostą grę, w której użytkownik musi zgadnąć liczbę od 0 - 20 ukrytą w programie (np. secret_num = 5).
Pytaj użytkownika o podanie liczby tak długo, aż nie zgadnie.
"""
number=int(input("Please enter number between 0 to 20--> "))
secret_num = 3
if number in range(0,21):
    while number< secret_num or number> secret_num:
        if number in range (0,21):
            number=int(input("Try Again-->  "))
        else:
            number=int(input(" Your number must be i range 0 to 20 --> "))

    print("You win")

else:
    print("You must enter  number between 0 to 20 !!!")