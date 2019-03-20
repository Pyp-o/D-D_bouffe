from Competence import *

class CompetenceAttaque(Competence):
    def __init__(self, nom, cout, description, groupe, tauxReussite):
        Competence.__init__(nom, cout, description, groupe, tauxReussite)

    def activerCompetence(self):
        print("j'attaque!!!")