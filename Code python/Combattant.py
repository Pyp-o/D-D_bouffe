from Personnage import *

class Combattant(Personnage):
    def __init__(self, personnage, teamHero):
        Personnage.__init__(self, personnage.getNom(), personnage.getPVmax(), personnage.getPV(), personnage.getPCmax(), personnage.getPC(), personnage.getAgilite(),
                            personnage.getInitiative(), personnage.getAttaque(), personnage.getDefense(), personnage.getStatut(), personnage.getArme(),
                            personnage.getArmure(), personnage.getCompetence())
        self.__perso = personnage
        self.__tourFini = False
        self.__teamHero = teamHero

    def setTourFini(self, isTourFini):
        self.__tourFini = isTourFini

    def getTourfini(self):
        return self.__tourFini

    def attaquer(self, combattant):
        print("j'attaque "+combattant.getNom()+"!!!")

    def seDefendre(self):
        print("je me défend")

    def isTeamHero(self):
        return self.__teamHero

a = Personnage('crotte',0,0,0,0,0,0,0,0,0,0,0,0)
b = Combattant(a)
b.attaquer(a) #!!! a n'est pas un combattant, c'est juste pour les test!!!!