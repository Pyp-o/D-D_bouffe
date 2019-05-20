from Salle import *

class SalleEvenement(Salle):
    def __init__(self, isExplore, x, y, salleDroite, salleGauche, salleHaut, salleBas):
        Salle.__init__(self, isExplore, x, y)
        self.setSalleDoite(salleDroite)
        self.setSalleGauche(salleGauche)
        self.setSalleHaut(salleHaut)
        self.setSalleBas(salleBas)
        self.setSalleVide(False)

    def declancherEvenement(self):
        raise NotImplementedError
