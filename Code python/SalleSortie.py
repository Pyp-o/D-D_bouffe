from SalleEvenement import *

class SalleSortie(SalleEvenement):
    def __init__(self, isExplore, x, y, gameMap):
        SalleEvenement.__init__(self, isExplore, x, y)
        self.__map = gameMap

    def declancherEvenement(self):
        print("Vous venez de trouvez la sortie!!!")
        return "sortie"
    
