"""
Napisz program, który używa pętli while do wyznaczenia liczby wystąpień litery "e" w podanym przez użytkownika ciągu znaków.
"""
sentence=input("Enter sentence--> ")
sentence="".join(sentence)
lenght=len(sentence)
print(lenght)
i =0
k=0
while i < int(lenght-1):
    i+=1
    if sentence[i]== "e" or sentence[i]=="E":
        k=k+1
    else:
        k=k
print("Letter e in your sentence appeared ", k,"times")