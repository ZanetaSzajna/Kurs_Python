"""
Napisz program, który używa pętli for do wyznaczenia największej liczby spośród:
[3, 6, 12, 54, 21, 35, 2, 9]
[9, 0, 30, 25, 44, 71, 42, 5, 17, 89, 39, 10, 22, 1]
Liczb w dowolnu sposób wprowadzonych przez użytkownika.

"""
print("Podpunkt a)")
set_number =[3, 6, 12, 54, 21, 35, 2, 9]

Biggest=0

for number  in set_number:
    if Biggest < number:
        Biggest = number
print("The biggest number in set", set_number," is :", Biggest)
print("------------------------------------------------------------------------------------------")
print("Podpunkt b")
set_numberb=[9, 0, 30, 25, 44, 71, 42, 5, 17, 89, 39, 10, 22, 1]

B=0
for num in set_numberb:
    if B < num:
        B=num
print("The biggest number in set", set_numberb," is :", B)
print("------------------------------------------------------------------------------------------------")
print("Podpunkt c)")

user_numbers=input("Enter your number --> ")
set_user_number=[]
for n in user_numbers.split():
    set_user_number.append(int(n))
Biggest_user=0
for nC in set_user_number:
    if Biggest_user < nC:
        Biggest_user=nC
print("The biggest number in set", set_user_number," is :", Biggest_user)