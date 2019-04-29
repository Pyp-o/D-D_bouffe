from Competence import *

class CompetenceBuff(Competence):
    def __init__(self, nom, cout, description, groupe, tauxReussite, degatBuff, armureBuff, agiliteBuff):
        Competence.__init__(self, nom, cout, description, groupe, tauxReussite)
        self.__degatBuff = degatBuff
        self.__armureBuff = armureBuff
        self.__agiliteBuff = agiliteBuff

    def activerCompetence(self):
        print("je buff!!!")
