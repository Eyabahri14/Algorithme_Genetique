from gui.RegionGUI import *
from tkinter import *

class MainWindow :

    def __init__ ( self, s, g ) :
        self.fenetre = Tk()
        self.fenetre.title("Voyageur de commerce")
        self.widget_scene = RegionGUI( s, g )	
        
    def loop ( self ) :
        self.widget_scene.affiche()
        self.widget_scene.pack()
        self.fenetre.mainloop()