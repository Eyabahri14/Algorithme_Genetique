import random

# Fonction pour générer des génomes aléatoires
def generate_genomes(n):
    return [[random.randint(1, 5) for _ in range(5)] for _ in range(n)]


# Fonction pour évaluer les génomes et filtrer ceux qui sont dans une plage donnée
def evaluation(genomes, min_sum, max_sum):
    return [genome for genome in genomes if min_sum <= sum(genome) <= max_sum]

# Fonction pour effectuer un croisement sur une liste de génomes
def crossover_all_genomes(genomes):
    new_genomes = []

    for i in range(0, len(genomes), 2):
        parent1 = genomes[i]
        parent2 = genomes[i + 1]

        crossover_point = random.randint(1, len(parent1) - 1)

        child1 = parent1[:crossover_point] + parent2[crossover_point:]
        child2 = parent2[:crossover_point] + parent1[crossover_point:]

        new_genomes.extend([child1, child2])

    return new_genomes


#****************PARTIE TEST **********************
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