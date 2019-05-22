from SalleEvenement import *

class SalleGardeManger(SalleEvenement):
    def __init__(self, isExplore, x, y, salleDroite, salleGauche, salleHaut, salleBas):
        SalleEvenement.__init__(self, isExplore, x, y, salleDroite, salleGauche, salleHaut, salleBas)

    def declancherEvenement(self):
        print("un garde manger :)")
