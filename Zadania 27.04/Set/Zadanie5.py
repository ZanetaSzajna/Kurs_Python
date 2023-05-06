""""
Porównaj zachowanie discard() vs remove() dla typu set.
"""
lista=["Berlin","Wien","Venice","Warsaw", "Roma"]
set_list=set(lista)
print(set_list)

print("Use remove: ")
set_list.remove("Warsaw")
print(set_list)

print("Use discard ")
set_list.discard("Roma")
print(set_list)


print("Use discard ")
set_list.discard("Warsaw")
print(set_list)
"""
print("Use remove: ")
set_list.remove("Roma")
print(set_list)

W przypadku remove  pojawia się błąd gdy nie ma lelemetu na liście 
Traceback (most recent call last):
  File "C:\Users\Mati\Desktop\Kurs Python\Zadania 27.04\Set\Zadanie5.py", line 22, in <module>
    set_list.remove("Roma")
KeyError: 'Roma'

"""