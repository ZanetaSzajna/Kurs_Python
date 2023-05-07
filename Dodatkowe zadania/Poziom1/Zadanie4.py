"""
Napisz program, który używa pętli for do zsumowania wszystkich liczb parzystych z zakresu od 1 do 100.
"""
sum=0
for i in range(2,101,2):
    sum=sum+i
print(sum)
