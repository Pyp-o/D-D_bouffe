from Ressource import *
from Consommable import *

##### RESSOURCES
PommesDeTerre = Ressource('Pommes de terre crues', 'Des pommes de terres banales')  #nom, description
Oignons = Ressource('Oignons crus', "Des oignons frais")
Carottes = Ressource("Carottes crues", "Des carottes des sables")
Paleron = Ressource("Paleron de boeuf", "Une belle piece de boucher")
Magret = Ressource("Magret de canard", "Une des plus belles piece de boucher")
Andouillettes = Ressource("Andouillettes crues", "Une odeur forte s'en dégage")

##### POTIONS
PotionPomme = Consommable("Pommes de terre sautées", "Rend 15PV", 15, 0, 0, 0, 0, 0, 0, 0, False)
PotionEstouffade = Consommable("Estouffade de pommes de terre et carottes", "Rend 10PC", 0, 10, 0, 0, 0, 0, 0, 0, False)
PotionDaubeOignon = Consommable("Daube à l'oignon", "Augmente de 5 les Pvmax", 0, 0, 5, 0, 0, 0, 0, 0, False)
PotionDaubeCarottes = Consommable("Daube aux carottes", "Augmente de 5 les PCmax", 0, 0, 0, 5, 0, 0, 0, 0, False)
PotionPlat = Consommable("Plat du terroir", "Augmente de 1 l'attaque", 0, 0, 0, 0, 1, 0, 0, 0, False)
PotionCanard = Consommable("Canard et compotée d'oignons", "Augmente de 1 la défense", 0, 0, 0, 0, 0, 1, 0, 0, False)
PotionCanardCarottes = Consommable("Canard aux carottes", "Augmente de 1 l'agilité", 0, 0, 0, 0, 0, 0, 1, 0, False)
PotionDaubeGraisse = Consommable("Daube à la graisse de canard", "Augmente de 1 l'initiative", 0, 0, 0, 0, 0, 0, 0, 1, False)
AndouillettesCanard = Consommable("Andouillettes de canard", "Permet de ressusciter un personnage", 0, 0, 0, 0, 0, 0, 0, 0, True)
Villageoise = Consommable("Villageoise", "Rend 30PV", 30, 0, 0, 0, 0, 0, 0, 0, False)
Kronenbourg = Consommable("Kronenbourg", "Rend 20PC", 0, 30, 0, 0, 0, 0, 0, 0, False)
Gin = Consommable("Gin", "Rend 15PV et 15PC", 15, 15, 0, 0, 0, 0, 0, 0, False)
Jack = Consommable("Jack Daniels", "Augmente de 3 l'attaque", 0, 0, 0, 0, 3, 0, 0, 0, False)
Captain = Consommable("Captain Morgan", "Augmente de 3 la défense", 0, 0, 0, 0, 0, 3, 0, 0, False)
Hic = Consommable("Hic", "Ressuscite et rend tous les PV et PC",999, 999, 0, 0, 0, 0, 0, 0, True)

##### ENNEMIS
#etage 1
grosTas = Ennemi("Gros tas", 10, 10, 0, 0, 6, 8, 5, 2, None, Jambon, Tonneau, None, 10)   #nom, PVmax, PV, PCmax, PC, agilite, initiative, attaque, defense, statut, arme, armure, competence, chanceRejoindre
vieuxPoivrot = Ennemi("Vieux poivrot", 10, 10, 10,10,8,6,3,2,None, None, None, None, 10)
golemDeGras = Ennemi("Golem de gras", 16, 16, 10, 10, 5, 7, 6, 2,None,None,None, None, 10)

#etage 2
simpletVillage = Ennemi("Simplet du village", 13, 13, 5, 5, 20, 10, 6,1,None,None,None, None, 10)
cuisinierCannibal = Ennemi("Cuisinier cannibal", 18, 18, 10, 10, 7, 7, 3, 3, None,None,None, None, 10)
golemDeJambon = Ennemi("Golem de jambon", 20, 20, 10, 10, 5, 8, 7, 3, None,None,None, None, 10)

#etage 3
pouilleux = Ennemi("Pouilleux", 18, 18, 25, 25, 10, 10, 5, 2, None,None,None, None, 10)
croqueMort = Ennemi("Croque-mort", 18, 18, 20, 20, 6, 9, 1, 2, None,None,None, None, 10)
golemDAndouillette = Ennemi("Golemn d'andouillette", 23, 23, 15, 15, 5, 8, 8, 3, None,None,None, None, 10)

#etage 4
boomer = Ennemi("Boomer", 8, 8, 5, 5, 5, 5, 1, 2, None,None,None, None, 10)
chevalierCasseCroute = Ennemi("Chevalier Casse-croute", 25, 25, 0, 0, 6, 8, 7, 4, None,None,None, None, 10)
golemNafnaf = Ennemi("Golem Nafnaf", 30, 30, 15, 15, 5, 8, 8, 4, None,None,None, None, 10)

#etage 5
ombreRampante = Ennemi("Ombre rampante", 10,10,10,10, 66, 13, 5, 1, None,None,None, None, 10)
psychopate = Ennemi("Psychopathe", 20, 20, 0, 0, 10, 10, 9, 2, None,None,None, None, 10)
geant = Ennemi("Geant", 35,35,20,20, 5,9,10,5, None,None,None, None, 10)

#boss etage1
maite = Ennemi("Maïte", 20, 20, 20, 20, 7, 20, 6, 3, None,None,None, None, 10)
#boss etage2
unParDieux = Ennemi("Un par Dieux", 30,30,5,5, 5, 20, 6, 3, None,None,None, None, 10)
deuxParDieux = Ennemi("Deux par Dieux", 15, 15, 10, 10, 6, 20, 8, 3, None,None,None, None, 10)
#boss etage 3
jerryLePestifere = Ennemi("Jerry le Pestiféré", 55, 55, 20, 20, 10, 20, 6, 3, None,None,None, None, 10)
#boss etage 4
ramsayLHysterique = Ennemi("Ramsay l'hystérique", 75, 75, 15, 15, 10, 20, 9, 4, None,None,None, None, 10)
#boss etage 5
merlinPanzer4 = Ennemi("Merlin et son Panzerkampfwagen IV", 150, 150, 50, 50, 1, 20, 12, 5, None,None,None, None, 10)



#viens de moteur
Jambon = Arme("Jambon1", "nul", 1)
Tonneau = Armure("Tonneau1", "nul", 1)
bouleFeu = CompetenceAttaque("boule de feu", 3, "lance une boule de feu", 0, 75,5)
delugeFeu = CompetenceAttaque("deluge de feu", 2, "embraise les ennemies", 1, 75,5)
soinMineur = CompetenceHeal("soin mineur", 3, "soigne de facon mineur", 0, 80, 7)
buffAttaque = CompetenceBuff("Encouragement!", 2, "Gueule sur un allié", 0, 85, 4, 0, 0, 0)

poison = Empoisonne("empoisonné",4)
vomi = CompetenceStatut("vomir",5, "vomit sur un ennemi",0,70,poison, 0)


competences = []
competences.append(delugeFeu)
competences.append(bouleFeu)
competences.append(soinMineur)
competences.append(vomi)
competences.append(buffAttaque)