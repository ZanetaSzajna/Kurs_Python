"""
Algorytm szyfrowania:
Napisz program, który zaszyfruje tekst, wprowadzony przez użytkownika, używając prostej metody szyfrowania przesunięciowego.
Program powinien prosić użytkownika o wpisanie tekstu oraz przesunięcie, o które chce przesunąć każdą literę tekstu.
Następnie program powinien wypisać zaszyfrowany tekst.
"""

sentence = input("Please enter a sentence --> ")
shift = int(input("Please enter the number of places to shift --> "))
encrypted =''
k=0
for letetr in sentence:

    if letetr.isupper() == True:
        if ord(letetr) < ord('A') or ord(letetr) > ord("Z"):
            encrypted += letetr
        elif ord(letetr) > ord("V"):
            encrypted += chr(ord(letetr)+shift-26)
        else:
            encrypted += chr(ord(letetr)+shift)
    else:
        if ord(letetr) < ord('a') or ord(letetr) > ord("z"):
            encrypted += letetr
        elif ord(letetr) > ord("v"):
            encrypted += chr(ord(letetr) + shift - 26)
        else:
            encrypted += chr(ord(letetr) + shift)
print(encrypted)


