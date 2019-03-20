class Personnage :
    def __init__(self, nom='Personnage non defini', PVmax, PV, PCmax, PC, agilite, initiative, attaque, defense, statut, arme, armure, competence):
        self.__nom = nom
        self.__PVmax = PVmax
        self.PV = PV
        self.__PCmax = PCmax
        self.__PC = PC
        self.__agilite = agilite
        self.__initiative = initiative
        self.__attaque = attaque
        self.__defense = defense
        self.__statut = statut
        self.__arme = arme
        self.__armure = armure
        self.__competence = competence