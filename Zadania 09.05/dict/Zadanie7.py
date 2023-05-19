"""
 Usuń duplikat z podanej list i utwórz na jej bazie krotkę. Znajdź minimalną i maksymalną liczbę w krotce.

"""

example_list = [34, 17, 25, 41, 12, 194, 41, 3, 12, 99, 94]
unique=[]

for i in example_list:
    if  i not  in unique:
        unique.append(i)
print(unique)
tuple_to_list = tuple(unique)
print(max(tuple_to_list))
print(min(tuple_to_list))