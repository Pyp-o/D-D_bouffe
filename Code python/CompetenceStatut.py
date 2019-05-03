# -*- coding: utf-8 -*-

from Competence import *
from Statut import *
from Empoisonne import *    #TODO a delete, seulement pour les test

class CompetenceStatut(Competence):
    def __init__(self, nom, cout, description, groupe, tauxReussite, statut, isEnnemi):
        Competence.__init__(self, nom, cout, description, groupe, tauxReussite)
        self.__statut = statut
        self.__isEnnemi = isEnnemi      #Attribut qui sert à savoir si ce sont les ennemi ou ennemie
        self.__teamConcerned = 0


    def activerCompetence(self,combattant, teamAllie, teamEnnemi):
        if self.__isEnnemi == 1:  # on buff ou debuff quelle team?
            self.__teamConcerned = teamEnnemi
        else:
            self.__teamConcerned = teamAllie
        if (self.getGroupe() == 0):
            print("qui sera affecter? (utiliser les z et q pour choisir et entrée pour selectionner)")
            rep = "0x00"
            i = 0
            maxRange = self.__teamConcerned.getLenPersonnage()
            while rep != "0xd":  # différent de entrée
                print(self.__teamConcerned.getPersonnage(i).getNom())
                rep = hex(
                    ord(self.getch()))  # on récupère la touche tapé par l'utilisateur (pas besoin de faire entrée)
                if (rep == "0x7a"):  # z
                    if (i < maxRange - 1):
                        i = i + 1
                    else:
                        i = 0
                if (rep == "0x73"):  # s
                    if (i > 0):
                        i = i - 1
                    else:
                        i = maxRange - 1
            rand = random.randint(0, 100)  # le sort echoue?
            if rand > self.getTauxReussite():
                print("le sort echoue...")
            else:
                self.__teamConcerned.getPersonnage(i).ajouterStatut(self.__statut)
                print(self.__teamConcerned.getPersonnage(i).getNom() + " est maintenant " + self.__statut.getNom() + "!")
        else:  # attaque de groupe
            rand = random.randint(0, 100)  # le sort echoue?
            if rand > self.getTauxReussite():
                print("le sort echoue...")
            else:
                for c in self.__teamConcerned.getPersonnages():
                    c.ajouterStatut(self.__statut)
                    print(c.getNom() + " est maintenant " + self.__statut.getNom() + "point d'attaque!")

a = Personnage('hero1',50,30,0,0,0,0,0,0,0,0,0,0)
b = Personnage('hero2',50,30,0,0,0,0,0,0,0,0,0,0)
c = Personnage('hero3',0,0,0,0,0,0,0,0,0,0,0,0)
f = Combattant(a,0)
h = Combattant(b,0)
i = Combattant(c,0)


tAlli = Team()
tEnn = Team()
tAlli.ajouterPersonnage(f)
tAlli.ajouterPersonnage(h)
tAlli.ajouterPersonnage(i)
tEnn.ajouterPersonnage(f)
tEnn.ajouterPersonnage(h)
tEnn.ajouterPersonnage(i)

poison = Empoisonne("poison", h, 3)
c1 = CompetenceStatut("jet de poison", 3, "inflige poison", 0, 75, poison, 1)
c2 = CompetenceStatut("deluge de poison", 3, "inflige poison", 1, 75,  poison, 1)
c1.activerCompetence(h, tAlli, tEnn)
#c2.activerCompetence(b, tAlli, tEnn)
#poison.activerStatut(h)
#poison.activerStatut(h)
h.ajouterStatut(poison)
h.activerStatut()
h.activerStatut()
print(str(h.getPV()))