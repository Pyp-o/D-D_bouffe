from Equipement import *

class Arme(Equipement):
    def __init__(self, nom, description, degat):
        Equipement.__init__(self, nom, description)
        self.__degat = degat

    def getDegat(self):
        return self.__degat
