"""
Pozwól użytkownikowi wprowadzić dowolną liczbę imion ciągiem
 (np.jako jeden string rozdzielonych przecinkiem lub białym znakiem).
  Następnie powitaj każdą osobę na liście.
"""
names=input("Please enter name of  person separate space --> ")
list_names=names.split()

for personn in list_names:
    print("Hello ", personn)
