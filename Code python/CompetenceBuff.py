# coding: utf8

from Competence import *

class CompetenceBuff(Competence):
    def __init__(self, nom, cout, description, groupe, tauxReussite, degatBuff, defenseBuff, agiliteBuff, forEnnemi):
        Competence.__init__(self, nom, cout, description, groupe, tauxReussite)
        self.__degatBuff = degatBuff
        self.__defenseBuff = defenseBuff
        self.__agiliteBuff = agiliteBuff
        self.__forEnnemi = forEnnemi      #est ce une competence à destination des ennemies
        self.__teamConcerned = 0

    def activerCompetence(self, combattant, teamAllie, teamEnnemi):
        if self.__forEnnemi == True:    #on buff ou debuff quelle team?
            self.__teamConcerned = teamEnnemi
        else:
            self.__teamConcerned = teamAllie
        if (self.getGroupe() == 0):
            print("qui sera affecter? (utiliser les z et q pour choisir et entrée pour selectionner)")
            rep = "0x00"
            i = 0
            maxRange = len(self.__teamConcerned)
            while rep != "0xd":  # différent de entrée
                print(self.__teamConcerned[i].getNom())
                rep = hex(
                    ord(self.getch()))  # on récupère la touche tapé par l'utilisateur (pas besoin de faire entrée)
                if (rep == "0x7a"):  # z
                    if (i < maxRange - 1):
                        i = i + 1
                    else:
                        i = 0
                if (rep == "0x73"):  # s
                    if (i > 0):
                        i = i - 1
                    else:
                        i = maxRange - 1
            rand = random.randint(0, 100)  # le sort echoue?
            if rand > self.getTauxReussite():
                print("le sort echoue...")
            else:
                if self.__degatBuff != 0: #est ce un buff de degat?
                    self.__teamConcerned[i].setAttaque(self.__teamConcerned[i].getAttaque() + self.__degatBuff)
                    if(self.__degatBuff>0):
                        print(self.__teamConcerned[i].getNom() + " gagne " + str(self.__degatBuff) + "point d'attaque!")
                    else:
                        print(self.__teamConcerned[i].getNom() + " perd " + str(abs(self.__degatBuff)) + "point d'attaque!")
                if self.__defenseBuff != 0: #est ce un buff de defense?
                    self.__teamConcerned[i].setDefense(self.__teamConcerned[i].getDefense() + self.__defenseBuff)
                    if(self.__defenseBuff>0):
                        print(self.__teamConcerned[i].getNom() + " gagne " + str(self.__defenseBuff) + "point de defense!")
                    else:
                        print(self.__teamConcerned[i].getNom() + " perd " + str(abs(self.__defenseBuff)) + "point de defense!")
                if self.__agiliteBuff != 0: #est ce un buff d'agilite?
                    self.__teamConcerned[i].setAgilite(self.__teamConcerned[i].getAgilite() + self.__agiliteBuff)
                    if(self.__agiliteBuff>0):
                        print(self.__teamConcerned[i].getNom() + " gagne " + str(self.__agiliteBuff) + "point d'agilité!")
                    else:
                        print(self.__teamConcerned[i].getNom() + " perd " + str(abs(self.__agiliteBuff)) + "point d'agilité!")
        else:  # attaque de groupe
            rand = random.randint(0, 100)  # le sort echoue?
            if rand > self.getTauxReussite():
                print("le sort echoue...")
            else:
                for c in self.__teamConcerned:
                    if self.__degatBuff != 0:  # est ce un buff de degat?
                        c.setAttaque(c.getAttaque() + self.__degatBuff)
                        if (self.__degatBuff > 0):
                            print(c.getNom() + " gagne " + str(self.__degatBuff) + "point d'attaque!")
                        else:
                            print(c.getNom() + " perd " + str(abs(self.__degatBuff)) + "point d'attaque!")
                    if self.__defenseBuff != 0:  # est ce un buff de defense?
                        c.setDefense(c.getDefense() + self.__defenseBuff)
                        if(self.__defenseBuff>0):
                            print(c.getNom() + " gagne " + str(
                            self.__defenseBuff) + "point de defense!")
                        else:
                            print(c.getNom() + " perd " + str(
                            abs(self.__defenseBuff)) + "point de defense!")
                    if self.__agiliteBuff != 0:  # est ce un buff d'agilite?
                        c.setAgilite(c.getAgilite() + self.__agiliteBuff)
                        if(self.__agiliteBuff>0):
                            print(c.getNom() + " gagne " + str(
                            self.__agiliteBuff) + "point d'agilité!")
                        else:
                            print(c.getNom() + " perd " + str(
                            abs(self.__agiliteBuff)) + "point d'agilité!")



