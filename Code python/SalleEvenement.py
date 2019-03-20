from Salle import *

class SalleEvenement(Salle):
    def __init__(self, isExplore, x, y):
        Salle.__init__(self, isExplore, x, y)

    def declancherEvenement(self):
        raise NotImplementedError