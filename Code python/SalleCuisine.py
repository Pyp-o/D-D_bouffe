import time

from SalleEvenement import *

class SalleCuisine(SalleEvenement):
    def __init__(self, isExplore, x, y, salleDroite, salleGauche, salleHaut, salleBas):
        SalleEvenement.__init__(self, isExplore, x, y, salleDroite, salleGauche, salleHaut, salleBas)
        self.__visite = False

    def declancherEvenement(self):
        print("La cuisine!!!")
        time.sleep(1)
        if(self.__visite == False):
            print("Il y a plein de truc intéressant à prendre!")
            self.__visite = True

            return "cuisine"
        else:
            print("Mais il y a plus rien à prendre...")


