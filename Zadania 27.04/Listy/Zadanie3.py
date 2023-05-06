"""
 Dla podanej przez użytkownika liście liczb całkowitych sprawdź czy pierwszy i ostatni element są takie same.
"""
numebers = input("Please eneter numebers separate space: ")
list = numebers.split()
print(list)

lenght =len(list)
first =list[0]
last=list[lenght-1]
if first == last:
    print("First element in list is equal last element")
else:
    print("First element in list is different from last element")

