from Vehicule import Vehicule


class Automovil(Vehicule):
    def __init__(self, marque, modele, color):
        self.marque = marque
        self.modele = modele
        self.color = color

    def auto_info(self):
        print("This is a car")
        print("Marque: ", self.marque)
        print("Modele: ", self.modele)
        print("Color: ", self.color)