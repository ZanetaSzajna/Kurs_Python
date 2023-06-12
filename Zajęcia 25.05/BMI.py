weight = float(input("Enter your weight--> "))
height = float(input("Enter your height--> "))

def bmi(weight, height):
    BMI= round(weight/(height**2),2)

    if 0 <= BMI <= 18.49:
        print("underweight")
    elif 18.5 <= BMI <= 24.99:
        print(" correct weight")
    elif 25 <= BMI <=29.9:
        print(" overweight")
    else:
        print("obesity")

bmi(weight, height)


def calculate_bmi(weight, height):
    bmi = weight / (height ** 2)
    if bmi < 18.5:
        answer = read_from_file('Underweight.txt')
    elif bmi < 25:
        answer = read_from_file('Normal.txt')
    elif bmi < 30:
        answer = read_from_file('Overweight.txt')
    else:
        answer = read_from_file('Obese.txt')
    return answer


def read_from_file(filename):
    with open(filename) as f:
        lines = f.read()
        return lines