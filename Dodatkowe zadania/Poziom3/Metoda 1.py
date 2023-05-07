"""
Algorytm szyfrowania:
Napisz program, który zaszyfruje tekst, wprowadzony przez użytkownika, używając prostej metody szyfrowania przesunięciowego.
Program powinien prosić użytkownika o wpisanie tekstu oraz przesunięcie, o które chce przesunąć każdą literę tekstu.
Następnie program powinien wypisać zaszyfrowany tekst.
"""

encrypted=''
sentence=input("Please enter e sentence --> ")
shift = int(input("Please enter the number of places to shift --> "))

for letter in sentence:

        if ord(letter) < ord("a") or ord(letter)>ord("z"):
                encrypted += letter
        elif ord(letter)+shift > ord("z"):
                encrypted += chr(ord(letter)+shift-26)
        else:
                encrypted+= chr(ord(letter)+shift)
print(encrypted)
