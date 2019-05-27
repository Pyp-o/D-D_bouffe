import time

from SalleEvenement import *

class SalleLevier(SalleEvenement):
    def __init__(self,isExplore, gameMap, x, y, salleDroite, salleGauche, salleHaut, salleBas):
        SalleEvenement.__init__(self, isExplore, x, y, salleDroite, salleGauche, salleHaut, salleBas)
        self.__gameMap = gameMap

    def declancherEvenement(self):
        if (self.__gameMap.getLevierActive() == False):
            print("Vous trouvez et activez un levier.")
            print("Vous entendez un bruit sourd au loin...")
            self.__gameMap.setLevierActive(True)
            time.sleep(1.5)
        else:
            i = randint(0,5)
            if i<=1:
                return "bagarre"
