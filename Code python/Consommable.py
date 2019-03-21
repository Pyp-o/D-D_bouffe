from Item import *
from Personnage import *

class Consommable(Item):
    def __init__(self, nom, description, soin, energie, statutRetire, faitRevivre):
        Item.__init__(self, nom, description)
        self.__soin = soin
        self.__energie = energie
        self.__statutRetire = statutRetire
        self.__faitRevivre = faitRevivre

    def getSoin(self):
        return self.__soin

    def getEnergie(self):
        return self.__energie

    def getStatutretire(self):
        return self.__statutRetire

    def getFaitRevivre(self):
        return self.__faitRevivre

    def utiliser(self, personnage):
        print(personnage.getNom() + " : une bonne potion!")