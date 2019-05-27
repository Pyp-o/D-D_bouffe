# coding: utf8

from Competence import *

class CompetenceInvocation(Competence):
    def __init__(self, nom, cout, description, groupe, tauxReussite, invoc):
        Competence.__init__(self, nom, cout, description, groupe, tauxReussite)
        self.__invoc = invoc

    def activerCompetence(self, combattant, teamAllie, teamEnnemi):
        rand = random.randint(0, 100)  # le sort echoue?
        if rand > self.getTauxReussite():
            print("le sort echoue...")
        else:
            teamAllie.append(self.__invoc)
            print(self.__invoc.getNom()+" vient d'être invoqué!")


