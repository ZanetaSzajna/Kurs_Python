
def serach_email(search, email):
    email = ["nanana@wp.pl", "klllka@wp.pl", "kzsksk@wp.pl ", "ajses@we.p"]
    search = input("podaj adres maila którego suzkasz ")
    lenght = len(email)
    print(lenght)
    for i in len(email):
        print(i)
        if  email[i-1]==search:
            print("Jest")
        else:
            print("Nie ma na liście")
serach_email()