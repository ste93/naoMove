import random
import time

import bcolors
from deap import base, creator, tools
from GeneticAlgorithm import Individual, OperationsWithLetters as Operations , Constants
from GeneticAlgorithm.FileManagement import Archive


def calculate_fitnesses(ind, pop, toolbox):
    try:
        return toolbox.evaluate(ind)
    except Exception as e:
        print "fitness"
        print e


def calculate_novelty(ind, pop, toolbox):
    try:
        return toolbox.evaluate_hybrid(ind, pop, tools,  toolbox)
    except Exception as e:
        print "novelty"
        print e


def print_pop(pop):
    for x in pop:
        print x, x.fitness.values


def create_choreography(number_of_generations):
    Archive.clearArchive()
    # initialization
    fitness_function = calculate_novelty
    creator.create("FitnessMax", base.Fitness, weights=(1.0, 1.0))
    creator.create("Individual", list, fitness=creator.FitnessMax)
    toolbox = base.Toolbox()
    toolbox.register("individual", tools.initIterate, creator.Individual, Individual.init_individual)
    toolbox.register("population", tools.initRepeat, list, toolbox.individual)
    toolbox.register("evaluate", Operations.calculate_fitness)
    toolbox.register("evaluate_hybrid", Operations.calculate_fitness_and_novelty)
    toolbox.register("mutate", Operations.mutation)
    toolbox.register("mate", tools.cxTwoPoint)
    toolbox.register("select", tools.selSPEA2, k=100)
    toolbox.register("selectTournament", tools.selTournament, k=100, tournsize = 5)
    toolbox.register("select10", tools.selSPEA2, k=10)
    toolbox.register("selectTournament10", tools.selTournament, k=10, tournsize = 5)

    # begins the counter of individuals with fitness over threshold over to 0
    count_individuals = 0

    # create the population
    pop = toolbox.population(n=Constants.population_size)
    print "population done"

    # Begin the evolution
    print(bcolors.BLUE + "initialization" + bcolors.ENDC)
    for g in range(number_of_generations):

        # A new generation
        print "generation", g

        # switch function for evaluation
        if count_individuals >= Constants.t_max and fitness_function == calculate_fitnesses:
            fitness_function = calculate_novelty
        elif count_individuals <= Constants.t_min and fitness_function == calculate_novelty:
            fitness_function = calculate_fitnesses

        # Clone the selected individuals
        offspring = list(map(toolbox.clone, pop))

        # new individuals of the population
        new = []

        # crossover
        for child1, child2 in zip(offspring[::2], offspring[1::2]):
            if random.random() < Constants.CXPB:
                a,b = toolbox.mate(child1, child2)
                new.append(a)
                new.append(b)
                del child1.fitness.values
                del child2.fitness.values

        # mutation
        for mutant in offspring:
            if random.random() < Constants.MUTPB:
                c, = toolbox.mutate(mutant)
                new.append(c)
                del mutant.fitness.values

        # create the new offspring with old population and new individuals
        offspring = pop + new

        # evaluate the individuals
        count_individuals = 0
        for ind in offspring:
            ind.fitness.values = fitness_function(ind, pop, toolbox)
            if ind.fitness.values[0] > Constants.threshold_f_min:
                count_individuals = count_individuals + 1
        pop[:] = offspring

        # selection
        if fitness_function == calculate_fitnesses:
            pop = toolbox.selectTournament(pop)
        else:
            pop = toolbox.select(pop)

    if fitness_function == calculate_fitnesses:
        return toolbox.selectTournament10(pop)
    else:
        return toolbox.select10(pop)
