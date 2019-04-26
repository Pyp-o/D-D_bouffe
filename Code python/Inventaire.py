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
        print("Que faire ?\n1-Gestion de l'équipement\n2-Utilisation de consommables\n3-Création de potions\n4-Retour")
        choix=input()
        while(choix!='1' and choix!='2' and choix!='3' and choix!='4'):
            print("\nChoix erroné\n\nQue faire ?\n1-Gestion de l'équipement\n2-Utilisation de consommables\n3-Création de potions\n4-Retour")
            choix=input()

inv = Inventaire()
inv.gestionInventaire()