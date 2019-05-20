from SalleEvenement import *

class SalleLevier(SalleEvenement):
    def __init__(self,isExplore, gameMap, x, y, salleDroite, salleGauche, salleHaut, salleBas):
        SalleEvenement.__init__(self, isExplore, x, y, salleDroite, salleGauche, salleHaut, salleBas)
        self.__gameMap = gameMap
        print(gameMap)

    def declancherEvenement(self):
        print("un levier!!!")
        self.__gameMap.setLevierActive(True)
