# -*- coding: utf-8 -*-

from random import *
from Hero import *
from Arme import *
from Map import *
from Personnage import *
from Competence import *
from CompetenceAttaque import *
from CompetenceHeal import *
from CompetenceStatut import *
from CompetenceBuff import *
from Ennemi import *
from Team import *
from Combat import *
import copy

from Lore import *

class Moteur :
    def __init__(self):
        self.__teamHero=Team()
        self.initTeam()
        self.__map = Map()
        self.__etage = 1
        self.__tailleMapX = 5
        self.__tailleMapY = 5
        self.__map.genererMap(self.__tailleMapX, self.__tailleMapY)
        self.end = 0
        self.bossTue = False #le boss de l'étage est mort?
        while(self.end != 1):
            self.end = self.tour()

    def getTeamHero(self):
        return self.__teamHero

    def nouvelleEtage(self):
        self.__etage = self.__etage +1
        self.__tailleMapX = self.__tailleMapX + 2
        self.__tailleMapY = self.__tailleMapY + 2
        self.__map.genererMap(self.__tailleMapX, self.__tailleMapY)


    def initTeam(self):
        print("---- HEROS ----\n")
        print("1- Charcutier :\t")
        print("Question barbaque il s'y connait, et son embon point montre qu'il teste ses produits. \n\tIl manie avec aisance les armes assez lourdes comme les hachoirs ou les jambons secs entiers\n\n")
        time.sleep(2)

        print("2- Pillier de Bar :\t")
        print("C'est le bon copain du village. Il a une résistance à l'alcool impressionnante !! \n\tEt puis, à force de faire la baguarre dans le bar, il résiste plutôt bien aux coups\n\n")
        time.sleep(2)

        print("3- Crève-dalle :\t")
        print("Maigre comme un clou, il n'a jamais pu manger à sa faim. Il a donc développé des techniques imparables pour pouvoir manger. \n\tHabitué à voler, il utilise des dagues et se débrouille très bien pour repérer les dangers et les trésors.\n")
        time.sleep(2)

        print("4- Cuistot :\t")
        print("Gros comme un cochon, il transforme n'importe quel ingrédient en plat digne d'un roi. \n\tIl parait même que ses plats apportent des pouvoirsmagiques à ceux qui les consomment.\n\n")
        time.sleep(2)

        print("5- Poivrot :\t")
        print("Toujours aussi saoul que le pillier de bar, il est pas vraiment copain avec tout le monde... \n\tMais il lance des trucs avec assez de précision pour blesser des gens à chaque coup, ça pourrait être utilse.\n\n")
        time.sleep(2)
        a = randint(0,2)
        choixPrecedent='12'
        for i in range(1, 3):
            print("Choisir le personnage ", i)
            a = self.selectPerso()
            while(a not in [1,2,3,4,5] or a == choixPrecedent):
                if(a==choixPrecedent) :
                    print("Ce personnage a déjà rejoint votre équipe\n")
                else :
                    print("Le personnage choisi n'existe pas\n")
                print("Choisir un autre personnage : \n")
                a = self.selectPerso()

            t = self.getTeamHero().getInventaire()
            if (a == 1 and a != choixPrecedent):
                self.__teamHero.ajouterPersonnage(Charcutier)
            elif (a == 2 and a!=choixPrecedent):
                self.__teamHero.ajouterPersonnage(Pilier)
            elif (a == 3 and a!=choixPrecedent):
                self.__teamHero.ajouterPersonnage(Creve)
            elif (a == 4 and a!=choixPrecedent):
                self.__teamHero.ajouterPersonnage(Cuistot)
            elif (a == 5 and a!=choixPrecedent):
                self.__teamHero.ajouterPersonnage(Poivrot)
            elif (a == choixPrecedent):
                print("Ce personnage a déjà rejoins votre équipe\n")

            choixPrecedent = a
        print("\n\n\n")

    def tour(self):
        ok = False
        while(ok != True):
            print("Que voulez-vous faire ? \nse déplacer (z,q,s,d), gestion d'inventaire (i), statistiques (e), quitter (t)\n")
            self.__map.display_maze()
            rep=self.getch()
            if(rep in ['z', 'q', 's', 'd']):
                ok = self.__map.seDeplacer(rep)
                if ok :
                    event = self.__map.declancherEvent()
                    self.gererEvent(event)
            elif (rep=='i'):
                print("choisir un perso à gérer\n")
                perso=self.getTeamHero().getPersonnages()
                self.__teamHero.getInventaire().choixAction(perso)
                self.__map.display_maze()
            elif (rep=='e'):
                for personnage in self.__teamHero.getPersonnages():
                    personnage.AfficherStat()
            elif(rep=='t'):
                ok=True
                return True
        return 0

    def gererEvent(self, event):
        if event == "sortie":
            if (self.bossTue == False):
                self.combatDeBoss()
            print("Voulez-vous continuer? (o : oui, n : non)")
            rep = ""
            while rep not in ["o", "n"]:  #o,n
                rep = self.getch()
            if rep == "o":
                self.nouvelleEtage()
        if event == "bagarre":
            teamEnnemi = Team()
            i = randint(1,3)
            for x in range(0,i):
                teamEnnemi.ajouterPersonnage(self.getEnnemi())
            combat = Combat(self.__teamHero, teamEnnemi)
            combat.lancerCombat()
        if event == "salle cache":
            self.loot("legendaire")
        if event == "cache":
            self.loot("ressource")
        if event == "garde manger":
            self.loot("normal")
        if("piege"):
            i= randint(0,1)
            if(i):
                print("Tous les heros perdent 5PV!!!")
                for hero in self.__teamHero.getPersonnages():
                    hero.setPV(hero.getPV()-5)
                    if(hero.getPV<=0):
                        print(hero.getNom()+ " a succombé...")
            else:
                print("Des ennemies vous tombent dessus!!!")
                for x in range(0, 3):
                    teamEnnemi.ajouterPersonnage(self.getEnnemi())
                combat = Combat(self.__teamHero, teamEnnemi)
                combat.lancerCombat()


    def loot(self, rarete): #TODO le loot
        print("du loot!!!!")

    def combatDeBoss(self):
        teamEnnemi = Team()
        if(self.__etage == 1):
            print("Maïté vous bloque l'accès à la sortie!")
            time.sleep(1.5)
            print("Maïté : c'est leur de passer à table!!!")
            time.sleep(1.5)
            teamEnnemi.ajouterPersonnage(copy.deepcopy(grosTas))
            teamEnnemi.ajouterPersonnage(copy.deepcopy(maite))
            teamEnnemi.ajouterPersonnage(copy.deepcopy(grosTas))
        if(self.__etage == 2):
            print("Deux odieux personnages vous bloquent l'accès à la sortie!")
            time.sleep(1.5)
            print("Un par Dieux : Ya encrore un truc qui pu par ici... Et vous là!!!")
            time.sleep(1.5)
            time.sleep("Deux par Dieux : Désolé frérot, je pète de plus en plus souvent ces derniers temps...")
            time.sleep(1.5)
            teamEnnemi.ajouterPersonnage(copy.deepcopy(unParDieux))
            teamEnnemi.ajouterPersonnage(copy.deepcopy(deuxParDieux))
        if(self.__etage == 3):
            print("Un cadavre ambulant vous bloquent l'accès à la sortie!")
            time.sleep(1.5)
            print("Il vient de vous remarquez et se jette sur vous!!!")
            time.sleep(1.5)
            teamEnnemi.ajouterPersonnage(copy.deepcopy(pouilleux))
            teamEnnemi.ajouterPersonnage(copy.deepcopy(jerryLePestifere))
            teamEnnemi.ajouterPersonnage(copy.deepcopy(pouilleux))
        if(self.__etage == 4):
            print("Vous entendez quelqu'un gueuler au loin ")
            time.sleep(1.5)
            print("Ramsey : Vous êtes tous des bons à rien qui ne savez rien faire!!!")
            time.sleep(1.5)           
            print("Ramsey : Vous êtes encore un de ces commis qui ne savent rien faire? Je vais vous apprendre!!!")
            time.sleep(1.5)     
            teamEnnemi.ajouterPersonnage(copy.deepcopy(chevalierCasseCroute))
            teamEnnemi.ajouterPersonnage(copy.deepcopy(ramsayLHysterique))
            teamEnnemi.ajouterPersonnage(copy.deepcopy(chevalierCasseCroute))
        if(self.__etage == 5):
            print("Vous arrivez dans la salle où est prisonnier le chef du village...")
            time.sleep(1.5)
            print("Vous ne savez pas trop comment pourquoi, mais un Panzerkampfwagen IV vous barre la route!!!")
            time.sleep(1.5)           
            print("*Merlin sort de son tank*")
            time.sleep(1.5)     
            print("Merlin : Vous pensiez pouvoir ma battre en tuant tous mes subbordonnées?")
            time.sleep(1.5)  
            print("Merlin : Détrompez-vous!!! Maintenant il est l'heure de mourir!!!")
            time.sleep(1.5) 
            teamEnnemi.ajouterPersonnage(copy.deepcopy(merlinPanzer4))
        combat = Combat(self.__teamHero, teamEnnemi)
        combat.lancerCombat()
        if(combat.getFuiteReussi() == False):
            self.bossTue = True

    def getEnnemi(self):
        i = randint(1, 10)
        if(self.__etage == 1):
            if(i<=4):
                return copy.deepcopy(grosTas)
            if(i<=8):
                return copy.deepcopy(vieuxPoivrot)
            else:
                return copy.deepcopy(golemDeGras)
        if(self.__etage == 2):
            if(i<=4):
                return copy.deepcopy(simpletVillage)
            if(i<=8):
                return copy.deepcopy(cuisinierCannibal)
            else:
                return copy.deepcopy(golemDeJambon)
        if(self.__etage == 3):
            if(i<=4):
                return copy.deepcopy(pouilleux)
            if(i<=8):
                return copy.deepcopy(croqueMort)
            else:
                return copy.deepcopy(golemDAndouillette)
        if(self.__etage == 4):
            if(i<=4):
                return copy.deepcopy(boomer)
            if(i<=8):
                return copy.deepcopy(chevalierCasseCroute)
            else:
                return copy.deepcopy(golemNafnaf)
        if(self.__etage == 5):
            if(i<=4):
                return copy.deepcopy(ombreRampante)
            if(i<=8):
                return copy.deepcopy(psychopate)
            else:
                return copy.deepcopy(geant)


    def selectPerso(self):
        rep = "0xa"
        i = 1
        print("1- Charcutier")
        while rep != "0xd":  # différent de entrée
            rep = hex(
                ord(self.getch()))  # on récupère la touche tapé par l'utilisateur (pas besoin de faire entrée)
            if (rep == "0x7a"):  # z
                if (i != 5):
                    i = i + 1
                else:
                    i = 1
            if (rep == "0x73"):  # s
                if (i > 1):
                    i = i - 1
                else:
                    i = 5
            if(i==1):
                print("1- Charcutier")
            elif(i==2):
                print("2- Pilier de bar")
            elif(i==3):
                print("3- Crève-dalle")
            elif(i==4):
                print("4- Cuistot")
            elif(i==5):
                print("5- Poivrot")
        return i

    def selectPersonnage(self, nbChoix):
        rep = "0xa"
        i = 1
        team = self.getTeamHero()
        team = team.getPersonnages()
        team[i-1].AfficherPersonnage()
        while rep != "0xd":  # différent de entrée
            rep = hex(
                ord(self.getch()))  # on récupère la touche tapé par l'utilisateur (pas besoin de faire entrée)
            if (rep == "0x7a"):  # z
                if (i != nbChoix):
                    i = i + 1
                else:
                    i = 1
                team[i-1].AfficherPersonnage()
            if (rep == "0x73"):  # s
                if (i > 1):
                    i = i - 1
                else:
                    i = nbChoix
                team[i-1].AfficherPersonnage()
        return team[i-1]

    def getch(self):
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch
