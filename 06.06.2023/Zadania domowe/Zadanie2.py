"""
Utwórz klasę dla storczyków. Storczyki z zasady mają różne kolory, pory kwitnienia, gatunki.
Utwórz dowolne atrybuty i metody. Dodaj atrybut wspólny dla wszystkich storczyków - królestwo roślin.
"""

class Orchids:
    def __init__(self,species,colour, kingdom):
        self.kingdom =kingdom
        self.species = species
        self.colour = colour

    def substrate(self):
        return "For orchids, only use a material that has a solid structure and is as permeable as possible, " \
                   "such as not too fine pieces of bark. " \
                   "Coconut chips can be mixed in to increase the water storage capacity."
    def light(self):
        return "The best exposure is a southern windowsill, or possibly a western or eastern window, but then the orchids will bloom less profusely. " \
               "These orchids can grow outside but only when it is very warm. They should be protected from direct sunlight during the midday hours"


    def moisture (self):
         return " Water generously during the growing season. During the pseudobulb maturation period, moderate watering is recommended. " \
                "During the winter, keep leaf shedding species dry so that they do not lose their leaves. Rainwater, without lime content, is recommended."



phalaenopsis = Orchids("Phalaenopsis", "White", "Plant kingdom")
print(phalaenopsis.colour)
print(phalaenopsis.light())

