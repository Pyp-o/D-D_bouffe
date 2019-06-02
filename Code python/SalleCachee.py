import time

from SalleEvenement import *
from random import *

class SalleCache(SalleEvenement):
    def __init__(self,isExplore, gameMap, x, y, salleDroite, salleGauche, salleHaut, salleBas):
        SalleEvenement.__init__(self, isExplore, x, y, salleDroite, salleGauche, salleHaut, salleBas)
        self.__gameMap = gameMap
        self.__visite = False


    def declancherEvenement(self):
        if (self.__gameMap.getLevierActive()):
            print("une salle caché!!!")
            if(self.__visite):
                print("Mais il n'y a plus rien...")
            else:
                print("Il y a plein de trésors!!!")
                self.__visite = True
                time.sleep(1.5)
                return "salle cache"
            time.sleep(1.5)

        else:
            i = randint(0,7)
            if i<=1:
                return "bagarre"
