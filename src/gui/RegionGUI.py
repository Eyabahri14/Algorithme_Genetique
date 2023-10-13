from tkinter import *
from core.Region import *
from gui.GrapheGUI import *

class RegionGUI (Canvas) :

    def __init__ ( self, s, g ) :
        super().__init__()
        self.region = s
        self.graphe = GrapheGUI ( g )
        self.config(width=self.region.getLargeur(), height=self.region.getHauteur())
        
        self.lesVillesGUI = []
        lesVilles = self.region.getVilles()
        for v in lesVilles :
            self.lesVillesGUI.append ( VilleGUI(v) )
        
        self.lesRoutesGUI = []
        lesRoutes = self.region.getRoutes()
        for r in lesRoutes :
            self.lesRoutesGUI.append ( RouteGUI(r) )
        
        
    def affiche ( self ) :

        for r in self.lesRoutesGUI :
            r.affiche ( self )
            
        self.graphe.affiche_parcours(self)
            
        for v in self.lesVillesGUI :
            v.affiche ( self )

    