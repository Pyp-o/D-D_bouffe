from random import choice, randrange as rand
from Salle import *
import sys, termios, tty, os, time	#for getch()

class Map:
    def __init__(self):
        self.__tailleX = 0
        self.__tailleY = 0
        self.__positionX = 0
        self.__positionY = 0

    def getPositionX(self):
        return self.__positionX

    def getPositionY(self):
        return self.__positionY


    def genererMap(self, tailleX, tailleY):
        self.__tailleX = tailleX
        self.__tailleY = tailleY

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
        self.__salles = [([0] * self.width) for _ in range(self.height)]
        self.frontier = set()
        ##
        # Exécution du script
        from sys import argv

        if len(argv) == 3:
            self.width, self.height = map(int, argv[1:])
            self.__grid = [[0] * self.width for _ in range(self.height)]
            self.__salles = [([0] * self.width) for _ in range(self.height)]

        self.creerSalle()

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
            #print("frontier =", self.frontier)
            #print("(%d, %d) -> (%d, %d)" % (x, y, nx, ny))
            #self.display_maze()
            #input("Appuyez sur Entree pour continuer")

            #self.display_maze()
        #print("générer map")
        self.creationFrontiereSalle()

        ##
        # Méthodes utilitaires

    def creerSalle(self):
        for x in range(self.width):
            for y in range(self.height):
                self.__salles[x][y] = Salle(False,x,y)


    def add_frontier(self, x, y):
        if (x >= 0 and y >= 0 and y < len(self.__grid) and x < len(self.__grid[y]) and self.__grid[y][x] == 0):
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

    def creationFrontiereSalle(self):
        for y, row in enumerate(self.__grid):
            for x, cell in enumerate(row):
                if (cell & self.E):
                    self.__salles[x][y].setSalleDoite(self.__salles[x+1][y])
                    #print("on peut aller a doite de : "+str(x) + " " + str(y))
                if (cell & self.N):
                    self.__salles[x][y].setSalleHaut(self.__salles[x][y - 1])
                    #print("on peut aller en haut de : " + str(x) + " " + str(y))
                if (cell & self.S):
                    self.__salles[x][y].setSalleBas(self.__salles[x][y + 1])
                    #print("on peut aller en bas de : " + str(x) + " " + str(y))
                if (cell & self.W):
                    self.__salles[x][y].setSalleGauche(self.__salles[x-1][y])
                    #print("on peut aller a gauche de : " + str(x) + " " + str(y))

    def display_maze(self):
        sys.stdout.write("  ")
        for i in range(self.__tailleX):
            sys.stdout.write(" "+str(i))
        print()
        print('   ' + '_' * (len(self.__grid[0]) * 2 - 1))
        for y, row in enumerate(self.__grid):
            line = str(y)+" |"
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
        return self.__salles[x][y]

    def recupererSalleActuelle(self):
        return self.__salles[self.getPositionX()][self.getPositionY()]

    def seDeplacer(self):
        print("Vous etes en "+str(self.__positionX)+":"+str(self.__positionY))
        print("Vous pouvez vous déplacer vers :")
        haut = 0
        bas =0
        droite = 0
        gauche = 0
        if (self.__salles[self.__positionX][self.__positionY].getSalleHaut()!= None):
            haut=1
            print("le haut (h)")
        if (self.__salles[self.__positionX][self.__positionY].getSalleDroite()!= None):
            droite=1
            print("la droite (d)")
        if (self.__salles[self.__positionX][self.__positionY].getSalleGauche()!= None):
            gauche=1
            print("la gauche (g)")
        if (self.__salles[self.__positionX][self.__positionY].getSalleBas()!= None):
            bas=1
            print("le bas (b)")
        ok = False

        while(ok == False):
            print("Ou voulez-vous aller?")
            saisie = input()
            while(saisie not in ('b','h','g','d')):
                print("Mauvaise saisie")
                print("Ou voulez-vous aller?")
                saisie = input()
            if((saisie == 'h') and haut):
                ok = True
                self.__positionY-=1
            elif ((saisie == 'b') and bas):
                ok = True
                self.__positionY += 1
            elif ((saisie == 'g') and gauche):
                ok = True
                self.__positionX -= 1
            elif ((saisie == 'd') and droite):
                ok = True
                self.__positionX += 1
            else :
                print("Impossible d'aller par là...")
        print("Vous vous déplacer")

    def getch():
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(1)
	 
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch
