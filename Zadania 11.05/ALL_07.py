""""
Napisz program, który na podstawie numeru karty odpowie czy ma doczynienia z Visą, MasterCard, a może AmericanExpress.

All Visa card numbers start with a 4. New cards have 16 digits. Old cards have 13.

MasterCard numbers either start with the numbers 51 through 55 or with the numbers 2221 through 2720. All have 16 digits.

American Express card numbers start with 34 or 37 and have 15 digits.
"""
def corect_number(card_number):
    card_number.replace(" ","")
    card_number.replace("-","")
    if  card_number.isdigit():

        return True
    else:
        return False

def get_card_number():
    while True:
        number = input("Please enter  cards number --> ")
        if corect_number(number):
            print("Yes")
            break
        else:
            print("Nope")
            print("Try again ")
    return number

def visa(card_number):
   if card_number[0]=='4' and (len(card_number)==16 or len(card_number)==13):
       return True
   else:
       return False
def Master_card(card_number):
    if (int(card_number[0:2]) in range(51,56) or int(card_number[:4]) in range(2221, 2721)) and len(card_number)==16:
        return True
    else:
        return  False
def american_expres(card_number):
    if int(card_number[:2] in ('34','38')) and len(card_number)==15:
        return True
    else:
        return False

num=get_card_number()
print("NUMER KARTY:", num)
if visa(num):
    print("VISA")
elif Master_card(num):
    print("master cards")
elif american_expres(num):
    print("American Expres")


