from Statut import *

class Ralenti(Statut):
    def __init__(self,tourRestant):
        Statut.__init__(self,tourRestant)

    def activerStatut(self):
        self.setTourRestant(self.getTourRestant()-1)
