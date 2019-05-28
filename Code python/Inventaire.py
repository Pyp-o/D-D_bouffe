# -*- coding: utf-8 -*-

import sys, termios, tty, os, time
from Arme import *
from Armure import *
from Equipement import *
from Consommable import *
from ArmeConsommable import *
#TODO systeme de craft de potion
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
            item.affichageEquipement()
            i+=1

    def afficherEquipementDesequipe(self):
        print("\n***** Equipement Desequpé *****")
        a = self.getEquipementDesequipe()
        i=1
        for item in a:
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
            choix = self.selectEquipement(listEquipement)                  #MODIF EN COURS
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
            choix = self.selectEquipement(listEquipement)
            a = listEquipement[choix-1]
            a.retirerPorteur()
            personnage.setArme(None)

        else:
            print("\nAucun equipement equipe\n\n")

    def Manger(self, personnage):
        consom = self.getConsommables()
        if (len(consom) > 0):  # si liste de consommables non vide
            self.afficherConsommables()  # on affiche
            print("\nChoisir l'item à utiliser:")
            choix = self.selectPotion(consom)
            a = consom[choix - 1]
            a.utiliser(personnage)
            self.retirerItem(a)
        else:
            print("\nAucun consommable dans l'inventaire\n\n")

    def CreerPotion(self):
        print('\nliste potions possible\n')
        print("\nQuelle potion faire ?\n\n")

    def choixAction(self, listPerso):                  #modif en cours -> personnage est un tableau de personnages
        choix=1
        while(choix!=-1):
            print("Que faire ?\n1- Gestion de l'équipement\n2- Utilisation de consommables\n3- Création de potions\n4- Retour\n")
            choix=self.selectAction(4)

            #gestion equipement
            if(choix==1):
                for perso in listPerso:
                    perso.AfficherPersonnage()
                    self.afficherEquipementEquipe(perso)
                    time.sleep(1.2)
                self.afficherEquipementDesequipe()
                time.sleep(1.2)
                print("\nQue faire ?\n1-Equiper\n2-Désequiper\n3-Retour\n")
                choix=self.selectSousAction(3)
                #equiper
                if(choix == 1):
                    ch = self.selectPerso(listPerso)
                    perso=listPerso[ch-1]
                    self.Equiper(perso)


                #desequiper
                elif(choix==2):
                    ch = self.selectPerso(listPerso)
                    perso = listPerso[ch - 1]
                    self.Desequiper(perso)

            #utilisation consommables
            elif(choix==2):
                ch = self.selectPerso(listPerso)
                perso = listPerso[ch - 1]
                self.Manger(perso)

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

    def selectPerso(self, listPerso):
        rep = "0xa"
        print("\nChoisir pour quel personnage :")
        i = 1
        listPerso[0].AfficherPersonnage()
        while rep != "0xd":  # différent de entrée
            rep = hex(ord(self.getch()))  # on récupère la touche tapé par l'utilisateur (pas besoin de faire entrée)
            if (rep == "0x7a"):  # z
                if (i != len(listPerso)):
                    i = i + 1
                else:
                    i = 1
                listPerso[i-1].AfficherPersonnage()
            if (rep == "0x73"):  # s
                if (i > 1):
                    i = i - 1
                else:
                    i = len(listPerso)
                listPerso[i-1].AfficherPersonnage()
        return i


    def selectAction(self, nbChoix):
        rep="0xa"
        i=1
        print("1- Gestion de l'équipement")
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
            if(i==1):
                print("1- Gestion de l'équipement")
            elif(i==2):
                print("2- Utilisation de consommable")
            elif(i==3):
                print("3- Création de potion")
            elif(i==4):
                print("4- Retour")
        return i

    def selectSousAction(self, nbChoix):
        rep = "0xa"
        i = 1
        print("1- Equiper")
        while rep != "0xd":  # différent de entrée
            rep = hex(ord(self.getch()))  # on récupère la touche tapé par l'utilisateur (pas besoin de faire entrée)
            if (rep == "0x7a"):  # z
                if (i != nbChoix):
                    i = i + 1
                else:
                    i = 1
            if (rep == "0x73"):  # s
                if (i > 1):
                    i = i - 1
                else:
                    i = nbChoix
            if (i == 1):
                print("1- Equiper")
            elif (i == 2):
                print("2- Desequiper")
            elif (i == 3):
                print("3- Retour")
        return i

    def selectPotion(self, listConsom):
        rep="0xa"
        i=1
        listConsom[i-1].affichageConsommable()
        while rep != "0xd":  # différent de entrée
            rep = hex(ord(self.getch()))  # on récupère la touche tapé par l'utilisateur (pas besoin de faire entrée)
            if (rep == "0x7a"):  # z
                if (i!=len(listConsom)):
                    i += 1
                else:
                    i = 1
                listConsom[i-1].affichageConsommable()
            if (rep == "0x73"):  # s
                if (i > 1):
                    i -= 1
                else:
                    i = len(listConsom)
                listConsom[i-1].affichageConsommable()
        return i


    def selectEquipement(self, listEquipement):
        rep="0xa"
        i=1
        listEquipement[i-1].affichageEquipement()
        while rep != "0xd":  # différent de entrée
            rep = hex(ord(self.getch()))  # on récupère la touche tapé par l'utilisateur (pas besoin de faire entrée)
            if (rep == "0x7a"):  # z
                if (i!=len(listEquipement)):
                    i += 1
                else:
                    i = 1
                listEquipement[i-1].affichageEquipement()
            if (rep == "0x73"):  # s
                if (i > 1):
                    i -= 1
                else:
                    i = len(listEquipement)
                listEquipement[i-1].affichageEquipement()
        return i



