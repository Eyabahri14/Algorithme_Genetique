from core.Graphe import *
from gui.VilleGUI import *
from gui.RouteGUI import *

color_parcours = "#FF0000"

class GrapheGUI :

    def __init__ ( self, g ) :
        self.graphe = g

    def affiche_parcours ( self, sc ) :
        liste_routes = self.graphe.getBestParcoursRoutes()
        for r in liste_routes :
            if r != None :
                ax = r.getAX()
                ay = r.getAY()
                bx = r.getBX()
                by = r.getBY()
                sc.create_line ( ax, ay, bx, by, fill=color_parcours )
            else :
                print ( "Route inexistante" )