# -*- coding: utf-8 -*-
from Competence import *


class CompetenceAttaque(Competence):
    def __init__(self, nom, cout, description, groupe, tauxReussite, degat):
        Competence.__init__(self,nom, cout, description, groupe, tauxReussite)
        self.__degat = degat

    def activerCompetence(self, combattant, teamAllie, teamEnnemi):
        if (self.getGroupe() == 0):
            print("qui attaquer? (utiliser les z et q pour choisir et entrée pour selectionner)")
            rep = "0x00"
            i=0
            maxRange = teamEnnemi.getLenPersonnage()
            while rep != "0xd": #différent de entrée
                print(teamEnnemi.getPersonnage(i).getNom())
                rep = hex(ord(self.getch()))    #on récupère la touche tapé par l'utilisateur (pas besoin de faire entrée)
                if(rep == "0x7a"):    #z
                    if(i<maxRange-1):
                        i = i+1
                    else :
                        i=0
                if(rep == "0x73"):    #s
                    if(i>0):
                        i = i-1
                    else:
                        i = maxRange - 1
            rand = random.randint(0, 100) #le sort echoue?
            if rand > self.getTauxReussite():
                print("le sort echoue...")
            else: 
                teamEnnemi.getPersonnage(i).setPV(teamEnnemi.getPersonnage(i).getPV()-self.__degat)
                print(teamEnnemi.getPersonnage(i).getNom()+" perd "+str(self.__degat)+"PV!")
        else:   #attaque de groupe
            rand = random.randint(0, 100) #le sort echoue?
            if rand > self.getTauxReussite():
                print("le sort echoue...")
            else:
                for c in teamEnnemi.getPersonnages():
                    c.setPV(c.getPV()-self.__degat)
                    print(c.getNom()+" perd "+str(self.__degat)+"PV!")
            			            
                    
                    

a = Personnage('hero1',0,0,0,0,0,0,0,0,0,0,0,0)
b = Personnage('hero2',0,0,0,0,0,0,0,0,0,0,0,0)
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

c1 = CompetenceAttaque("boule de feu", 3, "lance une boule de feu", 0, 75,5)
c2 = CompetenceAttaque("deluge de feu", 2, "embraise les ennemies", 1, 75,5)
c1.activerCompetence(b, tAlli, tEnn)
