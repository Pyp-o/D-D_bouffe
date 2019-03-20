from SalleEvenement import *

class SallePiege(SalleEvenement):
    def __init__(self, isExplore, x, y):
        SalleEvenement.__init__(self, isExplore, x, y)

    def declancherEvenement(self):
        print("un piege!!!")