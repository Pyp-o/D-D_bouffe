from Statut import *

class Empoisonne(Statut):
    def __init__(self,tourRestant):
        Statut.__init__(self,tourRestant)

    def activerStatut(self, combattant):
        self.setTourRestant(self.getTourRestant()-1)
        combattant.setPv(combattant.getPv() - int(combattant.getPVmax() * (1/10)))
        if(combattant.getPv() <= 0):
			print("Le poison a finalement eu raison de lui...")
        if (self.getTourRestant()==0):
            self.retirerStatut(combattant)        

    def retirerStatut(self, combattant):
        combattant.retirerStatut(self)

