# coding: utf8

from Competence import *

class CompetenceInvocation(Competence):
    def __init__(self, nom, cout, description, groupe, tauxReussite, tauxSupp):
        Competence.__init__(self, nom, cout, description, groupe, tauxReussite)
        self.__tauxSupp = tauxSupp

    def activerCompetence(self, combattant, teamAllie, teamEnnemi):
        rand = random.randint(0, 100)  # le sort echoue?
        if rand > self.getTauxReussite():
            print("le sort echoue...")
        else:
			for ennemi in teamEnnemi:
				ennemi.getPersonnage().setChanceRejoindre(ennemi.chanceRejoindre()+self.__tauxSupp)


