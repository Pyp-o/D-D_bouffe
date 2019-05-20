from Arme import *
from Armure import *
class Personnage :
    def __init__(self, nom, PVmax, PV, PCmax, PC, agilite, initiative, attaque, defense,statut, arme, armure, competences):
        self.__nom = nom
        self.__PVmax = PVmax
        self.__PV = PV
        self.__PCmax = PCmax
        self.__PC = PC
        self.__agilite = agilite
        self.__initiative = initiative
        self.__attaque = attaque
        self.__defense = defense
        self.__arme = arme
        self.__armure = armure
        self.__competences = competences
        self.__statut = statut

    def getNom(self):
        return self.__nom
    def setNom(self, nom):
        self.__nom = nom

    def getPVmax(self):
        return self.__PVmax
    def setPVmax(self, PVmax):
        self.__PVmax = PVmax

    def getPCmax(self):
        return self.__PCmax
    def setPCmax(self, PCmax):
        self.__PCmax = PCmax

    def getPV(self):
        return self.__PV
    def setPV(self, PV):
        self.__PV = PV

    def getPC(self):
        return self.__PC
    def setPC(self, PC):
        self.__PC = PC

    def getAgilite(self):
        return self.__agilite
    def setAgilite(self, agilite):
        self.__agilite = agilite

    def getInitiative(self):
        return self.__initiative
    def setInitiative(self, initiative):
        self.__initiative = initiative

    def getAttaque(self):
        return self.__attaque
    def setAttaque(self, attaque):
        self.__attaque = attaque

    def getDefense(self):
        return self.__defense
    def setDefense(self, defense):
        self.__defense = defense

    def getArme(self):
        return self.__arme
    def setArme(self, arme):
        self.__arme = arme

    def getArmure(self):
        return self.__armure
    def setArmure(self, armure):
        self.__armure = armure

    def getCompetences(self):
        return self.__competences
    def addCompetence(self, competence):
        self.__competences.append(competence)

    def getStatut(self):
        return self.__statut

    def AfficherPersonnage(self):
        print("\nLe personnage s'appelle :", self.getNom())

    def AfficherStat(self):
        print("-", self.getNom())
        print('\n**************** Caractéristiques ****************')
        print("Le personnage ", self.getNom(), " a : ", self.getPV(),"/", self.getPVmax(),"PV", end=" ")
        print(self.getPC(),"/", self.getPCmax(),"PC ", "Attaque :", self.getAttaque(), "Defense :", self.getDefense(), end=" ")
        print("Agilité :", self.getAgilite(), "Initiative :", self.getInitiative())
        print("\n**************** Compétences ****************")
        for competence in self.getCompetences():
            competence.AfficherCompetence()
        print("\n**************** Arme ****************")
        arme=self.getArme()
        arme.affichageEquipement()
        print("\n**************** Armure ****************\n")
        armure=self.getArmure()
        armure.affichageEquipement()