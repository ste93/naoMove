import random

import bcolors
from deap import base, creator, tools
from GeneticAlgorithm import Individual, OperationsWithLetters as Operations , Constants
from GeneticAlgorithm.FileManagement import Archive


def calculate_fitnesses(pop, toolbox):
    x = list(map(toolbox.evaluate, pop))
    return x


def calculate_novelty(pop, toolbox):
    list = []
    for x in pop:
        list.append(toolbox.evaluate_hybrid(x, pop, tools,  toolbox))
    return list



def create_choreography():
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
    # create the population
    pop = toolbox.population(n=Constants.population_size)
    print "population done"


    # Evaluate the entire population
    fitnesses = fitness_function(pop, toolbox)
    # print pop
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
    while  g < 100: # max(fits) < 100  can set a max to the fitness, convergence
        # A new generation
        try:
            g = g + 1
            #selection
            # print fitness_function
            # pop = toolbox.select(pop)

            if fitness_function == calculate_fitnesses:
                pop = toolbox.selectTournament(pop)
            else:
                pop = toolbox.select(pop)
                print "novelty"
            # switch function for evaluation
            if count_individuals >= Constants.t_max and fitness_function == calculate_fitnesses:
                fitness_function = calculate_novelty
                # print "switch novelty"
            elif count_individuals <= Constants.t_min and fitness_function == calculate_novelty:
                fitness_function = calculate_fitnesses
                # print "switch fitness"
            # Clone the selected individuals
            offspring = list(map(toolbox.clone, pop))
            # print pop
            # print offspring
            # crossover
            new = []
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

            # Evaluate the individuals with an invalid fitness
            # invalid_ind = [ind for ind in offspring if not ind.fitness.valid]
            offspring = pop + new
            # print offspring
            # print len(offspring)
            fitnesses = fitness_function(offspring, toolbox)
            count_individuals = 0
            for ind, fit in zip(offspring, fitnesses):
                if fit[0] > Constants.threshold_f_min:
                    count_individuals = count_individuals + 1
                    print "higher" , str(ind) ,fit # fii has 2 parts (a,b)
                    # print fit
                ind.fitness.values = fit

            pop[:] = offspring
        except Exception as e:
            print e
    print pop
    if fitness_function == calculate_fitnesses:
        return toolbox.selectTournament(pop)
    else:
        return toolbox.select(pop)


