class Inventaire():
    def __init__(self):
        self.__items = []

    def ajouterItem(self, item):
        self.__items.append(item)

    def retirerItem(self, item):
        self.__items.remove(item)

    def getitems(self):
        return self.__items

    def gestionInventaire(self):
        choix=-1
        while(choix!=0):
            print("Que faire ?\n1-Gestion de l'équipement\n2-Utilisation de consommables\n3-Création de potions\n4-Retour")
            choix=input()
            while(choix!='1' and choix!='2' and choix!='3' and choix!='4'):
                print("\nChoix erroné\n\nQue faire ?\n1-Gestion de l'équipement\n2-Utilisation de consommables\n3-Création de potions\n4-Retour")
                choix=input()

            #gestion equipement
            if(choix=='1'):
                print("Que faire ?\n1-Equiper\n2-Désequiper\n3-Retour\n")
                choix=input()
                while (choix != '1' and choix != '2' and choix != '3'):
                    print("\nChoix erroné\n\nQue faire ?\n1-Equiper\n2-Désequiper\n3-Retour\n")
                    choix=input()
                #equiper
                if(choix=='1'):
                    print("equipement actuel + stat")
                    print("\nEquipement non equipe + stat")
                    #TODO : choix equipement par chiffre
                    choix=0
                #desequiper
                if(choix=='2'):
                    print("equipement actuel + stat")
                    choix=0

            #utilisation consommables
            if(choix=='2'):
                print("Que faire ?\n1-Manger\n2-Retour\n")
                choix=input()
                while (choix != '1' and choix != '2' and choix != '3'):
                    print("\nChoix erroné\n\nQue faire ?\n1-Equiper\n2-Désequiper\n3-Retour\n")
                    choix=input()
                #equiper
                if(choix=='1'):
                    print("equipement actuel + stat")
                    print("\nEquipement non equipe + stat")
                    choix=0
                #desequiper
                if(choix=='2'):
                    print("equipement actuel + stat")
                    choix=0



inv = Inventaire()
inv.gestionInventaire()