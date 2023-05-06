"""
Pobierz od użytkownika 10 liczb, wyświetl tylko te, które są nieparzyste.
"""
number= input("Enter 10 numbers, separate space -->  ")
list_number=number.split()
new_list=[]
if len(list_number) == 10:
    for num in list_number:
        if int(num) % 2 >0:
            print(num)
            new_list.append(num)
    print(new_list)
else:
    if len(list_number)>10:
        print("You entered more numbers")
    else:
        print("You have entered too few numbers")