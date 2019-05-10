class Statut:
    def __init__(self, nom, tourRestant):
        self.__nom = nom
        self.__tourRestant=tourRestant


    def setTourRestant(self, tour):
        self.__tourRestant=tour

    def getTourRestant(self):
        return self.__tourRestant

    def activerStatut(self, combattant):
        raise NotImplementedError

    def retirerStatut(self, combattant):
        combattant.retirerStatut(self)

    def getNom(self):
        return self.__nom
