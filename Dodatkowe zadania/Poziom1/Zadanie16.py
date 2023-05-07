"""
Napisz program, który stworzy listę zawierającą 10 liczb losowych z zakresu od 1 do 100 (skorzystaj z modułu random)
 i  wyświetla tylko te, które są mniejsze od 50.
"""
import  random
list_random=[]
new_list=[]

for i in range(0,10):
    i=random.randrange(1,100)
    list_random.append(i)

for j in list_random:
    if j<50:
        new_list.append(j)
print(new_list)
