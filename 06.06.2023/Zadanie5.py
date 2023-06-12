class Shop:
    def __init__(self, lst):
        self.lst=lst

    def show(self,prod):
        print(f"Proszę o to {prod}, który chciała Pani zobaczyć ")

    def przym(self,prod):
        if prod in self.lst:
            print( f"Możesz przyymierzyć {prod}")
        else:
           print( f"Przepraszamy ale obecnie nie posaiadamy {prod}")

    def bay(self, prd):
       return self.lst.remove(prd)

    def return_pro(self, prod):
        self.lst.append(prod)
        print(f"zwrócono do sklepu {prod}")

    def show_all_prod(self):
        print(self.lst)

kolejka=Shop(["spodnie","sukienka", "bluzka", "torebka", "okulary"])
kolejka.show("Okulary")
kolejka.bay("spodnie")
kolejka.return_pro("bluzka")
kolejka.przym("szpilek")
kolejka.show_all_prod()