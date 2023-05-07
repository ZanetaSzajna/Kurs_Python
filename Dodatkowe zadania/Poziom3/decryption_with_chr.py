"""
Algorytm deszyfrowania:
Napisz program, który deszyfruje zaszyfrowany tekst, wprowadzony przez użytkownika, używając prostej metody deszyfrowania przesunięciowego.
 Program powinien prosić użytkownika o wpisanie zaszyfrowanego tekstu oraz przesunięcie, o które został on zaszyfrowany.
 Następnie program powinien wypisać odszyfrowany tekst.
"""

sentence = input("Please enter a sentence --> ")
shift = int(input("Please enter the number of places to shift --> "))
decryption =''
k=0
for letetr in sentence:

    if letetr.isupper() == True:
        if ord(letetr) < ord('A') or ord(letetr) > ord("Z"):
            decryption += letetr
        elif ord(letetr) < ord("F"):
            decryption += chr(ord(letetr)-shift+26)
        else:
            decryption += chr(ord(letetr)-shift)
    else:
        if ord(letetr) < ord('a') or ord(letetr) >= ord("z"):
            decryption += letetr
        elif ord(letetr) < ord("f"):
            decryption += chr(ord(letetr) - shift + 26)
        else:
            decryption += chr(ord(letetr) - shift)
print(decryption)
