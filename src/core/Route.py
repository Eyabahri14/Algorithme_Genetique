from core.Ville import *

class Route :

    def __init__ ( self, a, b ) :
        self.villeA = a
        self.villeB = b
        self.longueur = self.villeA.distance(self.villeB)
        
    def getVilleA ( self ) :
        return self.villeA
        
    def getVilleB ( self ) :
        return self.villeB
        
    def getLongueur ( self ) :
        return self.longueur

    def getAX ( self ) :
        return self.villeA.getAbscisse()
        
    def getAY ( self ) :
        return self.villeA.getOrdonnee()
        
    def getBX ( self ) :
        return self.villeB.getAbscisse()
        
    def getBY ( self ) :
        return self.villeB.getOrdonnee()