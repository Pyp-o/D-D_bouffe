from Statut import *

class Endormi(Statut):
    def __init__(self, nom, tourRestant):
        Statut.__init__(self,nom, tourRestant)

    def activerStatut(self, combattant):
		print(combattant.getNom()+ " est entierement endormi et ne pourra pas jouer ce tour...")
        self.setTourRestant(self.getTourRestant()-1)
        if (self.getTourRestant()==0):
            self.retirerStatut(combattant)
        else:
            combattant.setTourFini(True)

            
    def retirerStatut(self, combattant):
        print(combattant.getNom()+" se réveille")
        combattant.retirerStatut(self)
