from Statut import *
from random import *

class Paralyse(Statut):
    def __init__(self, nom, tourRestant):
        Statut.__init__(self,nom, tourRestant)

    def activerStatut(self, combattant):
        self.setTourRestant(self.getTourRestant()-1)
        n = randint(1,10)
        if (self.getTourRestant()==0):
            self.retirerStatut(combattant)
        else:
            if (n<4):
                combattant.setTourFini(True)
                print("La paralysie l'empeche d'attaquer...")
        
       
    def retirerStatut(self, combattant):
		print(combattant.getNom() + " n'est plus paralysé")
        combattant.retirerStatut(self)
