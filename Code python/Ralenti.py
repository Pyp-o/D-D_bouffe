from Statut import *

class Ralenti(Statut):
    def __init__(self, nom, combattant, tourRestant):
        Statut.__init__(self,nom,combattant, tourRestant)
        self.__combattant.setAgilite(combattant.getAgilite() - 3)

    def activerStatut(self, combattant):
        self.setTourRestant(self.getTourRestant()-1)
        
        if (self.getTourRestant()==0):
            self.retirerStatut(combattant)        

    def retirerStatut(self, combattant):
        combattant.setAgilite(combattant.getAgilite() + 3)
        combattant.retirerStatut(self)
