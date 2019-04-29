from Competence import *

class CompetenceAttaque(Competence):
    def __init__(self, nom, cout, description, groupe, tauxReussite, statut):
        Competence.__init__(self,nom, cout, description, groupe, tauxReussite)
        self.statut = statut

    def activerCompetence(self):
        print("j'affecte un statut!!!")
