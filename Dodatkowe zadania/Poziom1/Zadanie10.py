"""
Napisz program, który używa pętli while do zsumowania wszystkich liczb nieparzystych z zakresu od 1 do 100.
"""
liczba=0
sum=0
while liczba < 100:
    liczba=liczba+1
    if liczba %2> 0:
        sum=sum+liczba
print(sum)