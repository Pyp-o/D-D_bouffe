# -*- coding: utf-8 -*-
from Competence import *
from random import randint


class CompetenceHeal(Competence):
    def __init__(self, nom, cout, description, groupe, tauxReussite, soin):
        Competence.__init__(self, nom, cout, description, groupe, tauxReussite)
        self.__soin = soin

    def activerCompetence(self, combattant, teamAllie, teamEnnemi,isIA):
        if (self.getGroupe() == 0):
            if(isIA == False):
                print("qui soigner? (utiliser les z et q pour choisir et entrée pour selectionner)")
            rep = "0x00"
            i=0
            maxRange = len(teamAllie)
            if(isIA):
                i = randint(0,maxRange-1)
            else:
                while rep != "0xd": #différent de entrée
                    print(teamAllie[i].getNom())
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
                soinPV=teamAllie[i].getPV()+self.__soin
                if (teamAllie[i].getPVmax() >= teamAllie[i].getPV()+soinPV):
                    teamAllie[i].setPV(teamAllie[i].getPV()+self.__soin)
                else: 
                    soinPV = teamAllie[i].getPVmax() - teamAllie[i].getPV()
                    teamAllie[i].setPV(teamAllie[i].getPVmax())
                print(teamAllie[i].getNom()+" gagne "+str(soinPV)+"PV!")
        else:   #attaque de groupe
            rand = random.randint(0, 100) #le sort echoue?
            if rand > self.getTauxReussite():
                print("le sort echoue...")
            else:
                for c in teamAllie:
                    soinPV = c.getPV()+self.__soin
                    if(c.getPVmax() >= c.getPV()+soinPV):
                        c.setPV(soinPV)
                    else:
                        soinPV = c.getPVmax() - c.getPV()
                        c.setPV(c.getPVmax())
                    print(c.getNom()+" gagne "+str(soinPV)+"PV!")





