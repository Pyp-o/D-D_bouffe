from Item import *

class Equipement(Item):
    def __init__(self, nom, description):
        Item.__init__(self, nom, description)
        self.__porteur=None

    def getPorteur(self):
        return self.__porteur

    def retirerPorteur(self):
        self.__porteur = None

    def setPorteur(self, porteur):
        self.__porteur = porteur