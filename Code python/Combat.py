# -*- coding: utf-8 -*-

import sys, termios, tty, os, time
from Team import *
from Combattant import *
from Ennemi import *
from Hero import *

#CLASSE A FINIR

class Combat():
    def __init__(self, teamHero, teamEnnemi):
        self.__teamHero = teamHero  #objet Team
        self.__teamEnnemi = teamEnnemi  #objet Team
        self.__teamCombattantsEnnemi = []   #list de Combattants
        self.__teamCombattantsHero = [] #list de Combattants
        self.__creationCombattant()
        self.__definitionOrdrePassage()
        self.__teamAllieMorte = False
        self.__teamEnnemieMorte = False

    def lancerCombat(self): #la methode principale qui gere le combat
        while self.__teamAllieMorte == False and self.__teamAllieMorte == False: #tant que l'une des 2 team n'est pas entierement morte
            if self.__isFinDeTour() == True:
                self.__resetTour()  #Application des statuts
            nextCombattant = self.__getProchainCombattant()
            self.__tourCombattant(nextCombattant)
            self.__testTeamMorte()
        if self.__teamAllieMorte == True:
            print("Les ennemies ont été vaincu!!!")
        else:
            print("Les heros ont été vaincu...")
            print("Game Over")
            exit(0)
    
    def __tourCombattant(self, combattant): #le tour d'un des combattants
        if combattant.isTeamHero():
            print("C'est à "+combattant.getNom()+" d'agir!")
            self.__choixJoueur(combattant)
        else:
            print("L'ennemie "+combattant.getNom()+ " attaque!")
            self.__choixDeLIA(combattant)
        combattant.setTourFini(True)
    
    def __choixJoueur(self, combattant):
        print("Que faire? (utiliser z et s pour choisir et entrée pour selectionner)")
        i=0
        choixPossible = ["attaquer", "defendre", "utiliser competence", "fuir"]
        maxRange = len(choixPossible)
        rep = ""
        while rep != "0xd": #différent de entrée
            print(choixPossible[i])
            rep = hex(ord(self.getch()))    #on récupère la touche tapé par l'utilisateur (pas besoin de faire entrée)
            if(rep == "0x7a"):    #z
                if(i<maxRange-1):
                    i = i+1
                else :
                    i=0
            if(rep == "0x73"):    #s
                if(i>0):
                    i = i-1
                else:
                    i = maxRange - 1
        if (i==0):  #le hero attaque
            self.__heroAttaque(combattant)
        
            
    def __heroAttaque(self, combattant):
        print("Qui attaquer?")
        i=0
        maxRange = len(self.__teamCombattantsEnnemi)
        rep = ""
        while rep != "0xd": #différent de entrée
            print(self.__teamCombattantsEnnemi[i].getNom())
            rep = hex(ord(self.getch()))    #on récupère la touche tapé par l'utilisateur (pas besoin de faire entrée)
            if(rep == "0x7a"):    #z
                if(i<maxRange-1):
                    i = i+1
                else :
                    i=0
            if(rep == "0x73"):    #s
                if(i>0):
                    i = i-1
                else:
                    i = maxRange - 1
        combattant.attaquer(self.__teamCombattantsEnnemi[i])
        if self.__teamCombattantsEnnemi[i].getPV() == 0:
            self.__teamCombattantsEnnemi.remove(self.__teamCombattantsEnnemi[i])

            
    def __choixDeLIA(self, combattant):
        combattant.attaquer(self.__teamCombattantsHero[0])
    
    def __resetTour(self):
        for combattant in self.__teamCombattantsHero:
            combattant.activerStatut()
            combattant.setTourFini(False)
        for combattant in self.__teamCombattantsEnnemi:
            combattant.activerStatut()
            combattant.setTourFini(False)
    
    def __isFinDeTour(self):
        finDeTour = True    #on part du principe que c'est la fin du tour et on va essayer de prouver le contraire
        for combattant in self.__teamCombattantsHero:
            if combattant.getTourfini() == False:
                finDeTour = False
        for combattant in self.__teamCombattantsEnnemi:     #et également pour les ennemies
            if combattant.getTourfini() == False:
                finDeTour = False
        return finDeTour
                    
    def __creationCombattant(self):
        for personnage in self.__teamHero.getPersonnages():
            self.__teamCombattantsHero.append(Combattant(personnage, True))
        for personnage in self.__teamEnnemi.getPersonnages():
            self.__teamCombattantsEnnemi.append(Combattant(personnage, False))

    def __definitionOrdrePassage(self):
        i = 1 #nb combattant avec un ordre assigné
        n = len(self.__teamCombattantsEnnemi) + len(self.__teamCombattantsHero) #nombre de combattant a assigné
        combattantSelectionne = self.__teamCombattantsEnnemi[0]     #on assigne un combattant au hasard 
        while i!=n+1:
            initMax = -1 #on va chercher qui a la plus grande initiative parmis les combattant qui n'ont pas encore eu un ordre assigné
            
            for combattant in self.__teamCombattantsHero:
                #print(combattant.getOrdre())
                if ((combattant.getOrdre() == -1) and (combattant.getInitiative() > initMax)):
                    combattantSelectionne = combattant
                    initMax = combattant.getInitiative()
            for combattant in self.__teamCombattantsEnnemi:     #et également pour les ennemies
                if ((combattant.getOrdre() == -1) and (combattant.getInitiative() > initMax)):
                    initMax = combattant.getInitiative()
                    combattantSelectionne = combattant
            
            combattantSelectionne.setOrdre(i)   #on attribut un ordre de passage à ce combattant
            i = i+1
    
    def __getProchainCombattant(self):  #le prochain combattant 
        nextCombattant = self.__teamCombattantsEnnemi[0]
        ordrePrio = 999
        for combattant in self.__teamCombattantsHero:
                if ((combattant.getOrdre() < ordrePrio) and (combattant.getTourfini() == False)):
                    nextCombattant = combattant
                    ordrePrio = combattant.getOrdre()
        for combattant in self.__teamCombattantsEnnemi:
                if ((combattant.getOrdre() < ordrePrio) and (combattant.getTourfini() == False)):
                    nextCombattant = combattant
                    ordrePrio = combattant.getOrdre()
        return nextCombattant
    
    def __testTeamMorte(self):
        test = True
        for combattant in self.__teamCombattantsHero:
            if combattant.getPV()==0:
                test = False
        if test == True:
            self.__teamHeroMorte = True
        test = True
        for combattant in self.__teamCombattantsEnnemi:
            if combattant.getPV()==0:
                test = False
        if test == True:
            self.__teamEnnemieMorte = True
            
    
    def getch(self):
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch
        
hero1 = Hero('hero1',50,30,0,0,0,12,10,0,0,0,0,0)   #nom,  PVmax, PV, PCmax, PC, Agi, Init, Attaque, Def, Statut, Arme, Armure, Competence
hero2 = Hero('hero2',50,30,0,0,0,15,7,0,0,0,0,0)
hero3 = Hero('hero3',40,20,0,0,0,5,8,5,0,0,0,0)

enne1 = Ennemi('enne1',50,30,0,0,0,3,8,0,0,0,0,0,10)
enne2 = Ennemi('enne2',50,30,0,0,0,11,4,0,0,0,0,0,10)
enne3 = Ennemi('enne3',40,0,0,0,0,13,3,0,0,0,0,0,10)


tAlli = Team()
tEnn = Team()
tAlli.ajouterPersonnage(hero1)
tAlli.ajouterPersonnage(hero2)
tAlli.ajouterPersonnage(hero3)
tEnn.ajouterPersonnage(enne1)
tEnn.ajouterPersonnage(enne2)
tEnn.ajouterPersonnage(enne3)

c = Combat(tAlli, tEnn)
c.lancerCombat()
