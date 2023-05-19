"""
Skorzystaj ze swojego kodu bmi.py.
Rozbij liczenie bmi na funkcję obliczającą bmi na podstawie danych użytkownika oraz zwracającą odpowiednią wartość
(niedowaga, waga normalna, nadwaga, otyłość) w zależności od otrzymanego parametru.

"""
weight = float(input("Enter your weight--> "))
height = float(input("Enter your height--> "))

def bmi(weight, height):
    BMI= round(weight/(height**2),2)

    if 0 <= BMI <= 18.49:
        print(f"Your BMI is {BMI} and indicates that  you have underweight")
    elif 18.5 <= BMI <= 24.99:
        print(f"Your BMI is {BMI} and indicates that  you have correct weight")
    elif 25 <= BMI <=29.9:
        print(f"Your BMI is {BMI} and indicates that  you have overweight")
    else:
        print(f"Your BMI is {BMI} and indicates that  you have obesity")

bmi(weight, height)
