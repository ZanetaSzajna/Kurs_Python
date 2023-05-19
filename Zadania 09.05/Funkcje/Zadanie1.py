import math
def oblicz_pole():

    radius = int(input("Enter value of the radius --> "))
    circle_area =round(math.pi * radius*radius,2)
    print(f"The area of a circle with radius {radius} is equal {circle_area}")
oblicz_pole()

