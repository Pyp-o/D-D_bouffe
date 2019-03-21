from Arme import *
from Consommable import *

class ArmeConsommable(Arme, Consommable):
    def __init__(self,nom, description, soin, energie, statutRetire, faitRevivre, degat):
        Arme.__init__(self,nom, description,degat)
        Consommable.__init__(self,nom, description, soin, energie, statutRetire, faitRevivre)
