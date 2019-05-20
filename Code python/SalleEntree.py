from SalleEvenement import *

class SalleEntree(SalleEvenement):
    def __init__(self, isExplore, x, y, salleDroite, salleGauche, salleHaut, salleBas):
        SalleEvenement.__init__(self, isExplore, x, y, salleDroite, salleGauche, salleHaut, salleBas)

    def declancherEvenement(self):
        print("c'est de là que l'on est venu...")
