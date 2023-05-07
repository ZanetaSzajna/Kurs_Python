"""
Napisz skrypt orzeł 🦅 / reszka 🪙, w której “komputer rzuca monetą” - losuje wynik.
Program powinien pytać użytkownika, czy chce rzucać monetą ponownie, a także podawać wynik każdego rzutu.
Napisz skrypt orzeł 🦅 / reszka 🪙, w której “komputer rzuca monetą” - losuje wynik. Program powinien pytać użytkownika, czy chce rzucać monetą ponownie,
a także podawać wynik każdego rzutu.

"""
import random

list = ["heads", "tails"]
computer=random.choice(list)
print("I tossed a coin .........  and it came up -->", computer)
play_game="y"
i=True
while i:
    play_game = input("Do you want to toss a coin again if  yes  choose (y) if no chose  (n) --> ")
    if play_game == 'y':
        computer=random.choice(list)
        print("I toss a coin .........  and it came up -->", computer)
    elif play_game == "n":
        print(" Thanks for games !!!!!")
        break


