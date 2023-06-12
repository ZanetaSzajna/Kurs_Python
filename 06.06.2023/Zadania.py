class Student:
    school="UAM"
    def __init__(self, first, last, age):
        self.firstname=first
        self.lastname=last
        self.age=age

    def email(self):
        return  f"{self.lastname}.{self.firstname[0]}@{self.school.lower()}.pl"

    def sound(self, number):
        return " Hahahahahahahah "*number


anna = Student("Anna", "Nowak", 23)

print(anna.firstname)
print(anna.email())

print(anna.__dict__)

anna.lastname="kropka"
print(anna.email())
print(anna.sound(3))