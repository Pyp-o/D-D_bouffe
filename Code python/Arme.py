from Equipement import *
from Item import *
from Personnage import *

class Arme(Equipement):
    def __init__(self, nom, description, degat):
        Equipement.__init__(self, nom, description)
        self.__degat = degat

    def getDegat(self):
        return self.__degat

    def affichageEquipement(self):
        print('*Nom:', self.getNom(), '  *Description:', self.getDescription(), '  *Degats:', self.getDegat())
