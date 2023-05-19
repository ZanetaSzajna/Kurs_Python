poem="""Szybko, zbudź się, szybko, wstawaj
Szybko, szybko, stygnie kawa
Szybko, zęby myj i ręce"""


poem = poem.replace(",", "")
poem= poem.lower()
poem=poem.split()
print(poem)

dict={}

for i in poem:
    if i in dict:
        dict[i]=+1
    else:
        dict[i]=1
print(dict)

for word, counter in dict