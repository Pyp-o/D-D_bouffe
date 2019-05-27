# -*- coding: utf-8 -*-

import sys, termios, tty, os, time
from Arme import *
from Armure import *
from Equipement import *
from Consommable import *
from ArmeConsommable import *

class Inventaire():
    def __init__(self):
        self.__items = []

    def ajouterItem(self, item):
        self.__items.append(item)

    def retirerItem(self, item):
        self.__items.remove(item)

    def getitems(self):
        return self.__items

    def afficherEquipement(self):
        for item in self.__items:
            if (isinstance(item, Arme) or isinstance(item, Armure)):
                item.affichageEquipement()

    def afficherEquipementEquipe(self, personnage):
        print("\n***** Equipement Equpé *****")
        a = self.getEquipementEquipe(personnage)
        i=1
        for item in a:
            print(i, "-")
            item.affichageEquipement()
            i+=1

    def afficherEquipementDesequipe(self):
        print("\n***** Equipement Desequpé *****")
        a = self.getEquipementDesequipe()
        i=1
        for item in a:
            print(i, "-")
            item.affichageEquipement()
            i+=1

    def afficherConsommables(self):
        a=self.getConsommables()
        i=1
        for consommable in a:
                print(i, "-")
                consommable.affichageConsommable()
                i+=1

    def getConsommables(self):
        listeConsommables = []
        for item in self.__items:
            if ((isinstance(item, Consommable))):
                listeConsommables.append(item)
        return listeConsommables

    def getEquipementEquipe(self, personnage):
        listEquipement = []
        for item in self.__items:
            if ((isinstance(item, Equipement)) and item.getPorteur()==personnage):
                listEquipement.append(item)
        return listEquipement

    def getEquipementDesequipe(self):
        listEquipement = []
        for item in self.__items:
            if ((isinstance(item, Equipement)) and item.getPorteur()==None):
                listEquipement.append(item)
        return listEquipement


    def Equiper(self, personnage):
        self.afficherEquipementEquipe(personnage)
        self.afficherEquipementDesequipe()
        listEquipement = self.getEquipementDesequipe()
        if (len(listEquipement) > 0):
            print("\nChoisir l'équipement à équiper:")
            choix = self.select(len(listEquipement))
            equipement = listEquipement[choix-1]
            equipement.setPorteur(personnage)
            if(isinstance(equipement, Arme) or isinstance(equipement, ArmeConsommable)):
                if(personnage.getArme()!=None):
                    arme=personnage.getArme()
                    arme.setPorteur(None)
                personnage.setArme(equipement)
                equipement.setPorteur(personnage)
            else:
                if (personnage.getArmure() != None):
                    armure = personnage.getArmure()
                    armure.setPorteur(None)
                personnage.setArmure(equipement)
                equipement.setPorteur(personnage)
        else:
            print("\nAucun equipement dans l'inventaire\n\n")

    def Desequiper(self, personnage):
        self.afficherEquipementEquipe(personnage)
        listEquipement = self.getEquipementEquipe(personnage)
        if (len(listEquipement) > 0):
            print("\nChoisir l'équipement à deséquiper:")
            choix = self.select(len(listEquipement))
            a = listEquipement[choix-1]
            a.retirerPorteur()
            personnage.setArme(None)

        else:
            print("\nAucun equipement equipe\n\n")

    def Manger(self, personnage):
        print("Que faire ?\n1-Manger\n2-Retour\n")
        choix = self.select(2)
        # manger
        consom = self.getConsommables()
        if (len(consom) > 0):  # si liste de consommables non vide
            self.afficherConsommables()  # on affiche
            print("\nChoisir l'item à utiliser:")
            choix = self.select(len(consom))
            a = consom[choix - 1]
            a.utiliser(personnage)
            self.retirerItem(a)
        else:
            print("\nAucun consommable dans l'inventaire\n\n")

    def CreerPotion(self):
        print('\nliste potions possible\n')
        print("\nQuelle potion faire ?\n\n")

    def choixAction(self, personnage):
        choix=1
        while(choix!=-1):
            print("Que faire ?\n1-Gestion de l'équipement\n2-Utilisation de consommables\n3-Création de potions\n4-Retour\n")
            choix=self.select(4)

            #gestion equipement
            if(choix==1):
                self.afficherEquipementEquipe(personnage)
                self.afficherEquipementDesequipe()
                print("\nQue faire ?\n1-Equiper\n2-Désequiper\n3-Retour\n")
                choix=self.select(3)
                #equiper
                print("")
                if(choix == 1):
                    self.Equiper(personnage)


                #desequiper
                elif(choix==2):
                    self.Desequiper(personnage)

            #utilisation consommables
            elif(choix==2):
               self.Manger(personnage)

            #creation de potions
            elif(choix==3):
                self.CreerPotion()
            #sortie d'inventaire
            elif(choix==4):
                choix=-1


    def getch(self):
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch

    def select(self, nbChoix):
        rep="0xa"
        i=1
        print(i)
        while rep != "0xd":  # différent de entrée
            rep = hex(ord(self.getch()))  # on récupère la touche tapé par l'utilisateur (pas besoin de faire entrée)
            if (rep == "0x7a"):  # z
                if (i!=nbChoix):
                    i = i + 1
                else:
                    i = 1
            if (rep == "0x73"):  # s
                if (i > 1):
                    i = i - 1
                else:
                    i = nbChoix
            print(i)
        return i
#TODO : modifier diagramme inventaire, creer methode pour equiper et desequiper ailleurs que dans choixAction, deplacer les actions faites dans choixAction dans des methodes

#inv = Inventaire()
#gourdin = Arme('gourdin', 'morceau de bois moisi', 2)
#tonneau = Armure('tonneau', "planches de bois vermoulues ayant contenu de l'alcool", 3)
#potion1 = Consommable("potion1", "rien", 0, 0, None, 0)
#potion2 = Consommable("potion2", "rien", 0, 0, None, 0)
#potion3 = Consommable("potion3", "rien", 0, 0, None, 0)
#inv.ajouterItem(gourdin)
#inv.ajouterItem(tonneau)
#inv.ajouterItem(potion1)
#inv.ajouterItem(potion2)
#inv.ajouterItem(potion3)
#Gourou = Personnage("Gourou", 5, 5, 5, 5, 0, 0, 0, 0, None, None, None, None)
#inv.choixAction()