# -*- coding: utf-8 -*-

from Team import *
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
from Combat import *
import copy
import random 

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

        print("2- Pillier de Bar :\t")
        print("C'est le bon copain du village. Il a une résistance à l'alcool impressionnante !! \n\tEt puis, à force de faire la baguarre dans le bar, il résiste plutôt bien aux coups\n\n")

        print("3- Crève-dalle :\t")
        print("Maigre comme un clou, il n'a jamais pu manger à sa faim. Il a donc développé des techniques imparables pour pouvoir manger. \n\tHabitué à voler, il utilise des dagues et se débrouille très bien pour repérer les dangers et les trésors.\n")

        print("4- Cuistot :\t")
        print("Gros comme un cochon, il transforme n'importe quel ingrédient en plat digne d'un roi. \n\tIl parait même que ses plats apportent des pouvoirsmagiques à ceux qui les consomment.\n\n")

        print("5- Poivrot :\t")
        print("Toujours aussi saoul que le pillier de bar, il est pas vraiment copain avec tout le monde... \n\tMais il lance des trucs avec assez de précision pour blesser des gens à chaque coup, ça pourrait être utilse.\n\n")

        choixPrecedent='12'
        for i in range(1, 3):
            print("Choisir le personnage ", i)
            a = input()
            while(a not in ['1','2','3','4','5'] or a == choixPrecedent):
                if(a==choixPrecedent) :
                    print("Ce personnage a déjà rejoint votre équipe\n")
                else :
                    print("Le personnage choisi n'existe pas\n")
                print("Choisir un autre personnage : \n")
                a=input()
            Jambon = Arme("Jambon1", "nul", 1)
            Tonneau = Armure("Tonneau1", "nul", 1)
            bouleFeu = CompetenceAttaque("boule de feu", 3, "lance une boule de feu", 0, 75,5)
            delugeFeu = CompetenceAttaque("deluge de feu", 2, "embraise les ennemies", 1, 75,5)
            soinMineur = CompetenceHeal("soin mineur", 3, "soigne de facon mineur", 0, 80, 7)
            buffAttaque = CompetenceBuff("Encouragement!", 2, "Gueule sur un allié", 0, 85, 4, 0, 0, 0)

            poison = Empoisonne("empoisonné",4)
            vomi = CompetenceStatut("vomir",5, "vomit sur un ennemi",0,70,poison, 0)


            competences = []
            competences.append(delugeFeu)
            competences.append(bouleFeu)
            competences.append(soinMineur)
            competences.append(vomi)
            competences.append(buffAttaque)
            t = self.getTeamHero().getInventaire()
            if (a == '1' and a != choixPrecedent):
                Charcutier = Hero("Charcutier", 35, 35, 20, 20, 8, 8, 8, 2, None, None, None,  #nom, PVmax, PV, PCmax, PC, agilite, initiative, attaque, defense, statut, arme, armure, competence, chanceRejoindre
                                        competences)  # TODO : Arme, Armure, Compétences, Equilibrage caracteristiques
                self.__teamHero.ajouterPersonnage(Charcutier)
                Jambon = copy.deepcopy(Jambon)
                Tonneau = copy.deepcopy(Tonneau)
                t.ajouterItem(Jambon)
                t.ajouterItem(Tonneau)
            elif (a == '2' and a!=choixPrecedent):
                Pilier = Hero("Pilier", 35, 35, 30, 30, 6, 11, 5, 1, None, None, None,
                                    competences)  # TODO : Arme, Armure, Compétences, Equilibrage caracteristiques
                self.__teamHero.ajouterPersonnage(Pilier)
                Jambon = copy.deepcopy(Jambon)
                Tonneau = copy.deepcopy(Tonneau)
                t.ajouterItem(Jambon)
                t.ajouterItem(Tonneau)
            elif (a == '3' and a!=choixPrecedent):
                Creve = Hero("Creve-dalle", 25, 25, 25, 25, 25, 12, 7, 1, None, Jambon, Tonneau,
                                   competences)  # TODO : Arme, Armure, Compétences, Equilibrage caracteristiques
                self.__teamHero.ajouterPersonnage(Creve)
                t.ajouterItem(Jambon)
                t.ajouterItem(Tonneau)
            elif (a == '4' and a!=choixPrecedent):
                Cuistot = Hero("Cuistot", 35, 35, 30, 30, 6, 7, 4, 2, None, Jambon, Tonneau,
                                     competences)  # TODO : Arme, Armure, Compétences,Equilibrage caracteristiques
                self.__teamHero.ajouterPersonnage(Cuistot)
                t.ajouterItem(Jambon)
                t.ajouterItem(Tonneau)
            elif (a == '5' and a!=choixPrecedent):
                Poivrot = Hero("Poivrot", 40, 40, 20, 20, 4, 5, 5, 3, None, Jambon, Tonneau,
                                     competences)  # TODO : Arme, Armure, Compétences, Equilibrage caracteristiques
                self.__teamHero.ajouterPersonnage(Poivrot)
                t.ajouterItem(Jambon)
                t.ajouterItem(Tonneau)
            elif (a == choixPrecedent):
                print("Ce personnage a déjà rejoins votre équipe\n")

            choixPrecedent = a

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
                perso=self.choixPerso()
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
            for x in range(1,i):
                teamEnnemi.ajouterPersonnage(self.getEnnemi())
            combat = Combat(self.__teamHero, teamEnnemi)
            combat.lancerCombat()

    def combatDeBoss(self):
        teamEnnemi = Team()
        if(self.__etage == 1):
            print("Maïté vous bloque l'accès à la sortie!")
            sleep(1.5)
            print("Maïté : c'est leur de passer à table!!!")
            sleep(1.5)
            teamEnnemi.ajouterPersonnage(copy.deepcopy(grosTas))
            teamEnnemi.ajouterPersonnage(copy.deepcopy(maite))
            teamEnnemi.ajouterPersonnage(copy.deepcopy(grosTas))
        if(self.__etage == 2):
            print("Deux odieux personnages vous bloquent l'accès à la sortie!")
            sleep(1.5)
            print("Un par Dieux : Ya encrore un truc qui pu par ici... Et vous là!!!")
            sleep(1.5)
            print("Deux par Dieux : Désolé frérot, je pète de plus en plus souvent ces derniers temps...")
            sleep(1.5)
            teamEnnemi.ajouterPersonnage(copy.deepcopy(unParDieux))
            teamEnnemi.ajouterPersonnage(copy.deepcopy(deuxParDieux))
        if(self.__etage == 3):
            print("Un cadavre ambulant vous bloquent l'accès à la sortie!")
            sleep(1.5)
            print("Il vient de vous remarquez et se jette sur vous!!!")
            sleep(1.5)
            teamEnnemi.ajouterPersonnage(copy.deepcopy(pouilleux))
            teamEnnemi.ajouterPersonnage(copy.deepcopy(jerryLePestifere))
            teamEnnemi.ajouterPersonnage(copy.deepcopy(pouilleux))
        if(self.__etage == 4):
            print("Vous entendez quelqu'un gueuler au loin ")
            sleep(1.5)
            print("Ramsey : Vous êtes tous des bons à rien qui ne savez rien faire!!!")
            sleep(1.5)           
            print("Ramsey : Vous êtes encore un de ces commis qui ne savent rien faire? Je vais vous apprendre!!!")
            sleep(1.5)     
            teamEnnemi.ajouterPersonnage(copy.deepcopy(chevalierCasseCroute))
            teamEnnemi.ajouterPersonnage(copy.deepcopy(ramsayLHysterique))
            teamEnnemi.ajouterPersonnage(copy.deepcopy(chevalierCasseCroute))
        if(self.__etage == 5):
            print("Vous arrivez dans la salle où est prisonnier le chef du village...")
            sleep(1.5)
            print("Vous ne savez pas trop comment pourquoi, mais un Panzerkampfwagen IV vous barre la route!!!")
            sleep(1.5)           
            print("*Merlin sort de son tank*")
            sleep(1.5)     
            print("Merlin : Vous pensiez pouvoir ma battre en tuant tous mes subbordonnées?")
            sleep(1.5)  
            print("Merlin : Détrompez-vous!!! Maintenant il est l'heure de mourir!!!")
            sleep(1.5) 
            teamEnnemi.ajouterPersonnage(copy.deepcopy(merlinPanzer4))
        combat = Combat(self.__teamHero, teamEnnemi)
        combat.lancerCombat()
        if(combat.getFuiteReussi() == False):
            self.bossTue = True


    def getEnnemi(self):
        i = random.randint(1,10)
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


    def choixPerso(self):
        teamHero = self.getTeamHero()
        return self.selectPersonnage(len(self.__teamHero.getPersonnages()))

    def selectPersonnage(self, nbChoix):
        rep = "0xa"
        i = 1
        team = self.getTeamHero()
        team = team.getPersonnages()
        print(i)
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
            print(i)
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


############# LORE #############
Jambon = Arme("Jambon", "nul", 1)
Tonneau = Armure("Tonneau", "nul", 1)
#etage 1
grosTas = Ennemi("Gros tas", 10, 10, 0, 0, 6, 8, 5, 2, None, Jambon, Tonneau, None, 10)   #nom, PVmax, PV, PCmax, PC, agilite, initiative, attaque, defense, statut, arme, armure, competence, chanceRejoindre
vieuxPoivrot = Ennemi("Vieux poivrot", 10, 10, 10,10,8,6,3,2,None, None, None, None, 10)
golemDeGras = Ennemi("Golem de gras", 16, 16, 10, 10, 5, 7, 6, 2,None,None,None, None, 10)

#etage 2
simpletVillage = Ennemi("Simplet du village", 13, 13, 5, 5, 20, 10, 6,1,None,None,None, None, 10)
cuisinierCannibal = Ennemi("Cuisinier cannibal", 18, 18, 10, 10, 7, 7, 3, 3, None,None,None, None, 10)
golemDeJambon = Ennemi("Golem de jambon", 20, 20, 10, 10, 5, 8, 7, 3, None,None,None, None, 10)

#etage 3
pouilleux = Ennemi("Pouilleux", 18, 18, 25, 25, 10, 10, 5, 2, None,None,None, None, 10)
croqueMort = Ennemi("Croque-mort", 18, 18, 20, 20, 6, 9, 1, 2, None,None,None, None, 10)
golemDAndouillette = Ennemi("Golemn d'andouillette", 23, 23, 15, 15, 5, 8, 8, 3, None,None,None, None, 10)

#etage 4
boomer = Ennemi("Boomer", 8, 8, 5, 5, 5, 5, 1, 2, None,None,None, None, 10)
chevalierCasseCroute = Ennemi("Chevalier Casse-croute", 25, 25, 0, 0, 6, 8, 7, 4, None,None,None, None, 10)
golemNafnaf = Ennemi("Golem Nafnaf", 30, 30, 15, 15, 5, 8, 8, 4, None,None,None, None, 10)

#etage 5
ombreRampante = Ennemi("Ombre rampante", 10,10,10,10, 66, 13, 5, 1, None,None,None, None, 10)
psychopate = Ennemi("Psychopathe", 20, 20, 0, 0, 10, 10, 9, 2, None,None,None, None, 10)
geant = Ennemi("Geant", 35,35,20,20, 5,9,10,5, None,None,None, None, 10)

#boss etage1
maite = Ennemi("Maïte", 20, 20, 20, 20, 7, 20, 6, 3, None,None,None, None, 10)
#boss etage2
unParDieux = Ennemi("Un par Dieux", 30,30,5,5, 5, 20, 6, 3, None,None,None, None, 10)
deuxParDieux = Ennemi("Deux par Dieux", 15, 15, 10, 10, 6, 20, 8, 3, None,None,None, None, 10)
#boss etage 3
jerryLePestifere = Ennemi("Jerry le Pestiféré", 55, 55, 20, 20, 10, 20, 6, 3, None,None,None, None, 10)
#boss etage 4
ramsayLHysterique = Ennemi("Ramsay l'hystérique", 75, 75, 15, 15, 10, 20, 9, 4, None,None,None, None, 10)
#boss etage 5
merlinPanzer4 = Ennemi("Merlin et son Panzerkampfwagen IV", 150, 150, 50, 50, 1, 20, 12, 5, None,None,None, None, 10)




























############### Memo ######################


