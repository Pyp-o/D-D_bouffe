import time

from SalleEvenement import *

class SalleBuffet(SalleEvenement):
    def __init__(self, isExplore, x, y, salleDroite, salleGauche, salleHaut, salleBas):
        SalleEvenement.__init__(self, isExplore, x, y, salleDroite, salleGauche, salleHaut, salleBas)
        self.__visite = False


    def declancherEvenement(self):
        print("un buffet!!!")
        time.sleep(1.5)
        if(self.__visite == False):
            print("Apparement c'est encore chaud... A table!")
            self.__visite = True

            return "buffet"
        else:
            print("Tout a été dévoré...")