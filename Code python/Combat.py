from Team import *
from Combattant import *

#CLASSE A FINIR

class Combat():
    def __init__(self, teamHero, teamEnnemi):
        self.__teamHero = teamHero  #objet Team
        self.__teamEnnemi = teamEnnemi  #objet Team
        self.__teamCombattantsEnnemi = []   #list de Combattants
        self.__teamCombattantsHero = [] #list de Combattants
        self.__creationCombattant()
        self.__definitionOrdrePassage()


    def __creationCombattant(self):
        for personnage in self.__teamHero.getPersonnages():
            self.__teamCombattantsHero.append(Combattant(personnage, True))
        for personnage in self.__teamEnnemi.getPersonnages():
            self.__teamCombattantsEnnemi.append(Combattant(personnage, False))

    def __definitionOrdrePassage(self):
        i = 1 #nb combattant avec un ordre assigné
        n = len(self.__teamCombattantsEnnemi) + len(self.__teamCombattantsHero) #nombre de combattant a assigné
        combattantSelectionne = self.__teamCombattantsEnnemi[0]     #on assigne un combattant au hasard 
        while i!=n+1:
            initMax = -1 #on va chercher qui a la plus grande initiative parmis les combattant qui n'ont pas encore eu un ordre assigné
            
            for combattant in self.__teamCombattantsHero:
                #print(combattant.getOrdre())
                if ((combattant.getOrdre() == -1) and (combattant.getInitiative() > initMax)):
                    combattantSelectionne = combattant
                    initMax = combattant.getInitiative()
            for combattant in self.__teamCombattantsEnnemi:     #et également pour les ennemies
                if ((combattant.getOrdre() == -1) and (combattant.getInitiative() > initMax)):
                    initMax = combattant.getInitiative()
                    combattantSelectionne = combattant
            
            combattantSelectionne.setOrdre(i)   #on attribut un ordre de passage à ce combattant
            i = i+1
        for combattant in self.__teamCombattantsHero:
            print(combattant.getOrdre())
        for combattant in self.__teamCombattantsEnnemi:
            print(combattant.getOrdre())
        
hero1 = Personnage('hero1',50,30,0,0,0,12,0,0,0,0,0,0)   #nom,  PVmax, PV, PCmax, PC, Agi, Init, Attaque, Def, Statut, Arme, Armure, Competence
hero2 = Personnage('hero2',50,30,0,0,0,15,0,0,0,0,0,0)
hero3 = Personnage('hero3',0,0,0,0,0,5,0,0,0,0,0,0)

enne1 = Personnage('enne1',50,30,0,0,0,30,0,0,0,0,0,0)
enne2 = Personnage('enne2',50,30,0,0,0,11,0,0,0,0,0,0)
enne3 = Personnage('enne3',0,0,0,0,0,13,0,0,0,0,0,0)


tAlli = Team()
tEnn = Team()
tAlli.ajouterPersonnage(hero1)
tAlli.ajouterPersonnage(hero2)
tAlli.ajouterPersonnage(hero3)
tEnn.ajouterPersonnage(enne1)
tEnn.ajouterPersonnage(enne2)
tEnn.ajouterPersonnage(enne3)

c = Combat(tAlli, tEnn)
