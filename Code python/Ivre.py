from Statut import *

class Ivre(Statut):
    def __init__(self,tourRestant):
        Statut.__init__(self,tourRestant)
        combattant.setAgilite(combattant.getAgilite() - 2)
        combattant.setAttaque(combattant.getAttaque() - 2)

    def activerStatut(self, combattant):
        self.setTourRestant(self.getTourRestant()-1)
        
        if (self.getTourRestant()==0):
            self.retirerStatut(combattant)

    def retirerStatut(self, combattant):
        combattant.setAgilite(combattant.getAgilite() + 2)
        combattant.setAttaque(combattant.getAttaque() + 2)
        combattant.retirerStatut(self)
        
