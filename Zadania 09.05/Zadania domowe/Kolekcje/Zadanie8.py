"""
Utwórz słownik dla 10 krajów Europy zawierajacy listy 10 najpopularniejszych imion żeńskich.
Zapisz imiona w wersji anglojęzycznej. Dodaj wszystki listy razem. Nowa lista powinna zawierać 100 elementów.
Wyświetl tylko te imiona, które wystąpiły conajmniej w 3 krajach.
"""
names_dict= { "England": ["Olivia", "Amelia", "Isla","Ava", "Emily", "Isabella","Mia","Poppy","Ella","Lily"],
    "France": ["Emma""Jade","Louise","Alice","Chloe","Lina","Léa","Rose","Anna","Mila"],
    "Spain": ["Martina","Julia", "Laia", "Lucia" "Maria", "Emma","Noa","Paula","Ona","Aina"],
    "Holland":["Sophie","Julia","Lieke","Emma","Sanne","Anna","Lotte","Eva","Mia","Lisa"],
    "Ireland": ["Emily","Sophie","Emma","Grace","Lily","Sarah","Lucy","Ava","Chloe","Katie"],
    "Norway": ["Emma","Nora","Olivia","Sara","Emilie","Lea","Sophie","Ella","Amaile","Mia"],
    "Scotland":["Olivia","Emily","Isla","Sophie","Amelia","Jessica","Ava","Ella","Charlotte","Aria"],
    "Switzerland":["Emma","Mia","Sophie","Lina","Lena","Lea","Lara","Emily","Nina","Anna"],
    "Italy": ["Sophie","Julia","Aurora","Alice","Ginevra","Emma","Giorgia","Greta","Beatrice","Anna"],
    "Sweden": ["Alice","Mia","Lilly","Ella","Wilma","Ebba","Olivia","Astrid","Alma","Elsa"]}

#print(names_dict)

lista = list(names_dict.values())

list_names=[]
popular_name=[]
for row in lista:
    for elem in row:
        list_names.append(elem)
#print(list_names)

for name in list_names:
    if (list_names.count(name)>2 ) and (popular_name.count(name)==0):
        popular_name.append(name)
print(popular_name)


