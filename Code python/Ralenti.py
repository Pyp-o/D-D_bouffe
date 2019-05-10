from Statut import *

class Ralenti(Statut):
    def __init__(self, nom, combattant, tourRestant):
        Statut.__init__(self,nom,combattant, tourRestant)
        self.__activer=0

    def activerStatut(self, combattant):
        if self.__activer==0:
            combattant.setAgilite(combattant.getAgilite() - 3)
            self.__activer = 1
            
        self.setTourRestant(self.getTourRestant()-1)
        
        if (self.getTourRestant()==0):
            self.retirerStatut(combattant)        
        else:
			print("Les gestes de "+combattant.getNom()+" sont au ralentit...")

    def retirerStatut(self, combattant):
		print(combattant.getNom() + "n'est plus ralentit dans ses mouvements")
        combattant.setAgilite(combattant.getAgilite() + 3)
        combattant.retirerStatut(self)
