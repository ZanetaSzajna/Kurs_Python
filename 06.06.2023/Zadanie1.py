class Dog:
    def __init__(self, name, color, hair, breed):
        self.name = name
        self.color = color
        self.hair = hair
        self.breed = breed

    def behaviour(self):
        return "wow, wow. wow"

mecenas = Dog("Mecenas", "brown", "short", "labrador")
print(mecenas.breed)
print(mecenas.behaviour())

hugo = Dog("Hugo", "black", "long", "owczraek niemiecki")
print(hugo.breed)
print(hugo.behaviour())