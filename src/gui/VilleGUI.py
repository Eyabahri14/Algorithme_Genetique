from core.Ville import *
from tkinter import *

rayon = 2
color = "#0000FF"

class VilleGUI :

    def __init__ ( self, v ) :
        self.ville = v
        
    def affiche ( self, sc ) :
        x1 = self.ville.getAbscisse() - rayon
        y1 = self.ville.getOrdonnee() - rayon
        x2 = self.ville.getAbscisse() + rayon
        y2 = self.ville.getOrdonnee() + rayon
        
        sc.create_oval ( x1, y1, x2, y2, fill=color, outline=color )