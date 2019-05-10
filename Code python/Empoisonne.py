# -*- coding: utf-8 -*-

from Statut import *

class Empoisonne(Statut):
    def __init__(self, nom, tourRestant):
        Statut.__init__(self,nom, tourRestant)
    
    def activerStatut(self, combattant):
        self.setTourRestant(self.getTourRestant()-1)
        degat = int(combattant.getPVmax() * 0.1)
        newPV = combattant.getPV() - degat
        combattant.setPV(newPV)
        print("Le poison a infliger " + str(degat) + " point de dégat à " + combattant.getNom())
        if(combattant.getPV() <= 0):
            print("Le poison a finalement eu raison de lui...")
        if (self.getTourRestant()==0):
            self.retirerStatut(combattant)        
        
    def retirerStatut(self, combattant):
        print(combattant.getNom()+" n'est plus empoisonné")
        combattant.retirerStatut(self)
