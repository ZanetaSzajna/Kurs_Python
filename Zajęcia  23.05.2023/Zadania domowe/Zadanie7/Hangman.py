import random

print("select the category from which the word is to be drawn ")
print(" Category:  Animal, Cars brand, forest, fruit, sports, ")
category = input( "-->" ).lower()
list_word=[]
def choose_word(category):
    if category == "animal":
        with open("Animals.txt") as animal:
            word=animal.readlines()
            return word
    elif category == "cars brand":
        with open("cars.txt") as car:
            word=car.readlines()
            return word
    elif category=="forest":
        with open("forest.txt") as forest:
            word = forest.readlines()
            return word
    elif category == "fruit":
        with open("friut.txt") as fruit:
            word=fruit.readlines()
            return  word
    elif category =="sports":
        with open("sports.txt") as sport:
            word =sport.readlines()
            return  word
    else:
        print("there is no such category ")

words=choose_word(category)
keyword=random.choice(words)
keyword=str(keyword).lower().strip()
gues_word=list(keyword)

for i in range(len(keyword)):
    gues_word[i]="_"
print(keyword)
def hangmman_game():
    # określenie liczby rund
    round= 10

    while round > 0:
        print("")
        # poinformowanie gracza  o ilości rund
        print(f" You have {round} rounds to guess the password")
        print(" ")
        #  wyświetenie zaszyfrowaneh=go hasłą
        print(" ".join(gues_word))
        # podanie przez użytkownaika litery
        user_letter= input("Enter yor letter --> ")
        #  sprawdzenie czy podana litera jest w haśle
        if user_letter in keyword:
            for letter in range(len(keyword)):
                if keyword[letter] == user_letter:
                    print("congratulations you have successfully guessed the letter ")
                    gues_word[letter] = user_letter

            if "".join(map(str, gues_word)) == keyword:
                print("You win !!!!!!!!!!!!!!!!")
                break;
        # jeżeli nie odejmujemy jedą roundę
        else:
            round -= 1
            print(f"Sorry, {user_letter} is not in the keyword. Try Again ")
        #  wyświetenie zaszyfrowaneh=go hasłą
        print(" ".join(gues_word))
        #Pytaniie czy użytkownik chce odgadąć całe hasło
        question = input("Would you like to guess the word ? Yes/No -->  ")
        #Jezeli tak  to sprawdzamy czy to prawidłowe słowo
        if question == "Yes" or question == "yes":
            user_word = input("Enter word --> ")
            if user_word == keyword:
                    print("You win !!!!!!!!!!!!!!!!")
                    break;
            # jeżeli nie zgadnie hasła wracamy do gry ale tracimy jedną szansę
            else:
                round-= 1
                print("Oh no,  it is not this word, Try Again ")

hangmman_game()
