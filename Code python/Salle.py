from random import *


class Salle:
    def __init__(self, isExplore, x, y):
        self.__isExplore = isExplore
        self.__x = x
        self.__y = y
        self.__salleDroite = None
        self.__salleGauche = None
        self.__salleHaut = None
        self.__salleBas = None
        self.__salleVide = True

    def getX(self):
        return self.__x

    def getY(self):
        return self.__y

    def isExplore(self):
        return self.__isExplore

    def setExplore(self, isExplore):
        self.__isExplore = isExplore

    def setSalleDoite(self, salle):
        self.__salleDroite = salle

    def setSalleGauche(self, salle):
        self.__salleGauche = salle

    def setSalleBas(self, salle):
        self.__salleBas = salle

    def setSalleHaut(self, salle):
        self.__salleHaut = salle

    def getSalleGauche(self):
        return self.__salleGauche

    def getSalleDroite(self):
        return self.__salleDroite

    def getSalleBas(self):
        return self.__salleBas

    def getSalleHaut(self):
        return self.__salleHaut
    
    def getSalleVide(self):
        return self.__salleVide
	
    def setSalleVide(self, salleVide):
        self.__salleVide = salleVide
    
    def declancherEvenement(self):
        i = randint(0,7)
        if i<=1:
            return "bagarre"
