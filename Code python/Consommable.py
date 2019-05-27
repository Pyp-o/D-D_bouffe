# -*- coding: utf-8 -*-


from Item import *
from Personnage import *

class Consommable(Item):
    def __init__(self, nom, description, PV, PC,PVmax, PCmax, attaque, defense, agilite, initiative, faitRevivre):
        Item.__init__(self, nom, description)
        self.__soin = PV
        self.__energie = PC
        self.__PVmax = PVmax
        self.__PCmax = PCmax
        self.__attaque = attaque
        self.__defense = defense
        self.__agilité = agilite
        self.__initiative = initiative
        self.__faitRevivre = faitRevivre

    def getSoin(self):
        return self.__soin

    def getEnergie(self):
        return self.__energie

    def getPVmax(self):
        return self.__PVmax

    def getPCmax(self):
        return self.__PCmax

    def getAttaque(self):
        return self.__attaque

    def getDefense(self):
        return self.__defense

    def getAgilite(self):
        return self.__agilité

    def getInitiative(self):
        return self.__initiative

    def getFaitRevivre(self):
        return self.__faitRevivre

    def utiliser(self, personnage):
        print(personnage.getNom() + " : une bonne potion!")

    def affichageConsommable(self):
        if(self.getFaitRevivre()!=0):
            revive="Oui"
        else:
            revive="Non"
        print("*Nom:", self.getNom(), "  *Description:", self.getDescription(), "  *Soin:", self.getSoin(), "  *Energie:", self.getEnergie(), "*Pvmax :",self.getPVmax(), "*PCmax :", self.getPCmax(), "*Attaque :", self.getAttaque(),"*Defense :", self.getDefense(),"*Agilite :", self.getAgilite(),"*Initiative :", self.getInitiative(), "  *Peut réscussiter:", revive)