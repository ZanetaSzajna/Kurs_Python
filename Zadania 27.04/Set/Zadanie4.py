"""
Napisz skrypt, który podaną listę podzieli na 3 równe listy i odwraca każdą z tych.

input: [1, 2, 3, 4, 11, 12, 13, 14, 21, 22, 23, 24]

"""
Number = ['1','2', '3', '4', '11', '12', '13', '14', '21', '22', '23', '24']
First = Number[0:4]
Second=Number[4:8]
Third=Number[8:]
First.reverse()
Second.reverse()
Third.reverse()
print(First)
print(Second)
print(Third)
print("----------------------------------------------------------------------------------------------")

lenght=len(Number)
div=int(lenght/3)

First1=Number[:div]
Second1=Number[div:div*2]
Third1=Number[div*2:]
First1.reverse()
Second1.reverse()
Third1.reverse()
print(First1)
print(Second1)
print(Third1)