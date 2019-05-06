from Statut import *

class Ivre(Statut):
    def __init__(self, nom, combattant, tourRestant):
        Statut.__init__(self,nom,combattant, tourRestant)
        self.__combattant.setAgilite(combattant.getAgilite() - 2)
        self.__combattant.setAttaque(combattant.getAttaque() + 2)

    def activerStatut(self, combattant):

        self.setTourRestant(self.getTourRestant()-1)
        
        if (self.getTourRestant()==0):
            self.retirerStatut(combattant)
        else:
			print(combattant.getNom() + " a envie d'en découdre mais n'a pas l'air de marché très droit...")

    def retirerStatut(self, combattant):
        combattant.setAgilite(combattant.getAgilite() + 2)
        combattant.setAttaque(combattant.getAttaque() - 2)
        combattant.retirerStatut(self)
        
