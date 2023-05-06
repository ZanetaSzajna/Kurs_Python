"""
Utwórz 2 krotki.
Następnie utwórz listę będącą połączeniem elementów o parzystym indeksie z pierwszej krotki,
oraz nieparzystych elementów z drugiej.
Przekształć powstałą listę w set.
"""

Tuple1=("Apple", "Banana", "Orange", "Lemon","Pear", "Grape","Raspberries")
Tuple2=("Tomato", "Cucumber", "Carrot","Potato","Cabbage","Broccoli","Beans","Latauce")

Fruits= Tuple1[0::2]
print("Fruits with even index in tuple1 ")
print(Fruits)
Vegetables=Tuple2[1::2]
print("Vegetables  with odd index in tuple2")
print(Vegetables)


List_baskets=list(Fruits+Vegetables)
print("List created with Fruits and vegetables: ")
print(List_baskets)
Set_baskets=set(List_baskets)
print("Set created with list ")
print(Set_baskets)