"""
Napisz grę kamień-papier-nożyce tak, aby korzystać z funkcji.
"""
import random

game={  "stone ":"k",
        "paperr":"p",
        "scissors": "n"
}
list_options=list(game.values())

def game(computer, user):
        if (computer == "k" and user== "n" ) or (computer == "n" and user == "p" ) or (computer == "p" and user == "k"):
                print("Sorry you lose you choose", user, "computer : ", computer)
        else:
                print("Congrats yu win !!!!!!!!!!!! you choose", user,"computer " ,computer)

computer = random.choice(list_options)
user = input(" Chosse k - stone, p-paper, n-scissors --> ")
game(computer, user)