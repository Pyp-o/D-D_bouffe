from Personnage import *

class Ennemi(Personnage):
    def __init__(self, nom, PVmax, PV, PCmax, PC, agilite, initiative, attaque, defense, statut, arme, armure, competence, chanceRejoindre):
        Personnage.__init__(self, nom, PVmax, PV, PCmax, PC, agilite, initiative, attaque, defense, statut, arme, armure, competence)
        self.__chanceRejoindre = chanceRejoindre

    def getChanceRejoindre(self):
        return self.__chanceRejoindre

    def setChanceRejoindre(self, chanceRejoindre):
        self.__chanceRejoindre = chanceRejoindre
