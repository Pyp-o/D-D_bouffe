from Team import *
from Hero import *
from Arme import *
from Map import *
from Personnage import *
from Competence immport *

class Moteur :
    def __init__(self):
        self.__teamHero=Team()
        self.initTeam()
        self.__map = Map()
        self.__map.genererMap(5,5)
        self.end = 0
        while(self.end != 1):
            end = self.tour()

    def getTeamHero(self):
        return self.__teamHero

    def initTeam(self):
        print("---- HEROS ----\n")
        print("1- Charcutier :\t")
        print("Question barbaque il s'y connait, et son embon point montre qu'il teste ses produits. \n\tIl manie avec aisance les armes assez lourdes comme les hachoirs ou les jambons secs entiers\n\n")

        print("2- Pillier de Bar :\t")
        print("C'est le bon copain du village. Il a une résistance à l'alcool impressionnante !! \n\tEt puis, à force de faire la baguarre dans le bar, il résiste plutôt bien aux coups\n\n")

        print("3- Crève-dalle :\t")
        print("Maigre comme un clou, il n'a jamais pu manger à sa faim. Il a donc développé des techniques imparables pour pouvoir manger. \n\tHabitué à voler, il utilise des dagues et se débrouille très bien pour repérer les dangers et les trésors.\n")

        print("4- Cuistot :\t")
        print("Gros comme un cochon, il transforme n'importe quel ingrédient en plat digne d'un roi. \n\tIl parait même que ses plats apportent des pouvoirsmagiques à ceux qui les consomment.\n\n")

        print("5- Poivrot :\t")
        print("Toujours aussi saoul que le pillier de bar, il est pas vraiment copain avec tout le monde... \n\tMais il lance des trucs avec assez de précision pour blesser des gens à chaque coup, ça pourrait être utilse.\n\n")

        choixPrecedent='12'
        for i in range(1, 3):
            print("Choisir le personnage ", i)
            a = input()
            while(a==choixPrecedent or a<'1' or a>'5'):
                if(a==choixPrecedent) :
                    print("Ce personnage a déjà rejoint votre équipe\n")
                else :
                    print("Le personnage choisi n'existe pas\n")
                print("Choisir un autre personnage : \n")
                a=input()
            Jambon = Arme("Jambon", "nul", 1)
            Tonneau = Armure("Tonneau", "nul", 1)
            if (a == '1' and a != choixPrecedent):
                Charcutier = Hero("Charcutier", 10, 10, 5, 5, 3, 2, 15, 10, None, Jambon, Tonneau,
                                        None)  # TODO : Arme, Armure, Compétences, Equilibrage caracteristiques
                self.__teamHero.ajouterPersonnage(Charcutier)
            elif (a == '2' and a!=choixPrecedent):
                Pilier = Hero("Pilier", 10, 10, 5, 5, 3, 2, 15, 10, None, Jambon, Tonneau,
                                    None)  # TODO : Arme, Armure, Compétences, Equilibrage caracteristiques
                self.__teamHero.ajouterPersonnage(Pilier)
            elif (a == '3' and a!=choixPrecedent):
                Creve = Hero("Creve-dalle", 10, 10, 5, 5, 3, 2, 15, 10, None, Jambon, Tonneau,
                                   None)  # TODO : Arme, Armure, Compétences, Equilibrage caracteristiques
                self.__teamHero.ajouterPersonnage(Creve)
            elif (a == '4' and a!=choixPrecedent):
                Cuistot = Hero("Cuistot", 10, 10, 5, 5, 3, 2, 15, 10, None, Jambon, Tonneau,
                                     None)  # TODO : Arme, Armure, Compétences,Equilibrage caracteristiques
                self.__teamHero.ajouterPersonnage(Cuistot)
            elif (a == '5' and a!=choixPrecedent):
                Poivrot = Hero("Poivrot", 10, 10, 5, 5, 3, 2, 15, 10, None, Jambon, Tonneau,
                                     None)  # TODO : Arme, Armure, Compétences, Equilibrage caracteristiques
                self.__teamHero.ajouterPersonnage(Poivrot)
            elif (a == choixPrecedent):
                print("Ce personnage a déjà rejoins votre équipe\n")

            choixPrecedent = a


    def tour(self):
        ok = False
        while(ok != True):
            print("Que voulez-vous faire ? \n-se déplacer (z,q,s,d) \t-gestion d'inventaire (i) \t-statistiques (e)\n\n")
            self.__map.display_maze()
            rep=self.getch()
            if(rep in ['z', 'q', 's', 'd']):
                ok = self.__map.seDeplacer(rep)
            elif (rep=='i'):
                print("choisir un perso à gérer\n")
                perso=self.choixPerso()
                self.__teamHero.getInventaire().choixAction(perso)
                self.__map.display_maze()
            elif (rep=='e'):
                for personnage in self.__teamHero.getPersonnages():
                    personnage.AfficherStat()
        return 0

    def choixPerso(self):
        teamHero = self.getTeamHero()
        self.selectPersonnage(len(self.__teamHero.getPersonnages()))

        def getch(self):
            fd = sys.stdin.fileno()
            old_settings = termios.tcgetattr(fd)
            try:
                tty.setraw(sys.stdin.fileno())
                ch = sys.stdin.read(1)
            finally:
                termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
            return ch

    def selectPersonnage(self, nbChoix):
        rep = "0xa"
        i = 1
        team = self.getTeamHero()
        team = team.getPersonnages()
        print(i)
        while rep != "0xd":  # différent de entrée
            rep = hex(
                ord(self.getch()))  # on récupère la touche tapé par l'utilisateur (pas besoin de faire entrée)
            if (rep == "0x7a"):  # z
                if (i != nbChoix):
                    i = i + 1
                else:
                    i = 1
                team[i-1].AfficherPersonnage()
            if (rep == "0x73"):  # s
                if (i > 1):
                    i = i - 1
                else:
                    i = nbChoix
                team[i-1].AfficherPersonnage()
            print(i)
        return team[i-1]

    def getch(self):
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch


############# TEST #############



































############### Memo ######################


