from SalleEvenement import *

class SalleLevier(SalleEvenement):
    def __init__(self, isExplore, x, y):
        SalleEvenement.__init__(self, isExplore, x, y)

    def declancherEvenement(self):
        print("un levier!!!")