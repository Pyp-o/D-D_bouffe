import time

from SalleEvenement import *

class SalleBuffet(SalleEvenement):
    def __init__(self, isExplore, x, y, salleDroite, salleGauche, salleHaut, salleBas):
        SalleEvenement.__init__(self, isExplore, x, y, salleDroite, salleGauche, salleHaut, salleBas)

    def declancherEvenement(self):
        print("un buffer :p")
        time.sleep(1.5)
