from core.Region import *
from core.Graphe import *
from gui.MainWindow import *
import random

# Paramètres du problème
w = 800
h = 600
nb_villes = 100

# Génération du problème
r = Region ( w, h, nb_villes )

# Graphe du problème
g = Graphe ( r, nb_villes )
#print(g.matrice_distances)
# Insérer votre code ici
""" Mise en place de l'algorithme génétique
    Création d'une population d'individus
    Théoriquement le génome correspond à la succession des villes dans le circuit
    Ici la population est l'ensemble des circuits générés par l'algorithme    
"""
class Individu:
    # nombre_genes: ici nombre de villes dans le circuit
    def __init__(self,nombre_genes,distances):
        self.fitness = 0.0
        self.distance = 0
        self.genes = []
        # les distances entre les villes sont contenues dans une matrice renseignées par la classe Region
        self.distances = distances
        #print(self.distances)
        self.nombre_genes = nombre_genes
        #génére le génome de l'individu: ici le circuit aléatoire
        self.genere_genome()
        #on calcule dans la foulée le fitness du génome : c'est l'inverse de la distance totale du circuit
        self.setFitness()
    def genere_genome(self):
        #attention: il faut modifier cette partie du code afin que le genome contienne des genes tous différents les ine sde autes
        f = list(range(0, self.nombre_genes))
        for v in range(self.nombre_genes):
            val = random.choice(f)
            f.remove(val)
            self.genes.append(val)
    """fitness donne la qualité de notre individu ici le circuit
    pour être de qualité, il doit minimiser la distance totale du voyage"""
    def getGenome(self):
        return self.genes
    def setFitness(self):
        self.calculeFitness()

    def calculeFitness(self):
        #on calcule la distance totale du circuit
        self.setDistance()
        if self.fitness == 0:
            self.fitness = 1 / float(self.getDistance())
        #print(self.fitness)
    def getFitness(self):
        return self.fitness
    def setDistance(self):
        self.calculeDistance()

    def calculeDistance(self):
        #a correspond au numero de la ville 1, b au numéro de la ville 2
        a = self.genes[0]
        dist = 0
        for b in self.genes[1:]:
            min = 0
            max = 0
            if a > b:
                min = b
                max = a
            else:
                min = a
                max = b
            dist = dist + (self.distances[min])[max - min - 1]

            a = b
        self.distance = dist
    def getDistance(self):
        self.calculeDistance()
        return self.distance

    def getGene(self, genePosition):
        return self.genes[genePosition]

    def setGene(self, genePosition, gene):
        self.genes[genePosition] = gene
        self.fitness = 0.0
        self.distance = 0
    def __len__(self):
        return len(self.genes)

    def __getitem__(self, index):
        return self.genes[index]

    def __setitem__(self, key, value):
        self.genes[key] = value

    def tailleGenome(self):
        return len(self.genes)
    #ici les genes sont les numéros des villes
    def contientGene(self, gene):
        return gene in self.genes


""" on crée la classe Population (ensemble d'individus), qui représente 
ici un ensemble des circuits ou voyages
"""
class Population:
    def __init__(self, nombre_genes, taillePopulation,distances,init):
        # taillePopulation est le nombre de circuits
        self.taillePopulation = taillePopulation
        self.individus = []
        self.distances = distances
        for i in range(0, taillePopulation):
            self.individus.append(None)
        # si init est true, c'est la première génération
        if init:
            for i in range(0, taillePopulation):
                nouvelIndividu = Individu(nombre_genes, self.distances)
                self.addIndividu( i, nouvelIndividu)

    def addIndividu(self, index, individu):
        self.individus[index] = individu

    def getIndividu(self, index):
        return self.individus[index]

    def getFittest(self):
        fittest = self.individus[0]
        for i in range(0, self.getTaillePopulation()):
            if fittest.getFitness() <= self.getIndividu(i).getFitness():
                fittest = self.getIndividu(i)
        return fittest

    def __setitem__(self, key, value):
        self.individus[key] = value

    def __getitem__(self, index):
        return self.individus[index]

    def getTaillePopulation(self):
        return len(self.individus)

"""création d'une classe qui contient les principales étapes d'un algorithme génétique
"""
class AlgoGen:
    def __init__(self,distances,nbGenesParIndividu):
        self.distances = distances
        self.nbGenesParIndividu = nbGenesParIndividu
        """tauxMutation est la probabilité qu'un gène subisse une mutation
        ici la mutation modèlisera l'inversion de la position de deux villes dans le circuit
        c'est un taux faible car obtenir une distance plus faible en inversant deux villes
        à une probabilité faible
        """
        self.tauxMutation = 0.015
        """
        tailleTournoi : la taille des poules de notre tournoi
        
        Types de selection:
        Selection par tournoi:
        Fait affronter plusieurs individus selectionnés au hasard (ici la taille du tournoi est de 5 individus)
        Nous gardons l'individu avec le fitness le plus fort
        Avantage: laisse une chance à un mauvais individu d'être selectionné s'il gagne le tournoi
        
        
        Sélection par roulette:
        probabilité qu’un individu soit sélectionné est proportionnelle à sa fitness
        inconvénient: si la distribution des fitness n’est pas très uniforme, alors, certains circuits risquent d’être très fréquemment sélectionnés (ceux avec une faible distance) au détriment d’autres circuits (ceux avec grande distance)
        on veut pourtant reproduire même les mauvaits circuits (contrairement à la selection naturelle...)
        
        Selection par rang:
        ordonner les individus (ici les circuits) en fonction de leur fitness
        Donc probabilité d’être sélectionné est cette fois proportionnelle au rang de l’individu, et non à sa fitness
        inconvénient: Si la population a peu de bons individus, la vitesse de convergence peut être lente car on fera reproduire beaucoup de mauvais individus
        """
        self.tailleTournoi = 5
        """
        Elitisme: attribut qui correspond au fait de vouloir conserver les meilleurs individus d’une génération à une autre, afin d’être sûr de ne pas les perdre
        avantage: accélérer la convergence de l’algorithme au détriment de la diversité des individus
        Il y a plusieurs sortes d'élitisme:
        1. Copier les n meilleurs individus dans la nouvelle génération
        2. Sélectionner les n meilleurs individus pour qu'ils se reproduisent
        Ici on choisit le 1. avec un seul individu
        """
        self.elitisme = True

    def evoluerPopulation(self, pop):
        nouvellePopulation = Population(self.nbGenesParIndividu,pop.taillePopulation,self.distances,False)
        elitismeOffset = 0
        if self.elitisme:
            nouvellePopulation.addIndividu(0,pop.getFittest())
            elitismeOffset = 1

        for i in range(elitismeOffset, nouvellePopulation.getTaillePopulation()):
            parent1 = self.selectionTournoi(pop)
            parent2 = self.selectionTournoi(pop)
            enfant = self.crossover(parent1, parent2)
            nouvellePopulation.addIndividu(i, enfant)

        for i in range(elitismeOffset, nouvellePopulation.getTaillePopulation()):
            self.muter(nouvellePopulation.getIndividu(i))

        return nouvellePopulation

    def crossover(self, parent1, parent2):
        enfant = Individu(self.nbGenesParIndividu,self.distances)
        # méthode à deux coupures
        startPos = int(random.random() * parent1.tailleGenome())
        endPos = int(random.random() * parent1.tailleGenome())

        for i in range(0, enfant.tailleGenome()):
            if startPos < endPos and i > startPos and i < endPos:
                enfant.setGene(i, parent1.getGene(i))
            elif startPos > endPos:
                if not (i < startPos and i > endPos):
                    enfant.setGene(i, parent1.getGene(i))

        for i in range(0, parent2.tailleGenome()):
            if not enfant.contientGene(parent2.getGene(i)):
                for ii in range(0, enfant.tailleGenome()):
                    if enfant.getGene(ii) == None:
                        enfant.setGene(ii, parent2.getGene(i))
                        break

        return enfant

    def muter(self, individu):
        for genomePos1 in range(0, individu.tailleGenome()):
            if random.random() < self.tauxMutation:
                genomePos2 = int(individu.tailleGenome() * random.random())

                gene1 = individu.getGene(genomePos1)
                gene2 = individu.getGene(genomePos2)

                individu.setGene(genomePos2, gene1)
                individu.setGene(genomePos1, gene2)

    def selectionTournoi(self, pop):
        tournoi = Population(self.nbGenesParIndividu,self.tailleTournoi,self.distances, False)
        for i in range(0, self.tailleTournoi):
            randomId = int(random.random() * pop.getTaillePopulation())
            tournoi.addIndividu(i, pop.getIndividu(randomId))
        fittest = tournoi.getFittest()
        return fittest

"""on initialise la population avec 50 individu"""
population = Population(nb_villes,50,g.matrice_distances,True)
print ("Distance initiale : " + str(population.getFittest().getDistance()))
meilleurIndividu=population.getFittest()
print("Solution initiale non optimisée : " + str(meilleurIndividu.getGenome()))
print ("Distance initiale : " , float(g.getLongueurParcours(meilleurIndividu.getGenome())))

g.setBestParcours ( [ 0, 1, 2 ] )
# On fait avancer notre population sur 200 generations

algoGen = AlgoGen(g.matrice_distances,nb_villes)
population = algoGen.evoluerPopulation(population)
meilleurIndividu = population.getFittest()
bestParcours = float(g.getLongueurParcours(meilleurIndividu.getGenome()))
bestParcoursSansAlg = int(g.getLongueurParcours(g.getBestParcours()))
#for i in range(0, 1000):
cpt = 100
while(bestParcours>bestParcoursSansAlg):
    for i in range(0, 200):
        population = algoGen.evoluerPopulation(population)
    meilleurIndividu = population.getFittest()
    bestParcours = g.getLongueurParcours(meilleurIndividu.getGenome())
    cpt = cpt + 1

# Affichage du résultat

print("Solution finale optimisée : " + str(meilleurIndividu.getGenome()))
print("Distance finale optimisé avec l' algorithme : " , float(g.getLongueurParcours(meilleurIndividu.getGenome())))
print ( "Distance finale non optimisé:", int(g.getLongueurParcours(g.getBestParcours())), "kilomètres" )
print ("Il a fallu ",cpt, " générations pour que la distance calculé à l'aide de l'algorithme soit inférieur à celle calculé sans")
fenetre = MainWindow( r, g )
fenetre.loop()
