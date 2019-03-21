from Team import *
from Combattant import *

#CLASSE A FINIR

class Combat():
    def __init__(self, teamHero, teamEnnemi):
        self.__teamHero = teamHero
        self.__teamEnnemi = teamEnnemi
        self.__combattants = []
        self.__creationCombattant()


    def __creationCombattant(self):
        for personnage in self.__teamHero:
            self.__combattants.append(Combattant(personnage, True))
        for personnage in self.__teamEnnemi:
            self.__combattants.append(Combattant(personnage, False))
