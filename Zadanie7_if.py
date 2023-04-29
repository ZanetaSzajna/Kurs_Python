"""
Rozwiń kod bmi.py z pierwszych zajęć dodając teraz instrukcję warunkową,
która wyświetli w zależności od wyniku: niedowaga / waga normalna / nadwaga / otyłość.

"""
weight=float(input("Enter your weight--> "))
height = float(input("Enter your height--> "))

BMI=round(weight/(height**2),2)
print(BMI)

if 0 <= BMI <= 18.49:
    print("underweight")
elif 18.5 <= BMI <= 24.99:
    print("correct weight")
elif 25 <= BMI <=29.9:
    print("overweight")
else:
    print("obesity")