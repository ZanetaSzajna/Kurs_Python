"""
Algorytm deszyfrowania:
Napisz program, który deszyfruje zaszyfrowany tekst, wprowadzony przez użytkownika, używając prostej metody deszyfrowania przesunięciowego.
 Program powinien prosić użytkownika o wpisanie zaszyfrowanego tekstu oraz przesunięcie, o które został on zaszyfrowany.
 Następnie program powinien wypisać odszyfrowany tekst.

"""

alphabet = 'abcdefghijklmnopqrstuvwxyz'
translate = {}
shift = 99
while True:
    shift = input('Please enter the number of places to shift:')
    if shift.isdecimal():
        shift = int(shift)
        if 0<= shift < 26:
            break
    print('You need to enter a number between 0 and 25!')
# build translation dictionary
for letter in alphabet:
    translate[letter] = alphabet[(alphabet.index(letter)-shift) % 26]
sentence = input('Please enter a sentence:').lower()
crypted = ''
for letter in sentence:
    if letter in translate:
        crypted += translate[letter]
    else:
        crypted += letter
print('The encrypted sentence is:', crypted)