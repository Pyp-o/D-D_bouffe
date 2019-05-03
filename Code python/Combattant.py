from Personnage import *

class Combattant(Personnage):
    def __init__(self, personnage, teamHero):
        Personnage.__init__(self, personnage.getNom(), personnage.getPVmax(), personnage.getPV(), personnage.getPCmax(), personnage.getPC(), personnage.getAgilite(),
                            personnage.getInitiative(), personnage.getAttaque(), personnage.getDefense(), personnage.getStatut(), personnage.getArme(),
                            personnage.getArmure(), personnage.getCompetence())
        self.__perso = personnage
        self.__tourFini = False
        self.__teamHero = teamHero
        self.__statuts = []

    def setTourFini(self, isTourFini):
        self.__tourFini = isTourFini

    def getTourfini(self):
        return self.__tourFini

    def attaquer(self, combattant):
        print("j'attaque "+combattant.getNom()+"!!!")

    def seDefendre(self):
        print("je me defend")

    def isTeamHero(self):
        return self.__teamHero
    
    def ajouterStatut(self, statut):
        self.__statuts.append(statut)

    def retirerStatut(self, statut):
        self.__statut.remove(statut)

    def activerStatut(self):
        for statut in self.__statuts:
            statut.activerStatut(self)