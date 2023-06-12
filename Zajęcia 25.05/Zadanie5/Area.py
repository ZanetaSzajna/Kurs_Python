def rectange_area(lenght,widht, hight ):
    area= 2(lenght*widht+lenght*hight+widht*hight)
def triangle_area(lenght, width, hight):
    triangle_area = (lenght*lenght*3**1/3+6*lenght*hight)//2

def circle_area(radius):
    import math
    area=radius*radius*math.pi

def menu():
    print(" Specify which rooms you want")
    first_room=input("what shape the first room is to have ?")
    if first_room == "rectangle":
        lenght = int(input("specify the length of the room "))
        widht = int(input("specify the widht of the room "))
        hight = int(input("specify the hight of the room "))
        rectange_area(lenght,widht,hight)
        print(f"Your room will have an area of {rectange_area()}")
    elif first_room == "triangle":
        lenght = int(input("specify the length of the room "))
        widht = int(input("specify the widht of the room "))
        hight = int(input("specify the hight of the room "))
        triangle_area(lenght,widht,hight)

