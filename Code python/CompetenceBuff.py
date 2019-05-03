# coding: utf8

from Competence import *

class CompetenceBuff(Competence):
    def __init__(self, nom, cout, description, groupe, tauxReussite, degatBuff, defenseBuff, agiliteBuff):
        Competence.__init__(self, nom, cout, description, groupe, tauxReussite)
        self.__degatBuff = degatBuff
        self.__defenseBuff = defenseBuff
        self.__agiliteBuff = agiliteBuff

    def activerCompetence(self, combattant, teamAllie, teamEnnemi):
        if (self.getGroupe() == 0):
            print("qui sera affecter? (utiliser les z et q pour choisir et entrée pour selectionner)")
            rep = "0x00"
            i = 0
            maxRange = teamAllie.getLenPersonnage()
            while rep != "0xd":  # différent de entrée
                print(teamAllie.getPersonnage(i).getNom())
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
                    teamAllie.getPersonnage(i).setPV(teamAllie.getPersonnage(i).getAttaque() + self.__degatBuff)
                    print(teamAllie.getPersonnage(i).getNom() + " gagne " + str(self.__degatBuff) + "point d'attaque!")
                if self.__defenseBuff != 0: #est ce un buff de defense?
                    teamAllie.getPersonnage(i).setPV(teamAllie.getPersonnage(i).getDefense() + self.__defenseBuff)
                    print(teamAllie.getPersonnage(i).getNom() + " gagne " + str(self.__defenseBuff) + "point de defense!")
                if self.__agiliteBuff != 0: #est ce un buff d'agilite?
                    teamAllie.getPersonnage(i).setPV(teamAllie.getPersonnage(i).getAgilite() + self.__agiliteBuff)
                    print(teamAllie.getPersonnage(i).getNom() + " gagne " + str(self.__agiliteBuff) + "point d'agilité!")
        else:  # attaque de groupe
            rand = random.randint(0, 100)  # le sort echoue?
            if rand > self.getTauxReussite():
                print("le sort echoue...")
            else:
                for c in teamAllie.getPersonnages():
                    if self.__degatBuff != 0:  # est ce un buff de degat?
                        c.setPV(c.getAttaque() + self.__degatBuff)
                        print(c.getNom() + " gagne " + str(self.__degatBuff) + "point d'attaque!")
                    if self.__defenseBuff != 0:  # est ce un buff de defense?
                        c.setPV(c.getDefense() + self.__defenseBuff)
                        print(c.getNom() + " gagne " + str(
                            self.__defenseBuff) + "point de defense!")
                    if self.__agiliteBuff != 0:  # est ce un buff d'agilite?
                        c.setPV(c.getAgilite() + self.__agiliteBuff)
                        print(c.getNom() + " gagne " + str(
                            self.__agiliteBuff) + "point d'agilité!")


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

c1 = CompetenceBuff("boule de plus d'attaque", 3, "lance une boule de plus d'attaque", 0, 75,5,0,0)
c2 = CompetenceBuff("deluge de plus d'attaque et defense", 2, "embraise les de attaque et def", 1, 75,5,7,0)
c2.activerCompetence(b, tAlli, tEnn)
#c2.activerCompetence(b, tAlli, tEnn)