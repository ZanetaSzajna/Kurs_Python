"""
5 użytkowników poproś o podanie 4 przedmiotów szkolnych, sprawdź czy przedmioty powtarzają się na listach.
Wyświetl najpopularniejszy przedmiot. (Uwzględnij fakt, że użytkownicy mogą zapisać przedmioty małymi, drukowanymi lub zaczynając od dużej litery)

"""
school_subject=[]
popular=[]
m_popular=[]
for person in range(0,5):
    items=input("Enter  4 school subjects --> ").lower()
    list =items.split(" ")
    school_subject.append(list)

print(school_subject)

for row in school_subject:
    for elem in row:
        popular.append(elem)
for sub in popular:
    if popular.count(sub) >2 and m_popular.count(sub)==0:
        m_popular.append(sub)
print(m_popular)