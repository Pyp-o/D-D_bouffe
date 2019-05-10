from Statut import *

class Ivre(Statut):
    def __init__(self, nom, tourRestant):
        Statut.__init__(self,nom, tourRestant)
        self.__activer=0

    def activerStatut(self, combattant):
        if self.__activer==0:
            combattant.setAgilite(combattant.getAgilite() - 2)
            combattant.setAttaque(combattant.getAttaque() + 2)
            self.__activer = 1

        self.setTourRestant(self.getTourRestant()-1)
        
        if (self.getTourRestant()==0):
            self.retirerStatut(combattant)
        else:
			print(combattant.getNom() + " a envie d'en découdre mais n'a pas l'air de marché très droit...")

    def retirerStatut(self, combattant):
		print(combattant.getNom() + " a retrouvé ses esprits et n'est plus ivre")
        combattant.setAgilite(combattant.getAgilite() + 2)
        combattant.setAttaque(combattant.getAttaque() - 2)
        combattant.retirerStatut(self)
        
