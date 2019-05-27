import time

from SalleEvenement import *

class SalleCuisine(SalleEvenement):
    def __init__(self, isExplore, x, y, salleDroite, salleGauche, salleHaut, salleBas):
        SalleEvenement.__init__(self, isExplore, x, y, salleDroite, salleGauche, salleHaut, salleBas)


    def declancherEvenement(self):
        print("La cuisine!!!")
        time.sleep(1.5)
