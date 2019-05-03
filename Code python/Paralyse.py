from Statut import *
from random import *

class Paralyse(Statut):
    def __init__(self, nom, combattant, tourRestant):
        Statut.__init__(self,nom,combattant, tourRestant)

    def activerStatut(self, combattant):
        self.setTourRestant(self.getTourRestant()-1)
        n = randint(1,10)
        if (n<4):
            combattant.setTourFini(True)
            print("La paralysie l'empeche d'attaquer...")
        if (self.getTourRestant()==0):
            self.retirerStatut(combattant)
       
    def retirerStatut(self, combattant):
        combattant.retirerStatut(self)
