"""
 W kodzie BMI ufamy, że użytkownik podaje wartość w kilogramach lub w metrach i rzutujemy do float.
 Co jeśli użytkownik poda wartość 60 kg ? Zmodyfikuj kod z ostatnich zajęć tak, aby wykluczyć powyższy przypadek.
"""




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

def main():

    weight = float(input("Enter your weight--> "))
    height = float(input("Enter your height--> "))
    bmi(weight,height)

try:
    main()
except (ValueError,ZeroDivisionError, TypeError) as error:
    print(error)
