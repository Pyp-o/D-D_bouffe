# -*- coding: utf-8 -*-

from Personnage import *

class Combattant(Personnage):
    def __init__(self, personnage, teamHero, isHero):
        Personnage.__init__(self, personnage.getNom(), personnage.getPVmax(), personnage.getPV(), personnage.getPCmax(), personnage.getPC(), personnage.getAgilite(),
                            personnage.getInitiative(), personnage.getAttaque(), personnage.getDefense(), personnage.getStatut(), personnage.getArme(),
                            personnage.getArmure(), personnage.getCompetences())
        self.__perso = personnage
        self.__tourFini = False
        self.__teamHero = teamHero	#est-t-il dans la team des heros?
        self.__isHero = isHero
        self.__statuts = []
        self.__ordre = -1 #ordre de passage

    def setOrdre(self, ordre):
        self.__ordre = ordre
	
    def getOrdre(self):
        return self.__ordre

    def setTourFini(self, isTourFini):
        self.__tourFini = isTourFini

    def getTourfini(self):
        return self.__tourFini

    def attaquer(self, combattant):
        degat = self.getAttaque()-combattant.getDefense()
        if degat<0:
            degat = 0
        print(combattant.getNom()+" reçoit "+str(degat)+" degat!")
        if combattant.getPV() - degat <= 0:
            combattant.setPV(0)
        else:
            combattant.setPV(combattant.getPV() - degat)

    def seDefendre(self):
        print("je me defend")

    def isTeamHero(self):
        return self.__teamHero
    
    def ajouterStatut(self, statut):
        self.__statuts.append(statut)

    def retirerStatut(self, statut):
        self.__statuts.remove(statut)

    def activerStatut(self):
        for statut in self.__statuts:
            statut.activerStatut(self)
    def setPV(self, PV):	#redefinition
        if PV<=0:
            Personnage.setPV(self, 0)
            print(self.getNom()+" a succombé à ses blessures...")
        else:
            Personnage.setPV(self, PV)
    
    def isHero(self):
        return self.__isHero
