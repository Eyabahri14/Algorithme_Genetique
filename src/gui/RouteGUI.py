from core.Route import *
from tkinter import *

color = "#008800"

class RouteGUI :

    def __init__ ( self, r ) :
        self.route = r
        
    def affiche ( self, sc ) :
        ax = self.route.getAX()
        ay = self.route.getAY()
        bx = self.route.getBX()
        by = self.route.getBY()
        
        sc.create_line ( ax, ay, bx, by, fill=color )
    
