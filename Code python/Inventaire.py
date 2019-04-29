# -*- coding: utf-8 -*-


from Arme import *
from Armure import *
from Equipement import *

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
        for i in range(0, len(self.__items)):
            if (isinstance(self.__items[i], Arme) or isinstance(self.__items[i], Armure)):
                self.__items[i].affichageEquipement()

    def afficherEquipementEquipe(self):
        for i in range(0, len(self.__items)):
            if ((isinstance(self.__items[i], Arme) or isinstance(self.__items[i], Armure)) and self.__items[i].getPorteur()!=None):
                self.__items[i].affichageEquipement()

    def choixAction(self):
        choix=-1
        while(choix!=0):
            print("Que faire ?\n1-Gestion de l'équipement\n2-Utilisation de consommables\n3-Création de potions\n4-Retour\n")
            choix=input()
            while(choix!='1' and choix!='2' and choix!='3' and choix!='4'):
                print("\nChoix erroné\n\nQue faire ?\n1-Gestion de l'équipement\n2-Utilisation de consommables\n3-Création de potions\n4-Retour\n")
                choix=input()

            #gestion equipement
            if(choix=='1'):
                print("Que faire ?\n1-Equiper\n2-Désequiper\n3-Retour\n")
                choix=input()
                while (choix != '1' and choix != '2' and choix != '3'):
                    print("\nChoix erroné\n\nQue faire ?\n1-Equiper\n2-Désequiper\n3-Retour\n")
                    choix2=input()
                #equiper
                if(choix=='1'):
                    self.afficherEquipementEquipe()
                    self.afficherEquipement()
                #desequiper
                if(choix=='2'):
                    print("equipement actuel + stat\n")

            #utilisation consommables
            elif(choix=='2'):
                print("Que faire ?\n1-Manger\n2-Retour\n")
                choix=input()
                while (choix != '1' and choix != '2'):
                    print("\nChoix erroné\n\nQue faire ?\n1-Manger\n2-Retour\n")
                    choix=input()
                #manger
                if(choix=='1'):
                    print('liste consommables')

            #creation de potions
            elif(choix=='3'):
                print('liste potions possible\n')
                print("\nQuelle potion faire ?")


            #retour
            if(choix=='4'):
                choix=0



    def getch(self):
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch

    def select(self):
        while rep != "0xd":  # différent de entrée
            rep = hex(ord(self.getch()))  # on récupère la touche tapé par l'utilisateur (pas besoin de faire entrée)
            if (rep == "0x7a"):  # z
                if (i!=4):
                    i = i + 1
                else:
                    i = 0
            if (rep == "0x73"):  # s
                if (i > 0):
                    i = i - 1
                else:
                    i = 1
#TODO : gerer fleches directionnelles pour choisir équipement, modifier diagramme inventaire
