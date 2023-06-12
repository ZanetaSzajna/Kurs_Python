"""
Pomyśl co sprawia, że ssak jest ssakiem? Utwórz klasę ssaki. Stwórz kilka obiektów klasy ssaki np. wilk, koń, ssaki.

"""
class Mammals:
    def __init__(self, genre, living_environment, nutrition, reproduction):
        self.genre = genre
        self.living_envirnoment = living_environment
        self.nutrition = nutrition
        self.reproduction = reproduction


wolf =Mammals ("Wolf", "terrestrial mammals","carnivorous", "placentaly")
print(wolf.living_envirnoment)