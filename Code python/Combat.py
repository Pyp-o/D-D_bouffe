# -*- coding: utf-8 -*-

import sys, termios, tty, os, time
from Team import *
from Combattant import *
from Ennemi import *
from Hero import *
from random import *
from CompetenceAttaque import *
from CompetenceHeal import *
from CompetenceStatut import *
from CompetenceBuff import *
from Empoisonne import *
import time

class Combat():
    def __init__(self, teamHero, teamEnnemi):
        self.__teamHero = teamHero  #objet Team
        self.__teamEnnemi = teamEnnemi  #objet Team
        self.__teamCombattantsEnnemi = []   #list de Combattants
        self.__teamCombattantsHero = [] #list de Combattants
        self.__creationCombattant()
        self.__definitionOrdrePassage()
        self.__teamHeroMorte = False
        self.__teamEnnemieMorte = False
        self.__fuiteReussi = False
        self.__tour = 1

    def lancerCombat(self): #la methode principale qui gere le combat
        print("Vous venez de vous faire agresser par : ")
        for ennemi in self.__teamCombattantsEnnemi:
            print(ennemi.getNom() + " a " + str(ennemi.getPV()) + "/" + str(ennemi.getPVmax()) + "PV")
        time.sleep(1.5)
        print("******* Tour 1 *******")
        while (self.__teamHeroMorte == False) and (self.__teamEnnemieMorte == False) and (self.__fuiteReussi == False): #tant que l'une des 2 team n'est pas entierement morte
            if self.__isFinDeTour() == True:
                self.__tour = self.__tour+1
                print("******* Tour "+str(self.__tour)+" *******")
                self.__resetTour()  #Application des statuts
            nextCombattant = self.__getProchainCombattant()
            self.__tourCombattant(nextCombattant)
            self.__testTeamMorte()
            print("")
        if self.__fuiteReussi == False:
            if self.__teamEnnemieMorte == True:
                print("Les ennemies ont été vaincu!!!")
                self.__finCombat()
                time.sleep(1)
            else:
                print("Les heros ont été vaincu...")
                print("Game Over")
                exit(0)
    
    def __tourCombattant(self, combattant): #le tour d'un des combattants
        if combattant.isHero():
            print("C'est à "+combattant.getNom()+" d'agir!")
            self.__choixJoueur(combattant)
            time.sleep(1.5)
        else:
            if combattant.isTeamHero():
                print("L'allié "+combattant.getNom()+ " attaque l'ennemie!")
            else:
                print("L'ennemie "+combattant.getNom()+ " attaque!")
            self.__choixDeLIA(combattant)
            time.sleep(1.5)
        combattant.setTourFini(True)
    
    def __choixJoueur(self, combattant):
        i=0
        choixPossible = ["attaquer", "defendre", "utiliser competence", "fuir", "info"]
        maxRange = len(choixPossible)

        ok = False #variable pour savoir si l'utilisateur a juste demandé les infos
        while ok==False:
            print("Que faire? (utiliser z et s pour choisir et entrée pour selectionner)")
            ok = True
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
            if(i==1):    #le hero se defend
                print(combattant.getNom()+" se defend")     #TODO faire le defense
            if(i==2):
                ok = self.__heroUtiliserCompetence(combattant)
            if(i==3):
                self.__fuir(combattant)
            if(i==4):
                for hero in self.__teamCombattantsHero:
                    if hero.getPV()==0:
                        print(hero.getNom()+" est décédé...")
                    else: 
                        print(hero.getNom()+" a "+str(hero.getPV())+"/"+str(hero.getPVmax())+"PV, "+str(hero.getPC())+"/"+str(hero.getPCmax())+"PC, "+str(hero.getAttaque())+" attaque, "+str(hero.getDefense())+" defense, "+str(hero.getAgilite())+" agilité, ",end='')
                        if hero.getTourfini():
                            print("son tour est fini")
                        else:
                            print("il n'a pas encore fini son tour")
                print()
                for ennemi in self.__teamCombattantsEnnemi:
                    if ennemi.getTourfini():
                        print(ennemi.getNom()+" a "+str(ennemi.getPV())+"/"+str(ennemi.getPVmax())+"PV, son tour est fini")
                    else:
                        print(ennemi.getNom()+" a "+str(ennemi.getPV())+"/"+str(ennemi.getPVmax())+"PV, il n'a pas encore fini son tour")
                ok = False
                print()
                
            
    def __fuir(self, combattant):
        r = randint(1,10)
        if(r<=4):
            print("Fuite réussi!")
            self.__fuiteReussi = True
        else:
            print("Les héros essaient de fuir mais les ennemies les rattrapent...")

    def getFuiteReussi(self):
        return self.__fuiteReussi

    def __heroUtiliserCompetence(self, combattant):
        if (combattant.getCompetences() == 0):
            print("Mais le héro n'a pas de competence...")
        else:
            print("Quelle competence?")
            i = 0

            maxRange = len(combattant.getCompetences())
            rep = ""


            while rep != "0xd": #différent de entrée
                print(combattant.getCompetences()[i].getNom())
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
            if combattant.getPC()<combattant.getCompetences()[i].getCout():
                print("Pas assez de PC disponible...")
                return False
            combattant.getCompetences()[i].activerCompetence(combattant, self.__teamCombattantsHero, self.__teamCombattantsEnnemi, False)
            combattant.setPC(combattant.getPC() - combattant.getCompetences()[i].getCout())
            return True


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
        if combattant.isTeamHero():
            teamACombattre = self.__teamCombattantsEnnemi
            saTeam = self.__teamCombattantsHero
        else:
            teamACombattre = self.__teamCombattantsHero
            saTeam = self.__teamCombattantsEnnemi
        for ennemi in teamACombattre:
            if ennemi.getPV()==0:
                teamACombattre.remove(ennemi)
        isAttaque = True
        if(combattant.getCompetences()!=None):
            i = randint(0,1)    #si l'IA a une competence, elle a une chance sur deux de l'utiliser
            if(i):
                isAttaque = False
        if(isAttaque):
            i = randint(0,len(teamACombattre)-1)
            combattant.attaquer(teamACombattre[i])
        else:
            print(combattant.getNom()+" : "+combattant.getCompetences()[0].getDescription())
            combattant.getCompetences()[0].activerCompetence(combattant, saTeam, teamACombattre, True)
    
    def __resetTour(self):
        for combattant in self.__teamCombattantsHero:
            combattant.setTourFini(False)
            combattant.activerStatut()
        for combattant in self.__teamCombattantsEnnemi:
            combattant.setTourFini(False)
            combattant.activerStatut()
    
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
            if (isinstance(personnage,Hero)):
                self.__teamCombattantsHero.append(Combattant(personnage, True,True))
            else:
                self.__teamCombattantsHero.append(Combattant(personnage, True,False))                
        for personnage in self.__teamEnnemi.getPersonnages():
            self.__teamCombattantsEnnemi.append(Combattant(personnage, False, False))

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
                if ((combattant.getOrdre() < ordrePrio) and (combattant.getTourfini() == False) and (combattant.getPV()!=0)):
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
            if combattant.getPV() != 0:
                test = False
            else:
                if combattant.isHero()==False:
                    self.__teamCombattantsHero.remove(combattant)
        if test:
            self.__teamHeroMorte = True
        test = True
        for combattant in self.__teamCombattantsEnnemi:
            if combattant.getPV() != 0:
                test = False
            else:
                self.__teamCombattantsEnnemi.remove(combattant) #les ennemies mort ne restent pas dans les team
        if test:
            self.__teamEnnemieMorte = True
    
    def __finCombat(self):
        for combattant in self.__teamCombattantsHero:
            combattant.getPersonnage().setPV(combattant.getPV())
            combattant.getPersonnage().setPC(combattant.getPC())
        for persoEnnemie in self.__teamEnnemi.getPersonnages():
            i = randint(0,100)
            if(i<persoEnnemie.getChanceRejoindre()):
                print(persoEnnemie.getNom()+" a décidé de rejoindre votre équipe!")
                if(self.__teamHero.getLenPersonnage()<=8):
                    print("Accepter "+persoEnnemie.getNom()+"? (o : oui, n : non)")
                    rep = ""
                    while rep not in ["o", "n"]:  #o,n
                        rep = self.getch()
                    if rep == "o":
                        self.__teamHero.ajouterPersonnage(persoEnnemie)
                        persoEnnemie
                        print(persoEnnemie.getNom()+" a rejoint votre équipe!")
                    else:
                        print(persoEnnemie.getNom()+" s'en va tristement...")
                else:
                    print("Mais l'équipe est déjà au complet...")
                time.sleep(1)
        
    
    def getch(self):
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch

