from Personnage import *
from Inventaire import *

class Team:
    def __init__(self, personnages):
        self.__personnages = []
        self.__personnages.append(personnages)
        self.__inventaire = Inventaire()

    def ajouterPersonnage(self, personnage):
        self.__personnages.append(personnage)

    def enelverPersonnage(self, personnage):
        self.__personnages.remove(personnage)

    def getPersonnages(self):
        return self.__personnages


###########test#################
a = Personnage('crotte',0,0,0,0,0,0,0,0,0,0,0,0)
t = Team(a)
t.enelverPersonnage(a)
for p in t.getPersonnages():
    print(":"+p.getNom())
t.ajouterPersonnage(a)
for p in t.getPersonnages():
    print(":"+p.getNom())