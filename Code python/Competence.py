import sys, termios, tty, os, time
import random
from Combattant import *
from Team import *

class Competence:
    def __init__(self, nom, cout, description, groupe, tauxReussite):
        self.__nom = nom
        self.__cout = cout
        self.__description = description
        self.__groupe = groupe
        self.__tauxResussite = tauxReussite

    def getTauxReussite(self):
        return self.__tauxResussite

    def getNom(self):
        return self.__nom
    
    def getGroupe(self):
        return self.__groupe

    def getDescription(self):
        return self.__description

    def setCout(self, cout):
        self.__cout = cout

    def getCout(self):
        return self.__cout

    def AfficherCompetence(self):
        print("*Nom :", self.getNom(),"  *Description :", self.getCout(), "  *Cout :", self.getCout(), "  *Groupe :", self.getGroupe(), "  *Taux de réussite :", self.getTauxReussite())

    def activerCompetence(self, combattant, teamAllie, teamEnnemi,isAI):    #est ce que une IA attaque?
        raise NotImplementedError

    def getch(self):
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch