import random

import bcolors
from deap import base, creator, tools
from GeneticAlgorithm import Individual, OperationsWithLetters as Operations , Constants
from GeneticAlgorithm.FileManagement import Archive
from NaoLibs.Common import sendToRobotMultipleMovements as sendToRobot


def evaluate(individual):
    return sum(individual),

def create_choreography():
    IND_SIZE = 10

    toolbox = base.Toolbox()
    creator.create("FitnessMin", base.Fitness, weights=(-1.0,))
    creator.create("Individual", list, fitness=creator.FitnessMin)

    toolbox.register("attribute", random.random)
    toolbox.register("individual", tools.initRepeat, creator.Individual,
                     toolbox.attribute, n=IND_SIZE)
    toolbox.register("population", tools.initRepeat, list, toolbox.individual)
    toolbox.register("mate", tools.cxTwoPoint)
    toolbox.register("mutate", tools.mutGaussian, mu=0, sigma=1, indpb=0.1)
    toolbox.register("select", tools.selTournament, tournsize=3)
    toolbox.register("evaluate", evaluate)

    # print pop
    pop = toolbox.population(n=50)
    CXPB, MUTPB, NGEN = 0.5, 0.2, 40

    fitnesses = map(toolbox.evaluate, pop)

    count_individuals = 0
    for ind, fit in zip(pop, fitnesses):
        if fit > Constants.threshold_f_min:
            count_individuals = count_individuals + 1
        ind.fitness.values = fit


    # Extracting all the fitnesses for max fits
    # fits = [ind.fitness.values[0] for ind in pop]


    # Variable keeping track of the number of generations
    g = 0
    # Begin the evolution
    print(bcolors.BLUE + "initialization" + bcolors.ENDC)


    pop = toolbox.population(n=50)
    CXPB, MUTPB, NGEN = 0.5, 0.2, 40

    # Evaluate the entire population
    fitnesses = map(toolbox.evaluate, pop)
    for ind, fit in zip(pop, fitnesses):
        ind.fitness.values = fit

    for g in range(NGEN):
        # Select the next generation individuals
        offspring = toolbox.select(pop, len(pop))
        # Clone the selected individuals
        offspring = map(toolbox.clone, offspring)

        # Apply crossover and mutation on the offspring
        print offspring
        for child1, child2 in zip(offspring[::2], offspring[1::2]):
            if random.random() < CXPB:
                print "asdfa", str(child1)," - ", str(child2)
                print toolbox.mate(child1, child2)
                print offspring
                del child1.fitness.values
                del child2.fitness.values
        print len(offspring)
        for mutant in offspring:
            if random.random() < MUTPB:
                toolbox.mutate(mutant)
                del mutant.fitness.values

        # Evaluate the individuals with an invalid fitness
        invalid_ind = [ind for ind in offspring if not ind.fitness.valid]
        fitnesses = map(toolbox.evaluate, pop)
        for ind, fit in zip(invalid_ind, fitnesses):
            ind.fitness.values = fit

        # The population is entirely replaced by the offspring
        pop[:] = offspring

    return pop

    # if fitness_function == calculate_fitnesses:
    #     return toolbox.selectTournament(pop)
    # else:
    #     return toolbox.select(pop)


