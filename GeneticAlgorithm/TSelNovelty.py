from deap import base, creator, tools
from GeneticAlgorithm import Individual , Constants
from GeneticAlgorithm.StringOperations import string_similarity


def create_individuals(population, toolbox, individual_to_compute_novelty):
    new_population = []
    for individual_in_population in population:
        new_individual = toolbox.individual2()
        new_individual.movesList = individual_in_population
        new_individual.fitness.values = (string_similarity(str(individual_to_compute_novelty),
                                                           str(new_individual.movesList)),)
        new_population.append(new_individual)
    return new_population


def select(population, individual_to_compute_novelty, archive):
    # initialization
    creator.create("FitnessMax2", base.Fitness, weights=(1.0,))
    creator.create("Individual2", list, fitness=creator.FitnessMax2)
    toolbox2 = base.Toolbox()
    toolbox2.register("individual2", tools.initIterate, creator.Individual2, Individual.init_individual)

    # select the individuals for evaluation
    # select the most similar to choreography
    new_population = create_individuals(population, toolbox2, individual_to_compute_novelty)
    pop_selected = tools.selTournament(new_population, k=4, tournsize=5)

    # select the most similar individuals to choreography in archive U selected before
    arch = create_individuals(archive, toolbox2, individual_to_compute_novelty)

    # the whole population is composed by selected individuals and archive
    pop_resulting = pop_selected + arch
    # r is the number of individuals to select
    r = min(len(archive), Constants.max_arch)

    # those are the most similar individuals
    ind_selected = tools.selBest(pop_resulting, k=r)

    return ind_selected
