from Hero import *
from Inventaire import *

class Team:
    def __init__(self):
        self.__personnages = []
        self.__inventaire = Inventaire()

    def ajouterPersonnage(self, personnage):
        self.__personnages.append(personnage)

    def enelverPersonnage(self, personnage):
        self.__personnages.remove(personnage)

    def getPersonnages(self):
        return self.__personnages
    
    def getPersonnage(self, i):
		return self.__personnages[i]
        
    def getLenPersonnage(self):
		return len(self.__personnages)


###########test#################
