import time

from SalleEvenement import *

class SallePiege(SalleEvenement):
    def __init__(self,isExplore, x, y, salleDroite, salleGauche, salleHaut, salleBas):
        SalleEvenement.__init__(self, isExplore, x, y, salleDroite, salleGauche, salleHaut, salleBas)

    def declancherEvenement(self):
        print("un piege!!!")
        time.sleep(1.5)