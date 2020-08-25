import bcolors
from deap import creator, tools
from GeneticAlgorithm.StringOperations import string_similarity


def create_individuals(population, individual_to_compute_novelty, is_archive):
    new_population = []
    first = True
    for individual_in_population in population:
        # the individual is excluded from the population (is not excluded if there is more than one copy of it
        # the individual is not excluded from the archive
        if "".join(individual_to_compute_novelty) != "".join(individual_in_population) or (not first) or is_archive:
            new_individual = creator.Individual2("".join(individual_in_population))
            new_individual.fitness.values = (string_similarity("".join(individual_to_compute_novelty),
                                                               "".join(new_individual)),)
            new_population.append(new_individual)
        else:
            first = False
    return new_population


def select(population, individual_to_compute_novelty, archive):
    # select the individuals for evaluation
    # select the most similar to choreography
    new_population = create_individuals(population, individual_to_compute_novelty, False)

    pop_selected = tools.selTournament(new_population, k=4, tournsize=5)
    # select the most similar individuals to choreography in archive U selected before
    arch = create_individuals(archive, individual_to_compute_novelty, True)

    # the whole population is composed by selected individuals and archive
    pop_resulting = pop_selected + arch

    ind_selected = tools.selBest(pop_resulting, 4)
    return ind_selected
