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
        print("Que faire ?\n1-Gestion de l'équipement\n2-Utilisation de consommables\3-Création de potions")
        choix=input()
        while(choix)
            choix=input()