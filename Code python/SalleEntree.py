from SalleEvenement import *

class SalleEntree(SalleEvenement):
    def __init__(self, isExplore, x, y):
        SalleEvenement.__init__(self, isExplore, x, y)

    def declancherEvenement(self):
        print("c'est de là que l'on est venu...")