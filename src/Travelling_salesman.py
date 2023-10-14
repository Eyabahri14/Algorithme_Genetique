from core.Region import *
from core.Graphe import *
from gui.MainWindow import *
from Solution import generate_genomes, evaluation, crossover_all_genomes
import random

# Paramètres du problème
w = 800
h = 600
nb_villes = 100

# Génération du problème
r = Region(w, h, nb_villes)

# Graphe du problème
g = Graphe(r, nb_villes)

# Génération de 5 génomes aléatoires
genomes = generate_genomes(5)

# Évaluation des génomes dans la plage [10, 20]
filtered_genomes = evaluation(genomes, 10, 20)

# Application du croisement sur les génomes évalués
new_genomes = crossover_all_genomes(filtered_genomes)

# Affichage des résultats
print("Génomes générés :")
for genome in genomes:
    print(genome)

print("\nGénomes évalués dans la plage [10, 20] :")
for genome in filtered_genomes:
    print(genome)

print("\nNouveaux génomes après le croisement :")
for genome in new_genomes:
    print(genome)

# Définir la meilleure solution
g.setBestParcours([0, 1, 2])

# Affichage du résultat
print("Distance finale :", int(g.getLongueurParcours(g.getBestParcours())), "kilomètres")
fenetre = MainWindow(r, g)
fenetre.loop()
