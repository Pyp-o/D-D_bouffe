from Personnage import *

class Hero(Personnage):
    def __init__(self, nom, PVmax, PV, PCmax, PC, agilite, initiative, attaque, defense, statut, arme, armure, competence):
        Personnage.__init__(self, nom, PVmax, PV, PCmax, PC, agilite, initiative, attaque, defense, statut, arme, armure, competence)