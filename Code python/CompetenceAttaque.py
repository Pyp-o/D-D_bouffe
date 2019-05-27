# -*- coding: utf-8 -*-
from Competence import *


class CompetenceAttaque(Competence):
    def __init__(self, nom, cout, description, groupe, tauxReussite, degat, degatFixe):
        Competence.__init__(self,nom, cout, description, groupe, tauxReussite)
        self.__degat = degat
        self.__degatFixe = degatFixe #Faut-il prendre en compte l'attaque du perso?

    def activerCompetence(self, combattant, teamAllie, teamEnnemi):
        if (self.getGroupe() == 0):
            print("qui attaquer? (utiliser les z et q pour choisir et entrée pour selectionner)")
            rep = "0x00"
            i=0
            maxRange = len(teamEnnemi)
            while rep != "0xd": #différent de entrée
                print(teamEnnemi[i].getNom())
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
                if (self.__degatFixe == True):
                    degat = self.__degat
                else:
                    degat = self.__degat+combattant.getAttaque()
                teamEnnemi[i].setPV(teamEnnemi[i].getPV()-degat)
                print(teamEnnemi[i].getNom()+" perd "+str(degat)+"PV!")
        else:   #attaque de groupe
            rand = random.randint(0, 100) #le sort echoue?
            if rand > self.getTauxReussite():
                print("le sort echoue...")
            else:
                for c in teamEnnemi:
                    if (self.__degatFixe == True):
                        degat = self.__degat
                    else:
                        degat = self.__degat+combattant.getAttaque()
                    c.setPV(c.getPV()-degat)
                    print(c.getNom()+" perd "+str(degat)+"PV!")
                                    
                    
                    


