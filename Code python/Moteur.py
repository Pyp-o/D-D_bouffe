from Team import *

class Moteur :
    def __init__(self):
        self.__teamHero=Team()
        self.initTeam()

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

        a='9'
        while(a>'5' or a<'1'):
            print("debug")
            print("Choisir le premier personnage : ")
            a=input()
            if(a=='1'):
                Charcutier = Personnage("Charcutier", 10, 10, 5, 5, 3, 2, 15, 10, None, "Jambon", "Tonneau", None)      #TODO : Statut, Arme, Armure, Compétences
                self.__teamHero.ajouterPersonnage(Charcutier)
            elif(a=='3'):
                Pilier = Personnage("Pilier", 10, 10, 5, 5, 3, 2, 15, 10, None, "Jambon", "Tonneau",None)  # TODO : Statut, Arme, Armure, Compétences
                self.__teamHero.ajouterPersonnage(Pilier)
            elif(a=='3'):
                Creve = Personnage("Creve-dalle", 10, 10, 5, 5, 3, 2, 15, 10, None, "Jambon", "Tonneau", None)  # TODO : Statut, Arme, Armure, Compétences
                self.__teamHero.ajouterPersonnage(Creve)
            elif(a=='4'):
                Cuistot = Personnage("Cuistot", 10, 10, 5, 5, 3, 2, 15, 10, None, "Jambon", "Tonneau",None)  # TODO : Statut, Arme, Armure, Compétences
                self.__teamHero.ajouterPersonnage(Cuistot)
            elif(a=='5'):
                Poivrot = Personnage("Poivrot", 10, 10, 5, 5, 3, 2, 15, 10, None, "Jambon", "Tonneau",None)  # TODO : Statut, Arme, Armure, Compétences
                self.__teamHero.ajouterPersonnage(Poivrot)
            else: print("Le code ne correspond à aucun personnage")


m = Moteur()