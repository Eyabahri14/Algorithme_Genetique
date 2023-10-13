from random import *
from math import *

class Ville :

    def __init__ ( self, x, y, n ) :
        self.numero = n
        self.abscisse = x
        self.ordonnee = y

    def getNumero ( self ) :
        return self.numero

    def getAbscisse ( self ) :
        return self.abscisse

    def getOrdonnee ( self ) :
        return self.ordonnee

    def affiche ( self ) :
        print ( "(", self.abscisse, ";", self.ordonnee, ")" )

    def distance ( self, autre ) :
        dx = self.abscisse - autre.getAbscisse()
        dy = self.ordonnee - autre.getOrdonnee()
        return sqrt ( dx*dx + dy*dy )
