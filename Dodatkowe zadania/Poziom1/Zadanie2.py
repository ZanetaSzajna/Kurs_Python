"""
Napisz program, który używa pętli for do wyświetlenia tabliczki mnożenia (1 do 10) dla wybranej przez użytkownika liczby do.
"""
user_number = int(input("Enter number --> "))

for i in range(1,11):
    print(user_number,"*",i, "=", user_number*i)
