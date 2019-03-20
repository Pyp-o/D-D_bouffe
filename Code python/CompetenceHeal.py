from Competence import *

class CompetenceHeal(Competence):
    def __init__(self, nom, cout, description, groupe, tauxReussite, soin):
        Competence.__init__(nom, cout, description, groupe, tauxReussite)
        self.__soin = soin

    def activerCompetence(self):
        print("je heal!!!")