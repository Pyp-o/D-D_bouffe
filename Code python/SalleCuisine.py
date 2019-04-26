from SalleEvenement import *

class SalleCuisine(SalleEvenement):
    def __init__(self):
        self.__cuisine=1

    def getCuisine(self):
        return self.__cuisine