import time

from SalleEvenement import *

class SalleGardeManger(SalleEvenement):
    def __init__(self, isExplore, x, y, salleDroite, salleGauche, salleHaut, salleBas):
        SalleEvenement.__init__(self, isExplore, x, y, salleDroite, salleGauche, salleHaut, salleBas)
        self.__visite = False

    def declancherEvenement(self):
        print("Un garde manger :)")
        time.sleep(1)
        if(self.__visite == False):
            print("Il y a un truc sympa à prendre!")
            self.__visite = True

            return "garde manger"
        else:
            print("Mais c'est vide...")