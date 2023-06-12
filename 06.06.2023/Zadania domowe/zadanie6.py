"""
 Utwórz klasę Pracownik.

Pracownik ma stanowisko, wynagrodzenie, imie, nazwisko, staz pracy.

Pracownik powinen miec roczne podwyżki wg. dowolnie wymyślonego sposobu liczenia.
racownik powinen odprowadzać podatek o wysokoci zależnej od swoich zarobków oraz minimalną składkę zdrowotną.

Pracownik powinien mieć pole typu boolowskiego zawierające status studenta. Jeśli pracownik jest studentem jego składka zdrowotna wynosi 0%.

Wszyscy pracownicy mają wspólną nazwę firmy. Spółgłoski imienia i nazwiska wraz z nazwą firmy .com tworzą adres mailowy. Np.

"""

class Employee:

    company_name = "DreamTeams"
    def __init__(self, name,last_name, job_title, seniority,grade, pay ):
        self.name=name
        self.last_name=last_name
        self.jo_title = job_title
        self.seniority = seniority
        self.grade = grade
        self.pay=pay

    def rise(self):
        pass

