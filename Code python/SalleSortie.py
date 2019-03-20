from SalleEvenement import *

class SalleSortie(SalleEvenement):
    def __init__(self, isExplore, x, y):
        SalleEvenement.__init__(self, isExplore, x, y)

    def declancherEvenement(self):
        print("la sortie!!!")