from core.Ville import *
from core.Region import *
from core.Route import *
from random import random

INF = 10**15

class Graphe :

    # Constructeurs
    def __init__ ( self, r, nb ) :
        self.region = r
        self.nb_sommets = self.region.getNbVilles()
        self.matrice_adjacence = [INF]*self.nb_sommets
        self.matrice_distances = [INF]*self.nb_sommets
        for i in range ( self.nb_sommets ) :
            self.matrice_adjacence[i] = [INF]*self.nb_sommets
            self.matrice_distances[i] = [INF]*self.nb_sommets
            self.matrice_adjacence[i][i] = 0
            self.matrice_distances[i][i] = 0
            
        self.genere_matrices()
        self.calcule_distances()
        self.best_parcours = []

    # Sous-fonctions du constructeur
    def genere_matrices ( self ) :
        liste_routes = self.region.getRoutes()   
        for r in liste_routes :
            i = r.getVilleA().getNumero()
            j = r.getVilleB().getNumero()
            self.matrice_adjacence[i][j] = r.getLongueur()
            self.matrice_adjacence[j][i] = r.getLongueur()
            self.matrice_distances[i][j] = r.getLongueur()
            self.matrice_distances[j][i] = r.getLongueur()
            
    def calcule_distances ( self ) : # Floyd-Warshall
        for k in range ( self.nb_sommets ) :
            for i in range ( self.nb_sommets ) :
                for j in range ( self.nb_sommets ) :
                    ij = self.matrice_distances[i][j]
                    ik = self.matrice_distances[i][k]
                    kj = self.matrice_distances[k][j]
                    if ( ik + kj < ij ) :
                        self.matrice_distances[i][j] = ik + kj
    
    # Accesseurs
    def sontVoisins ( self, a, b ) :
        return self.matrice_adjacence[a][b] < INF
    
    def getBestParcours ( self ) :
        return self.best_parcours
        
    def setBestParcours ( self, nouveau_parcours ) :
        self.best_parcours = nouveau_parcours
        
    def getDistance ( self, ville_A, ville_B ) :
        return self.matrice_distances[ville_A][ville_B]
        
    def getLongueurParcours ( self, parcours ) :
        longueur = 0
        for i in range ( len(self.best_parcours) - 1 ) :
            longueur += self.getDistance ( parcours[i], parcours[i+1] )
        longueur += self.getDistance ( parcours[ len(self.best_parcours) - 1 ], parcours[0] ) # retour au début
        return longueur 
       
    # Fonctions utilisées pour l'affichage
    def getBestParcoursRoutes ( self ) :
        liste_routes = []
        for i in range ( len(self.best_parcours) - 1 ) :
            a = self.best_parcours[i]
            b = self.best_parcours[i+1]
            if ( self.sontVoisins(a,b) ) :
                liste_routes.append ( self.region.getRoute(a,b) )
            else :
                interm = self.liste_intermediaire(a,b)
                for j in range ( len(interm) - 1 ) :
                    a = interm[j]
                    b = interm[j+1] 
                    liste_routes.append ( self.region.getRoute(a,b) )                
        
        # Retour au point de départ
        a = self.best_parcours[-1]
        b = self.best_parcours[0]
        if ( self.sontVoisins(a,b) ) :
            liste_routes.append ( self.region.getRoute(a,b) )
        else :
            interm = self.liste_intermediaire(a,b)
            for j in range ( len(interm) - 1 ) :
                a = interm[j]
                b = interm[j+1] 
                liste_routes.append ( self.region.getRoute(a,b) )
        return liste_routes
        
    def liste_intermediaire ( self, a, b ) : # Dijkstra
        
        liste_distance = [INF]*self.nb_sommets
        liste_precedents = [-1]*self.nb_sommets
        liste_traites = [False]*self.nb_sommets
        
        liste_distance[a] = 0
        liste_precedents[a] = a
        
        while ( not liste_traites[b] ) :
            sommetATraite = -1
            distMin = 999999999
            for i in range ( self.nb_sommets ) :
                if ( not liste_traites[i] and liste_distance[i] < distMin ) :
                    sommetATraite = i
                    distMin = liste_distance[i]
            liste_traites[sommetATraite] = True
            for i in range ( self.nb_sommets ) :
                if ( not liste_traites[i] and self.sontVoisins(sommetATraite, i) ) : 
                    dist = liste_distance[sommetATraite] + self.matrice_adjacence[sommetATraite][i]
                    if ( dist < liste_distance[i] ) :
                        liste_distance[i] = dist
                        liste_precedents[i] = sommetATraite
                        
        liste = [b]
        actuel = b
        while ( actuel != a ) :
            actuel = liste_precedents[actuel]
            liste.append(actuel)
        liste.reverse()
        return liste
    
    def affiche_matrice ( self ) :
        for i in range ( self.nb_sommets ) :
            for j in range ( self.nb_sommets ) :
                if ( self.matrice[i][j] == INF ) :
                    print ( "INF", end = " " )
                else :
                    print ( int ( self.matrice[i][j] * 100 ) / 100, end = " " )
                print()


