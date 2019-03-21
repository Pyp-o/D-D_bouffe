class Item():
    def __init__(self, nom, description):
        self.__nom = nom
        self.__description = description

    def getNom(self):
        return self.__nom

    def getDescription(self):
        return self.__description
