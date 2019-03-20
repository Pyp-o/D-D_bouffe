from SalleEvenement import *

class SalleCache(SalleEvenement):
    def __init__(self, isExplore, x, y):
        SalleEvenement.__init__(self, isExplore, x, y)

    def declancherEvenement(self):
        print("une salle caché!!!")