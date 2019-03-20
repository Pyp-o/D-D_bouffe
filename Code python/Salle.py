class Salle:
    def __init__(self, isExplore, x, y):
        self.__isExplore = isExplore
        self.__x = x
        self.__y = y

    def getX(self):
        return self.__x

    def getY(self):
        return self.__y

    def isExplore(self):
        return self.__isExplore

    def setExplore(self, isExplore):
        self.__isExplore = isExplore