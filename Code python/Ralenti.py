from Statut import *

class Ralenti(Statut):
    def __init__(self,tourRestant):
        Statut.__init__(self,tourRestant)

    def activerStatut(self, combattant):
        self.setTourRestant(self.getTourRestant()-1)

    def retirerStatut(self, combattant):
        raise NotImplementedError

    def retirerStatut(self, combattant):
        combattant.retirerStatut(self)
