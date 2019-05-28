# coding: utf8

from Competence import *

class CompetenceRecrutement(Competence):
    def __init__(self, nom, cout, description, groupe, tauxReussite, tauxSupp):
        Competence.__init__(self, nom, cout, description, groupe, tauxReussite)
        self.__tauxSupp = tauxSupp

    def activerCompetence(self, combattant, teamAllie, teamEnnemi, isIA):
        rand = random.randint(0, 100)  # le sort echoue?
        if rand > self.getTauxReussite():
            print("le sort echoue...")
        else:
            for ennemi in teamEnnemi:
                ennemi.getPersonnage().setChanceRejoindre(ennemi.getPersonnage().getChanceRejoindre()+self.__tauxSupp)
                print(ennemi.getNom()+" est séduit de cette générosité")


