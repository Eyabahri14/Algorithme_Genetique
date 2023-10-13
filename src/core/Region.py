from core.Ville import *
from core.Route import *

class Region :

    def __init__ ( self, l, h, n ) :
        self.largeur = l
        self.hauteur = h
        self.nbVilles = n
        self.lesVilles = [0] * self.nbVilles
        self.lesRoutes = []
        self.genereVilles()
        self.genereRoutes ( 100 )
    
    def genereVilles ( self ) :
        for i in range ( self.nbVilles ) :
            distMax = 0
            bestVille = Ville(0,0,0)
            for j in range ( 10 ) :
                x = int ( random() * self.largeur * 100 ) / 100
                y = int ( random() * self.hauteur * 100 ) / 100
                v = Ville ( x, y, i )
                distMin = 9999999999999999
                for k in range ( i ) :
                    dist = self.lesVilles[k].distance(v)
                    if ( dist < distMin ) :
                        distMin = dist
                if ( distMin > distMax ) :
                    bestVille = v
                    distMax = distMin
            self.lesVilles[i] = bestVille
            
    def genereRoutes ( self, dist_max ) :
        estIsolee = [True]*self.nbVilles
        for i in range ( self.nbVilles ) :
            for j in range ( i+1, self.nbVilles ) :
                d = self.lesVilles[i].distance ( self.lesVilles[j] )
                if ( d < dist_max ) :
                    self.lesRoutes.append ( Route ( self.lesVilles[i], self.lesVilles[j] ) )
                    estIsolee[i] = False
                    estIsolee[j] = False
        
        for i in range ( self.nbVilles ) :
            if ( estIsolee[i] ) :
                distMin = 9999999999
                bestVille = -1
                for j in range ( self.nbVilles ) :
                    d = self.lesVilles[i].distance( self.lesVilles[j] )
                    if ( i != j and d < distMin ) :
                        distMin = d
                        bestVille = j
                self.lesRoutes.append ( Route ( self.lesVilles[i], self.lesVilles[bestVille] ) )

    def getLargeur ( self ) :
        return self.largeur

    def getHauteur ( self ) :
        return self.hauteur
        
    def getNbVilles ( self ) :
        return self.nbVilles
       
    def getVilles ( self ) :
        return self.lesVilles
        
    def getRoutes ( self ) :
        return self.lesRoutes
        
    def getRoute ( self, villeA, villeB ) :
        for r in self.lesRoutes :
            a = r.getVilleA().getNumero()
            b = r.getVilleB().getNumero()
            if ( a == villeA and b == villeB or a == villeB and b == villeA ) :
                return r
        print ( "Pas de route entre", villeA, villeB )
        return None
    

