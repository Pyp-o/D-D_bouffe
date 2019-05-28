from Ressource import *
from Consommable import *
from Ennemi import *
from Arme import *
from Armure import *
from ArmeConsommable import *
from CompetenceAttaque import *
from CompetenceHeal import *
from CompetenceBuff import *
from CompetenceStatut import *
from CompetenceRecrutement import *
from CompetenceInvocation import *
from Paralyse import *
from Endormi import *
from Ralenti import *
from Ivre import * 
from Empoisonne import *

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

####ARME
#etage 1
couteauBeurre = Arme("Couteau à beurre", "Pour beurrer à mort ses ennemis", 3)#nom, description, degat
pelleTarte = Arme("Pelle à tarte", "Utile une fois que vos ennemis sont découpés en tranche", 3)
#etage 2
grilleMarrons = Arme("Grille marrons", "C'est comme une poêle, mais avec des trous dedans", 4)
pressePuree = Arme("Presse-purée", "On a rarement vu moins efficace... A part le couteau a beurre", 4)
#etage 3
ciseauxBoucher = Arme("Ciseaux de boucher", "Pointu et tranchant, juste pas adapaté au combat...", 5)
broche = Arme("Broche", "Enfin une arme digne de ce nom, enfin si on peut appeler ça une arme", 5)
#etage 4
attendrisseur = Arme("Attendrisseur", "C'est fait pour broyer la viande, mais ça peut marcher avec des os", 6)
hachoir = Arme("Hachoir", "Tranche si bien les os et les doigts...", 6)
#etage 5
sabreChamp = Arme("Sabre à champagne", "Normalement, c'est pas prévu pour découper les gens, mais vous trouverez rien d'aussi efficace", 7)


#####ARME CONSOMMABLE
#nom, description, soin, energie, statutRetire, faitRevivre, degat)
pasteque = ArmeConsommable("Pastèque", "Bah c'est un peu lourd. C'est tout", 3,  1)
chaine = ArmeConsommable("Chaine de saucisse", "Au moins vous pourrez manger...", 6, 1)
os = ArmeConsommable("Os à moelle", "Ca a l'avantage d'etre rigide, peut etre meme un peu dur...", 7, 2)
pain = ArmeConsommable("Pain de campagne rassi", "C'est dur, mais pas encore assez...", 4, 2)
meule = ArmeConsommable("Meule de parmesan", "Ca a trop vieilli, impossible à manger, mais on peut frapper avec", 5, 3)
gigot = ArmeConsommable("Gigot d'agneau", "Une belle piece, on peut assomer quelqu'un avec", 8, 3)
jambon = ArmeConsommable("Jambon affiné", "Ca a durci pendant de longs mois, j'espere que ca le sera assez", 9, 4)
tete = ArmeConsommable("Tete de cheval", "Une tete de cheval... Oui c'est glauque!", 6, 4)
mechoui = ArmeConsommable("Méchoui d'agneau", "Parce que se battre avec une patte c'est bien, mais avec l'agneau entier, c'est mieux !!", 10, 5)
espadon = ArmeConsommable("Espadon", "Magnifique poisson !! Son nez éfilé sera redoutable", 7, 5)

#####ARMURE
#nom, description, bloquage
#etage 1
tablier = Armure("Tablier de tissu", "On dirait celui de ma mamie...", 1)
calecon = Armure("Caleçon", "Heureusement, il n'a jamais été porté", 1)
#etage 2
plastron = Armure("Plastron de saucisse", "Je sais pas comment ca peut proteger", 2)
peau = Armure("Peau de porc", "Au moins c'est du beau cuir...", 2)
#etage 3
commode = Armure("Armure", "On a percé des trous pour passer les bras, les jambes et la tete. Mais qui a eu cette idée !?",3)
tonneau = Armure("Tonneau vermoulu", "Un tonneau qui a entierement moisi...", 3)
#etage 4
marmite = Armure("Marmite à bretelles", "Une marmite sans fond maintenues par deux bretelles", 4)
cellophane = Armure("Cellophane", "On a fait pleins de tours, ca tiens chaud, ca pue, mais ca protege un peu", 4)
#etage 5
carcasse = Armure("Carcasse de boeuf", "Alors la, on s'enmbete meme plus a faire des efforts...", 5)
plastronMaille = Armure("Plastron de maille", "La premiere veritable armure que vous voyez depuis le debut de votre aventure", 5)
salopette = Armure("Salopette orange", "Une armure bénie dans la bière", 6)


####COMPETENCE
#competences test
bouleFeu = CompetenceAttaque("boule de feu", 3, "lance une boule de feu", 0, 75,5,True, None)
delugeFeu = CompetenceAttaque("deluge de feu", 2, "embraise les ennemies", 1, 75,5,True, None)
soinMineur = CompetenceHeal("soin mineur", 3, "soigne de facon mineur", 0, 80, 7)
buffAttaque = CompetenceBuff("Encouragement!", 2, "Gueule sur un allié", 0, 85, 4, 0, 0, 0)

#competences hero
coupDeBide = CompetenceAttaque("Coup de bide", 3, "S'élance pour donner un coup de bide à l'ennemie", False, 85, 8, True, None) #nom, cout, description, groupe, tauxReussite, degat, degatFixe
grognement = CompetenceBuff("Grognement", 4, "Lance un énorme grognement qui baisse l'attaque des ennemies", True,75, -2, 0,0,True) # nom, cout, description, groupe, tauxReussite, degatBuff, defenseBuff, agiliteBuff, forEnnemi
tourneeGeneral = CompetenceRecrutement("Tournée général", 5, "Offre une tournée aux ennemies pour avoir une chance en plus de les recruter", True, 75, 10)	#nom, cout, description, groupe, tauxReussite, tauxSupp
tenezUnPeuDeHik = CompetenceBuff("Tenez un peu de hik!", 4, "Offre une tournée de hik aux alliés pour booster leurs attaque", True, 80, 2, 0, 0, False)

coupDeSurin = CompetenceAttaque("Coup de surin", 5, "Surine l'ennemie dans le dos", False, 85, 4, False,None)
affutageDeLaLame = CompetenceBuff("Affutage de la lame", 3, "Le creve-dalle affute sa lame pour plus de degat", False, 85, 4, 0, 0, False)

aTaaable = CompetenceHeal("A taaable!!!", 4, "Une bonne ration pour tout le monde pour regagner de la vie!", True, 85, 10) # nom, cout, description, groupe, tauxReussite, soin
engraissement = CompetenceBuff("Engraissement", 5, "Engraisse les alliés pour les rendre plus résistant", True, 80, 0, 2, 0, False)

paralysePoivrot = Paralyse("Terrifié", 2) #nom, tourRestant
cEstMoiQueTuRegarde = CompetenceStatut("C'est moi que tu regarde?", 4, "Lance un regarde terrifiant qui paralyse les ennemies", True, 65, paralysePoivrot, True) #nom, cout, description, groupe, tauxReussite, statut, forEnnemi
lanceBouteilleVide = CompetenceAttaque("Lancer une bouteille vide", 3, "Lance une bouteille vide sur un ennemie", False, 75, 3, False, None)

#competences ennemie
aTaable = CompetenceHeal("A taaable!!!", 5, "Une bonne ration pour tout le monde pour regagner de la vie!", True, 75, 5) # nom, cout, description, groupe, tauxReussite, soin
endormiSimplet = Endormi("Endormi", 2)	#nom, tourRestant
tuVeuxUneHistoire = CompetenceStatut("Tu veux une histoire?", 2, "Raconte une histoire si ennuyante que tout le monde s'endort...", False, 70, endormiSimplet, True)
zombie = Combattant(Ennemi("Zombie", 10,10,0,0, 3,5,6,2,None,None, None, None, 0), False, False) #Ennemi(nom, PVmax, PV, PCmax, PC, agilite, initiative, attaque, defense, statut, arme, armure, competence, chanceRejoindre), teamHero, isHero

venezAMoi = CompetenceInvocation("Venez à moi!", 7, "invoque deux ignobles zombies", False, 60, zombie)#nom, cout, description, groupe, tauxReussite, invoc
boom = CompetenceAttaque("Boom", 5, "Explose en mille morceau!", True, 90, 15, True, None)

vagueDePeur = CompetenceAttaque("Vague de peur", 5, "Lance une grande vague de peur", True, 65, 5, True, paralysePoivrot)
ralenti = Ralenti("Ralenti", 3)
coupDeGlaire = CompetenceAttaque("Coup de Glaire", 5, "Lance un lourd coup de glaire", False, 80, 6, True, ralenti)
tornadeDeGuerande = CompetenceAttaque("Torande de guérande", 5, "Une tornade de sel", True, 80, 5, True, paralysePoivrot)
empoisonne = Empoisonne("Poison", 3)
odeurInfecte = CompetenceAttaque("Odeur infecte", 5, "Une odeur nauséabonde qui nécrause tout ce qu'il y a autours", True, 80, 7, True, empoisonne)
dort = Endormi("Endormi", 2)
patePiege = CompetenceAttaque("Paté piégé", 5, "Il ne fallait pas se laisser uper par ce formidable paté...", True, 80, 10, True, dort)
coupDeMassue = CompetenceAttaque("Coup de massue", 6, "Un énorme coup de massue d'une puissance impressionnante", False, 80, 18, True, None)

#competence boss
grossePatate = CompetenceAttaque("Grosse patate", 5, "Une grosse patate à la Maïté", False, 80, 5, True, None)
coupDeBouteille = CompetenceAttaque("Coup de bouteille", 5, "Un gros coup de sa précieuse bouteille du chateau de Mont-précieux", False, 85, 7, True, None)
rougeauPourLesCopains = CompetenceHeal("Rougeau pour les copains", 4, "Un petit coup pour les copains pour se revigorer", True, 80, 10)
caaalin = CompetenceAttaque("Caaalin!", 4, "Un gros caaalin d'un cadavre en décomposition <3", False, 85, 10, True, empoisonne)
idiotSandwich = CompetenceAttaque("Idiot sandwich", 5, "Vous prend entre 4 yeux pour vous rappelez à quelle point vous etes nulle", False, 85, 14, True, paralysePoivrot)
obusMagique = CompetenceAttaque("Obus magique", 5, "Tire une boule de feu magique grâce à son magnifique panzer 4!", True, 80, 22, True, paralysePoivrot)

#STATUT
poison = Empoisonne("empoisonné",4)
vomi = CompetenceStatut("vomir",5, "vomit sur un ennemi",0,70,poison, 0)


##### ENNEMIS
#etage 1
grosTas = Ennemi("Gros tas", 10, 10, 0, 0, 6, 8, 5, 2, None, None, None, [aTaable], 10, [pasteque, chaine, tablier, calecon], [20, 15, 15, 15])   #nom, PVmax, PV, PCmax, PC, agilite, initiative, attaque, defense, statut, arme, armure, competence, chanceRejoindre, loot, chancesLoot
vieuxPoivrot = Ennemi("Vieux poivrot", 10, 10, 10,10,8,6,3,2,None, None, None, None, 10, [pasteque, chaine, tablier, calecon], [20, 15, 15, 15])
golemDeGras = Ennemi("Golem de gras", 16, 16, 10, 10, 5, 7, 6, 2,None,None,None, [coupDeGlaire], 10, [couteauBeurre, pelleTarte], [10, 10])

#etage 2
simpletVillage = Ennemi("Simplet du village", 13, 13, 5, 5, 20, 10, 6,1,None,None,None, [tuVeuxUneHistoire], 10, [os, pain, plastron, peau], [19, 14, 14, 14])
cuisinierCannibal = Ennemi("Cuisinier cannibal", 18, 18, 10, 10, 7, 7, 3, 3, None,None,None, None, 10, [os, pain, plastron, peau], [19, 14, 14, 14])
golemDeJambon = Ennemi("Golem de jambon", 20, 20, 10, 10, 5, 8, 7, 3, None,None,None, [tornadeDeGuerande], 10, [grilleMarrons, pressePuree], [10, 10])

#etage 3
pouilleux = Ennemi("Pouilleux", 18, 18, 25, 25, 10, 10, 5, 2, None,None,None, None, 10, [meule, gigot, commode, tonneau], [19, 14, 13, 13])
croqueMort = Ennemi("Croque-mort", 18, 18, 20, 20, 6, 9, 1, 2, None,None,None, [venezAMoi], 10, [meule, gigot, commode, tonneau], [19, 14, 13, 13])
golemDAndouillette = Ennemi("Golemn d'andouillette", 23, 23, 15, 15, 5, 8, 8, 3, None,None,None, [odeurInfecte], 10, [ciseauxBoucher, broche], [10, 10])

#etage 4
boomer = Ennemi("Boomer", 8, 8, 5, 5, 5, 5, 1, 2, None,None,None, [boom], 10, [jambon, tete, marmite, cellophane], [13, 18, 12, 12])
chevalierCasseCroute = Ennemi("Chevalier Casse-croute", 25, 25, 0, 0, 6, 8, 7, 4, None,None,None, None, 10, [jambon, tete, marmite, cellophane], [13, 18, 12, 12])
golemNafnaf = Ennemi("Golem Nafnaf", 30, 30, 15, 15, 5, 8, 8, 4, None,None,None, [patePiege], 10, [attendrisseur, hachoir], [10, 10])

#etage 5
ombreRampante = Ennemi("Ombre rampante", 10,10,10,10, 66, 13, 5, 1, None,None,None, [vagueDePeur], 10, [mechoui, espadon, carcasse, plastronMaille, salopette], [12, 17, 11,11, 10])
psychopate = Ennemi("Psychopathe", 20, 20, 0, 0, 10, 10, 9, 2, None,None,None, None, 10, [mechoui, espadon, carcasse, plastronMaille, salopette], [12, 17, 11, 11, 10])
geant = Ennemi("Geant", 35,35,20,20, 5,9,10,5, None,None,None, [coupDeMassue], 10, sabreChamp, 10)

#special


#boss etage1
maite = Ennemi("Maïte", 20, 20, 20, 20, 7, 20, 6, 3, None,None,None, [grossePatate], 10)
#boss etage2
unParDieux = Ennemi("Un par Dieux", 30,30,5,5, 5, 20, 6, 3, None,None,None, [coupDeBouteille], 10)
deuxParDieux = Ennemi("Deux par Dieux", 15, 15, 10, 10, 6, 20, 8, 3, None,None,None, [rougeauPourLesCopains], 10)
#boss etage 3
jerryLePestifere = Ennemi("Jerry le Pestiféré", 55, 55, 20, 20, 10, 20, 6, 3, None,None,None, [caaalin], 10)
#boss etage 4
ramsayLHysterique = Ennemi("Ramsay l'hystérique", 75, 75, 15, 15, 10, 20, 9, 4, None,None,None, [idiotSandwich], 10)
#boss etage 5
merlinPanzer4 = Ennemi("Merlin et son Panzerkampfwagen IV", 150, 150, 50, 50, 1, 20, 12, 5, None,None,None, [obusMagique], 10)



competences = []
competences.append(delugeFeu)
competences.append(bouleFeu)
competences.append(soinMineur)
competences.append(vomi)
competences.append(buffAttaque)


#####HEROS
Charcutier = Hero("Charcutier", 35, 35, 20, 20, 8, 8, 8, 2, None, None, None, competences)
Pilier = Hero("Pilier", 35, 35, 30, 30, 6, 11, 5, 1, None, None, None, competences)
Creve = Hero("Creve-dalle", 25, 25, 25, 25, 25, 12, 7, 1, None, None, None, competences)
Cuistot = Hero("Cuistot", 35, 35, 30, 30, 6, 7, 4, 2, None, None, None, competences)
Poivrot = Hero("Poivrot", 40, 40, 20, 20, 4, 5, 5, 3, None, None, None, competences)




