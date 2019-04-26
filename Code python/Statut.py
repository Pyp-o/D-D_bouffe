class Statut:
    def __init__(self,tourRestant, personnage):
        self.__tourRestant=tourRestant


    def setTourRestant(self, tour):
        self.__tourRestant=tour

    def getTourRestant(self):
        return self.__tourRestant

    def activerStatut(self, combattant):
        raise NotImplementedError

    def retirerStatut(self, combattant):
        combattant.retirerStatut(self)
