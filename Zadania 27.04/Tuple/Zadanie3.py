"""
Stwórz krotkę liczb całkowitych. Poproś użytkownika o podanie dowolnej liczby.
Jeśli liczba znajduje się na krotce wyswietl jej indeks.
"""
Tuples =("15","25","6","7","25")
User_number=input("Enter number --> ")

instances = Tuples.count(User_number)

if instances > 0:
    print("Your number is in Tuple in place: ", Tuples.index(User_number))
else:
    print("Yours number isn't in tuples ")