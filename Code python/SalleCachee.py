import time

from SalleEvenement import *
from random import *

class SalleCache(SalleEvenement):
    def __init__(self,isExplore, gameMap, x, y, salleDroite, salleGauche, salleHaut, salleBas):
        SalleEvenement.__init__(self, isExplore, x, y, salleDroite, salleGauche, salleHaut, salleBas)
        self.__gameMap = gameMap


    def declancherEvenement(self):
        if (self.__gameMap.getLevierActive()):
            print("une salle caché!!!")
            time.sleep(1.5)
        else:
            i = randint(0,5)
            if i<=1:
                return "bagarre"
