import time

from SalleEvenement import *

class SallePiege(SalleEvenement):
    def __init__(self,isExplore, x, y, salleDroite, salleGauche, salleHaut, salleBas):
        SalleEvenement.__init__(self, isExplore, x, y, salleDroite, salleGauche, salleHaut, salleBas)
        self.__visite = False

    def declancherEvenement(self):
        if(self.__visite):
            print("Il y a des restes d'un piège assez fourbe...")
        else:
            print("un piege!!!")
            time.sleep(1.5)
            return "piege"