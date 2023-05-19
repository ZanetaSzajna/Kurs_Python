"""
Stwórz grę wisielec “bez wisielca”. Komputer losuje wyraz z dostępnej w programie listy wyrazów.
Wyświetla zamaskowany wyraz z widoczną liczbą znaków (np. ‘- - - - - - -‘)Użykownik podaje literę.
Sprawdź, czy litera istnieje w wyrazie. Jeśli tak, wyświetl mu komunikat: “Trafione!” oraz napis ze znanymi literami.
W przeciwnym wpadku pokaż komunikat: “Nie trafione, spróbuj jeszcze raz!”.
Możesz ograniczyć liczbę prób do np. 10.
"""
import random

word_list=["apple", "orange","pen","pencil", "glass", "laptop", "home", "phone", "word", "vacation", "holiday","name", "coffe"]
keyword = random.choice(word_list)
gues_word=list(keyword)


for i in range(len(keyword)):
    gues_word[i] = '_'

def hangman_game():
    round = 10
    while round > 0:
        print(" ")
        print(f"You have {round} lives" )
        print("")
        print(" ".join(gues_word))
        user_letter = input("Enter yor letter --> ")
        if user_letter in keyword:
             for index in range(len(keyword)):
                 if keyword[index] == user_letter:
                     print("congratulations you have successfully guessed the letter ")
                     gues_word[index]=user_letter
             if "".join(map(str,gues_word)) == keyword:
                 print("You win !!!!!!!!!!!!!!!!")
                 break;
        else:
            round -=1
            print("Try again ")
hangman_game()






