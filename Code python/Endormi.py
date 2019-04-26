from Statut import *

class Endormi(Statut):
    def __init__(self,tourRestant):
        Statut.__init__(self,tourRestant)

    def activerStatut(self, combattant):
        self.setTourRestant(self.getTourRestant()-1)

	def retirerStatut(self, combattant):
        raise NotImplementedError
