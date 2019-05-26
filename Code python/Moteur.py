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
        while(self.end != 1):
            self.end = self.tour()

    def getTeamHero(self):
        return self.__teamHero

    def nouvelleEtage(self):
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
            print("Voulez-vous continuer? (o : oui, n : non)")
            rep = ""
            while rep not in ["o", "n"]:  #o,n
                rep = self.getch()
            if rep == "o":
                self.nouvelleEtage()
        if event == "bagarre":
            teamEnnemi = Team()
            teamEnnemi.ajouterPersonnage(grosTas)
            teamEnnemi.ajouterPersonnage(grosTas)
            combat = Combat(self.__teamHero, teamEnnemi)
            combat.lancerCombat()

            

    def choixPerso(self):
        teamHero = self.getTeamHero()
        return self.selectPersonnage(len(self.__teamHero.getPersonnages()))

    def getch(self):
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch

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
geant = Ennemi("Geant", 35,35,20,20, 5,9,10,5,None,None,None, None, 10)






























############### Memo ######################


