import random

import string

def genererPopulation(n):
    population = []
    counts = {}

    alphabet = string.ascii_lowercase

    selected_types = alphabet[:n]

    for char in selected_types:
        count = random.randint(1, 3)
        population.extend([char] * count)
        counts[char] = count

    random.shuffle(population)

    return population, counts


def generate_genomes(people):
    genomes = {}

    for character in people:

        if character not in genomes:
            genome = [random.randint(1, 5) for _ in range(5)]

            genomes[character] = genome

    result = [{'individu': character, 'genomes': genomes[character]} for character in people]

    return result


def somme_genome(genome):
    return sum(genome)


#sélectionne les individus de la population dont la somme de leurs génomes se situe entre min_sum et max_sum.
def selection(population, min_sum, max_sum):
    selected = []

    for individual in population:

        genome = individual['genomes']

        genome_sum = somme_genome(genome)

        if min_sum <= genome_sum <= max_sum:
            selected.append(individual)

    return selected


#prend deux parents, extrait leurs génomes, et effectue un croisement entre eux.
# Les génomes des enfants sont créés en échangeant une partie aléatoire des génomes des parents.
def croisement(parent1, parent2):
    enfant1_genome = parent1['genomes'][:]

    enfant2_genome = parent2['genomes'][:]

    if enfant1_genome != enfant2_genome:
        crossover_point = random.randint(0, len(enfant1_genome) - 1)

        enfant1_genome[crossover_point:], enfant2_genome[crossover_point:] = (

            enfant2_genome[crossover_point:], enfant1_genome[crossover_point:]

        )

    enfant1 = {'individu': parent1['individu'], 'genomes': enfant1_genome}

    enfant2 = {'individu': parent2['individu'], 'genomes': enfant2_genome}

    return enfant1, enfant2


def mutation(individu, mutation_rate):
    mutated_genome = individu['genomes'][:]

    for i in range(len(mutated_genome)):

        if random.random() < mutation_rate:
            mutated_genome[i] = random.randint(1, 5)

    return {'individu': individu['individu'], 'genomes': mutated_genome}





# Génération de la population initiale avec les compteurs

population_initiale, counts = genererPopulation(3)

print(genererPopulation(3))

result = generate_genomes(population_initiale)

print(result)

#print("le nombre total est : ", counts)

#print("Population initiale:")

#print(result)

# Exécution de l'algorithme génétique sur la population initiale pendant un certain nombre de générations

#generations = 100  # Nombre de générations (ajustez selon vos besoins)

#min_sum = 10  # Remplacez par la valeur minimale souhaitée

#max_sum = 20  # Remplacez par la valeur maximale souhaitée

#mutation_rate = 0.1  # Taux de mutation

#for generation in range(generations):
    #algorithme_genetique(result, 1, min_sum, max_sum, mutation_rate)