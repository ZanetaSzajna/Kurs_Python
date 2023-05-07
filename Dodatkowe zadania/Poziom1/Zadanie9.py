"""
Napisz program, który używa pętli for do wyznaczenia liczby wystąpień
litery "a" w podanym przez użytkownika ciągu znaków.
"""

sentence=input("Enter Your sentence--> ")
letter_a=[]
for i in sentence:
    if i =="a" or i=="A":
        letter_a.append(i)


print("In your sentence letter a appears ",len(letter_a), "times")

