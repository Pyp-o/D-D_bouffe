from Personnage import *

class Ennemi(Personnage):
    def __init__(self, nom, PVmax, PV, PCmax, PC, agilite, initiative, attaque, defense, statut, arme, armure, competence, chanceRejoindre, loot = None, chancesLoot = None):
        Personnage.__init__(self, nom, PVmax, PV, PCmax, PC, agilite, initiative, attaque, defense, statut, arme, armure, competence)
        self.__chanceRejoindre = chanceRejoindre
        self.__rejointHero = False
        self.__loot = loot
        self.__chancesLoot = chancesLoot

    def getChanceRejoindre(self):
        return self.__chanceRejoindre

    def setChanceRejoindre(self, chanceRejoindre):
        self.__chanceRejoindre = chanceRejoindre

    def isRejointHero(self):
        return self.__rejointHero

    def setRejointHero(self, isRejointHero):
        self.__rejointHero = isRejointHero

    def getLoot(self):
        return self.__loot

    def getChancesLoot(self):
        return self.__chancesLoot