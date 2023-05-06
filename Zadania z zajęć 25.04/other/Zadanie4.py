"""
Napisz grę - kamień (k) / papier (p) / nożyce (n)
Użytkownik podaje jedną z 3 figur.

Komputer losuje jedną z 3 figur.

Sprawdź kto wygrał tę rundę.

Zmień kod tak, by użytkownik mógł podac liczbę rund.

Wygrana jest podawana jako suma wygranych rund komputer vs użytkownik.

Zmień tak, by gracz mógł zakończyć grę w dowolnej chwili przez np. hasło ‘koniec’
"""

game=["k","n","p"]
round= int(input("How many rounds you want to play?--> "))
score_user=0
score_computer=0
for i in range(0,round):
    user=input("Please enter one of thi:  k- if you choose stone, n- if you choose scissors, p- if you choose paper --> ")
    import random
    computer = random.choice(game)
    print("Your choose ", user)
    print("Computer choose", computer)
    if user == "koniec":
        break
    if user == "k" and computer == "p":
        score_computer=score_computer+1
        print("The paper covers the stone so I'm sorry but you lose" )
    elif user =="k" and computer == "n":
        print("Stone dulls scissors, so you win")
        score_user=score_user+1
    elif user=="p" and computer=="k":
        print("The paper covers the stone so you win")
        score_user=score_user+1
    elif user =="p" and computer=="n":
        print("Scissors cut the paper, I'm sorry but you lose")
        score_computer=score_computer+1
    elif user =="n" and computer=="p":
        score_user=score_user+1
        print("Scissors cut the paper so you win")
    elif  user =="n" and computer=="k":
        print("Stone dulls scissors, I'mm sorry but you lose")
        score_computer=score_computer+1
    elif user == computer:
        print("You chose the same, so we have a draw")
    else:
        print("zła wartość")
print("SCORE: ")
print("Computer points: ", score_computer)
print("Your points", score_user)
print("RESULT: ")
if score_user>score_computer:
    print("You win this game")
elif score_computer==score_user:
    print("Draw")
else:
    print("Sorry, You lose")