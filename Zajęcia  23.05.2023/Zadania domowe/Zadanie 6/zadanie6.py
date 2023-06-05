"""
Rozpoznawanie kart. Utwórz plik zawierający numery kart kredytowych.
Sprawdź dla każdej kart jej typ.
Podziel kart do plików wg typów np. visa.txt, mastercard.txt, americanexpress.txt
"""

def check_cards():
    with open("credit_cards.txt",encoding='1250') as fopen:
        cards=fopen.read()
    visa_cards = []
    master_card = []
    american_express = []
    no_card = []

    cards = cards.replace(",", "").split()
    cards = list(cards)
    for card_num in cards:

        if card_num[0] == '4' and (len(card_num) == 16 or len(card_num) == 13):
            visa_cards.append(card_num+"\n")
        elif len(card_num) == 16 and (int(card_num[0:2]) in range(51, 56) or int(card_num[0:4]) in range(2221, 2721)):
            master_card.append(card_num+"\n")
        elif len(card_num) == 16 and card_num[0:2] in ('34', '37'):
            american_express.append(card_num+"\n")
        else:
            no_card.append(card_num+"\n")

    with open("VISA.txt", 'w') as visa:
        visa.writelines(visa_cards)
    with open("MsterCard.txt", 'w') as master:
        master.writelines(master_card)
    with open("AmericanExpres.txt", "w") as american:
        american.writelines(american_express)
    with open( "No_cards","w") as no_car:
        no_car.writelines(no_card)

check_cards()

print("Karty z pliku podzielone i zapisane ")