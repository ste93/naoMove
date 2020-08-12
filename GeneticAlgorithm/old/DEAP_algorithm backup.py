import random
import time

import bcolors
from deap import base, creator, tools
from GeneticAlgorithm import Individual, OperationsWithLetters as Operations , Constants
from GeneticAlgorithm.FileManagement import Archive


def calculate_fitnesses(ind, pop, toolbox, repertoirePath):
    try:
        return toolbox.evaluate(ind, repertoirePath)
    except Exception as e:
        print "fitness"
        print e


def calculate_novelty(ind, pop, toolbox, repertoirePath):
    try:
        return toolbox.evaluate_hybrid(ind, pop, repertoirePath)
    except Exception as e:
        print "novelty"
        print e


def print_pop(pop):
    for x in pop:
        print x, x.fitness.values


# evaluation_method: 0 fitness, 1 novelty, 2 both
# def create_choreography(number_of_generations):
def create_choreography(number_of_generations, evaluation_method, repertoirePath):
    Archive.clearArchive()

    # initialization
    fitness_function = calculate_fitnesses
    if evaluation_method == 1:
        fitness_function = calculate_novelty
    creator.create("FitnessMax", base.Fitness, weights=(1.0, -1.0))
    creator.create("Individual", list, fitness=creator.FitnessMax)
    toolbox = base.Toolbox()
    toolbox.register("individual", tools.initIterate, creator.Individual, Individual.init_individual)
    toolbox.register("population", tools.initRepeat, list, toolbox.individual)
    toolbox.register("evaluate", Operations.calculate_fitness)
    toolbox.register("evaluate_hybrid", Operations.calculate_fitness_and_novelty)
    toolbox.register("mutate", Operations.mutation)
    toolbox.register("mate", tools.cxTwoPoint)
    toolbox.register("select", tools.selNSGA2, k=Constants.population_size)
    # toolbox.register("select", tools.selSPEA2, k=Constants.population_size)
    toolbox.register("selectTournament", tools.selTournament, k=Constants.population_size, tournsize = 5)
    toolbox.register("select10", tools.selNSGA2, k=10)
    # toolbox.register("select10", tools.selSPEA2, k=10)
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
        if evaluation_method == 2:
            if count_individuals >= Constants.t_max and fitness_function == calculate_fitnesses:
                fitness_function = calculate_novelty
            elif count_individuals <= Constants.t_min and fitness_function == calculate_novelty:
                fitness_function = calculate_fitnesses

        # Clone the selected individuals
        offspring = list(map(toolbox.clone, pop))

        # new individuals of the population
        new = []

        # crossover
        i = 0
        for child1, child2 in zip(offspring[::2], offspring[1::2]):
            # if random.random() < Constants.CXPB:
            i = i+2
            if i < 90:
                a,b = toolbox.mate(child1, child2)
                new.append(a)
                new.append(b)
                del child1.fitness.values
                del child2.fitness.values

        # mutation
        for mutant in new:
            if random.random() < Constants.MUTPB:
                print mutant
                c, = toolbox.mutate(mutant)
                print mutant
                new.append(c)
                del mutant.fitness.values

        # create the new offspring with old population and new individuals
        offspring = pop + new

        # evaluate the offspring
        count_individuals = 0
        for ind in offspring:
            # print fitness_function
            ind.fitness.values = fitness_function(ind, pop, toolbox, repertoirePath)
            # print ind, ind.fitness.values
            if ind.fitness.values[0] > Constants.threshold_f_min:
                count_individuals = count_individuals + 1

        # selection
        if evaluation_method == 2:
            if fitness_function == calculate_fitnesses:
                pop = toolbox.selectTournament(offspring)
            else:
                pop = toolbox.select(offspring)
                # print "selection novelty"
        elif evaluation_method == 1:
            pop = toolbox.select(offspring)
        else:
            pop = toolbox.selectTournament(offspring)

    if evaluation_method == 2:
        if fitness_function == calculate_fitnesses:
            return toolbox.selectTournament10(pop)
        else:
            return toolbox.select10(pop)
    elif evaluation_method == 1:
        return toolbox.select10(pop)
    else:
        return toolbox.selectTournament10(pop)
