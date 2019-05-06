# -*- coding: utf-8 -*-

import sys, termios, tty, os, time
from Arme import *
from Armure import *
from Equipement import *
from Consommable import *

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

    def afficherEquipementEquipe(self):
        for item in self.__items:
            if ((isinstance(item,Arme) or isinstance(item, Armure)) and item.getPorteur()!=None):
                item.affichageEquipement()

    def afficherEquipementDesequipe(self):
        for item in self.__items:
            if ((isinstance(item,Arme) or isinstance(item, Armure)) and item.getPorteur()==None):
                item.affichageEquipement()

    def afficherConsommables(self):
        i=1
        for consommable in self.__items:
            if((isinstance(consommable, Consommable))):
                print(i, "-")
                consommable.affichageConsommable()
                i+=1

    def getConsommables(self):
        listeConsommables = []
        for item in self.__items:
            if ((isinstance(item, Consommable))):
                listeConsommables.append(item)
        return listeConsommables

    def getEquipementEquipe(self):
        listEquipement = []
        for item in self.__items:
            if ((isinstance(item, Equipement)) and item.getPorteur()==None):
                listEquipement.append(item)
        return listEquipement

    def choixAction(self):
        choix=1
        while(choix!=-1):
            print("Que faire ?\n1-Gestion de l'équipement\n2-Utilisation de consommables\n3-Création de potions\n4-Retour\n")
            choix=self.select(4)

            #gestion equipement
            if(choix==1):
                print("Que faire ?\n1-Equiper\n2-Désequiper\n3-Retour\n")
                choix=self.select(3)
                #equiper
                if(choix==1):
                    self.afficherEquipementEquipe()
                    self.afficherEquipementDesequipe()
                    listEquipement=self.getEquipementEquipe()
                    if(len(listEquipement)>0):
                        print("\nChoisir l'équipement à équiper:")
                        choix=self.select(len(listEquipement))
                        print("\nChoisir le personnage qui va s'en equiper")
                        #recuperer le personnage qui va s'equiper
                    else:
                        print("\nAucun equipement dans l'inventaire\n\n")

                #desequiper
                elif(choix==2):
                    self.afficherEquipementEquipe()

            #utilisation consommables
            elif(choix==2):
                print("Que faire ?\n1-Manger\n2-Retour\n")
                choix=self.select(2)
                #manger
                consom=self.getConsommables()
                if(len(consom)>0):                      #si liste de consommables non vide
                    self.afficherConsommables()         #on affiche
                    print("\nChoisir l'item à utiliser:")
                    choix=self.select(len(consom))
                    a = consom[choix-1]
                    print("\nChoisir le personnage qui va en beneficier:")
                    #recuperer le personnage qui va en beneficier
                    self.retirerItem(a)
                else:
                    print("\nAucun consommable dans l'inventaire\n\n")

            #creation de potions
            elif(choix==3):
                print('\nliste potions possible\n')
                print("\nQuelle potion faire ?\n\n")

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

inv = Inventaire()
gourdin = Arme('gourdin', 'morceau de bois moisi', 2)
tonneau = Armure('tonneau', "planches de bois vermoulues ayant contenu de l'alcool", 3)
potion1 = Consommable("potion1", "rien", 0, 0, None, 0)
potion2 = Consommable("potion2", "rien", 0, 0, None, 0)
potion3 = Consommable("potion3", "rien", 0, 0, None, 0)
inv.ajouterItem(gourdin)
inv.ajouterItem(tonneau)
inv.ajouterItem(potion1)
inv.ajouterItem(potion2)
inv.ajouterItem(potion3)
Gourou = Personnage("Gourou", 5, 5, 5, 5, 0, 0, 0, 0, None, None, None, None)
inv.choixAction()