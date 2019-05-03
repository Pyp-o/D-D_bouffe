from Statut import *

class Endormi(Statut):
    def __init__(self, nom, combattant, tourRestant):
        Statut.__init__(self,nom,combattant, tourRestant)

    def activerStatut(self, combattant):
        self.setTourRestant(self.getTourRestant()-1)
        combattant.setTourFini(True)
        if (self.getTourRestant()==0):
            self.retirerStatut(combattant)
            
    def retirerStatut(self, combattant):
        combattant.retirerStatut(self)
