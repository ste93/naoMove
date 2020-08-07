import bcolors
from deap import base, creator, tools
from GeneticAlgorithm import Individual, Constants
from GeneticAlgorithm.StringOperations import string_similarity


def evaluate_ind(new_individual, individual_to_compute_novelty):
    new_individual.fitness.values = (string_similarity("".join(individual_to_compute_novelty),
                                                       "".join(new_individual)),)


def create_individuals(population, creator, individual_to_compute_novelty):
    new_population = []
    for individual_in_population in population:
        # print "".join(individual_in_population), "".join(individual_to_compute_novelty)
        # if "".join(individual_to_compute_novelty) != "".join(individual_in_population):
        new_individual = creator.Individual2(individual_in_population)
        # new_individual.
        # fitness.values = (string_similarity("".join(individual_to_compute_novelty),
        #                                                    "".join(new_individual.movesList)),)
        # print new_individual.fitness.values
        new_population.append(new_individual)
        # else:
        #     i = i + 1
        # if i > 0:
        #     print "else",i
    return new_population


def select(population, individual_to_compute_novelty, archive):
    # initialization
    creator.create("FitnessMax2", base.Fitness, weights=(1.0,))
    creator.create("Individual2", list, fitness=creator.FitnessMax2)
    toolbox2 = base.Toolbox()
    # toolbox2.register("individual2", tools.initIterate, creator.Individual2, Individual.fill_individual)
    toolbox2.register("evaluate", evaluate_ind)

    # select the individuals for evaluation
    # select the most similar to choreography
    new_population = create_individuals(population, creator, individual_to_compute_novelty)

    for x in new_population:
        evaluate_ind(x, individual_to_compute_novelty)
    pop_selected = tools.selTournament(new_population, k=4, tournsize=10)

    # select the most similar individuals to choreography in archive U selected before
    arch = create_individuals(archive, creator, individual_to_compute_novelty)
    # print bcolors.OKMSG + "".join(individual_to_compute_novelty) + bcolors.ENDC
    for x in arch:
        evaluate_ind(x, individual_to_compute_novelty)

    # the whole population is composed by selected individuals and archive
    pop_resulting = pop_selected + arch
    # pop_resulting = new_population + arch

    # those are the most similar individuals

    # for ind in pop_resulting:
    #     print "".join(ind), ind.fitness.values, ind.fitness.valid
    # print bcolors.ERRMSG  + "ind selected" + bcolors.ENDC
    ind_selected = tools.selBest(pop_resulting, 4, fit_attr='fitness')

    # for ind in ind_selected:
    #     print "".join(ind), string_similarity("".join(ind), "".join(individual_to_compute_novelty))
    return ind_selected
