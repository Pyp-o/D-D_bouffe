from random import choice, randrange as rand
from Salle import *

class Map:
    def __init__(self, tailleX, tailleY):
        self.__tailleX = tailleX
        self.__tailleY = tailleY

    def genererMap(self):


        ##
        # Dimensions du labyrinthe
        self.width = self.__tailleX
        self.height = self.__tailleY

        ##
        # Constantes servant à décrire les directions des passages
        self.N, self.S, self.E, self.W = 1, 2, 4, 8
        self.IN = 0x10
        self.FRONTIER = 0x20
        self.OPPOSITE = {self.E: self.W, self.W: self.E, self.S: self.N, self.N: self.S}

        ##
        # Structures de données
        self.__grid = [([0] * self.width) for _ in range(self.height)]
        self.frontier = set()
        ##
        # Exécution du script
        if __name__ == '__main__':
            from sys import argv

            if len(argv) == 3:
                self.width, self.height = map(int, argv[1:])
                self.__grid = [[0] * self.width for _ in range(self.height)]

            self.mark(rand(self.width), rand(self.height))
            while self.frontier:
                ##
                # Choix d'un voisin à la frontière
                x, y = choice(list(self.frontier))
                self.frontier.remove((x, y))
                nx, ny = choice(list(self.neighbors(x, y)))

                ##
                # Création d'un passage
                dir = self.direction(x, y, nx, ny)
                self.__grid[y][x] |= dir
                self.__grid[ny][nx] |= self.OPPOSITE[dir]

                self.mark(x, y)

                ## DEBUG :
                # print("frontier =", frontier)
                # print("(%d, %d) -> (%d, %d)" % (x, y, nx, ny))
                # display_maze()
                # input("Appuyez sur Entree pour continuer")

            self.display_maze()
        print("générer map")
        ##
        # Méthodes utilitaires
    def add_frontier(self, x, y):
        if (x >= 0 and y >= 0 and y < len(self.__grid)
                and x < len(self.__grid[y]) and self.__grid[y][x] == 0):
            self.__grid[y][x] |= self.FRONTIER
            self.frontier.add((x, y))

    def mark(self, x, y):
        self.__grid[y][x] |= self.IN
        self.add_frontier(x - 1, y)
        self.add_frontier(x + 1, y)
        self.add_frontier(x, y - 1)
        self.add_frontier(x, y + 1)

    def neighbors(self, x, y):
        if x > 0 and (self.__grid[y][x - 1] & self.IN):
            yield (x - 1, y)
        if x + 1 < len(self.__grid[y]) and (self.__grid[y][x + 1] & self.IN):
            yield (x + 1, y)
        if y > 0 and (self.__grid[y - 1][x] & self.IN):
            yield (x, y - 1)
        if y + 1 < len(self.__grid) and (self.__grid[y + 1][x] & self.IN):
            yield (x, y + 1)

    def direction(self, fx, fy, tx, ty):
        return {(fx < tx): self.E,
                (fx > tx):self. W,
                (fy < ty): self.S,
                (fy > ty): self.N}[True]

    def is_empty(self, cell):
        return cell == 0 or cell == self.FRONTIER

    def display_maze(self):
        print()
        print(' ' + '_' * (len(self.__grid[0]) * 2 - 1))
        for y, row in enumerate(self.__grid):
            line = '|'
            for x, cell in enumerate(row):
                # Dessin du mur ou du passage Sud
                if self.is_empty(cell) and y + 1 < len(self.__grid) and self.is_empty(self.__grid[y + 1][x]):
                    line += ' '
                else:
                    line += ' ' if cell & self.S else '_'

                # Dessin du mur ou du passage Est
                if self.is_empty(cell) and x + 1 < len(row) and self.is_empty(row[x + 1]):
                    if y + 1 < len(self.__grid) and (self.is_empty(self.__grid[y + 1][x]) or
                                              self.is_empty(self.__grid[y + 1][x + 1])):
                        line += ' '
                    else:
                        line += '_'
                elif cell & self.E:
                    line += ' ' if (cell | row[x + 1]) &self. S else '_'
                else:
                    line += '|'
            print(line)



    def recupererSalle(self, x, y):
        return 0

    def seDeplacer(self):
        print("je me déplace")

m = Map(10,10)
m.genererMap()
