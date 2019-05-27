from SalleEvenement import *

class SalleSortie(SalleEvenement):
    def __init__(self,isExplore, gameMap, x, y, salleDroite, salleGauche, salleHaut, salleBas):
        SalleEvenement.__init__(self, isExplore, x, y, salleDroite, salleGauche, salleHaut, salleBas)
        self.__map = gameMap

    def declancherEvenement(self):
        #print("Vous venez de trouvez la sortie!!!")
        return "sortie"
    
