class Inventaire():
    def __init__(self):
        self.__items = []

    def ajouterItem(self, item):
        self.__items.append(item)

    def retirerItem(self, item):
        self.__items.remove(item)

    def getitems(self):
        return self.__items

