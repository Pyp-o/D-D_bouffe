from Equipement import *

class Armure(Equipement):
    def __init__(self, nom, description, bloquage):
        Equipement.__init__(self, nom, description)
        self.__bloquage = bloquage

    def getBloquage(self):
        return self.__bloquage

    def affichageEquipement(self):
        print('*Nom:', self.getNom(), '  *Description:', self.getDescription(), '  *Protection:', self.getBloquage())