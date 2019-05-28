from Arme import *
from Consommable import *

class ArmeConsommable(Arme, Consommable):
    def __init__(self,nom, description, PV, degat):
        Arme.__init__(self,nom, description,degat)
        Consommable.__init__(self,nom, description, PV, PC=0,PVmax=0, PCmax=0, attaque=0, defense=0, agilite=0, initiative=0, faitRevivre=False)
