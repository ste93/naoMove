import random
import time

import bcolors
from deap import base, creator, tools
from GeneticAlgorithm import Individual, OperationsWithLetters as Operations , Constants
from GeneticAlgorithm.FileManagement import Archive


def init_individual():
    moves_list = []
    for _ in range(Constants.number_of_moves):
            move = random.choice(Constants.list_of_moves.keys())
            moves_list.append(move)
    return moves_list


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
        print "".join(x), x.fitness.values


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
    toolbox.register("individual", tools.initIterate, creator.Individual, init_individual)
    toolbox.register("population", tools.initRepeat, list, toolbox.individual)
    toolbox.register("evaluate", Operations.calculate_fitness)
    toolbox.register("evaluate_hybrid", Operations.calculate_fitness_and_novelty)
    toolbox.register("mutate", Operations.mutation)
    toolbox.register("mate", tools.cxTwoPoint)
    toolbox.register("select", tools.selNSGA2, k=Constants.population_size / 10)
    # toolbox.register("select10", tools.selSPEA2, k=Constants.population_size / 10)
    toolbox.register("selectTournament", tools.selTournament, k=Constants.population_size / 10, tournsize = 5)

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

        # evaluate the offspring
        count_individuals = 0
        for ind in pop:
            # print fitness_function
            ind.fitness.values = fitness_function(ind, pop, toolbox, repertoirePath)
            # print ind, ind.fitness.values
            if ind.fitness.values[0] > Constants.threshold_f_min:
                count_individuals = count_individuals + 1
        # print_pop(pop)
        print len(pop)

        # selection
        if evaluation_method == 2:
            if fitness_function == calculate_fitnesses:
                parents = toolbox.selectTournament(pop)
            else:
                parents = toolbox.select(pop)
                # print "selection novelty"
        elif evaluation_method == 1:
            parents = toolbox.select(pop)
        else:
            parents = toolbox.selectTournament(pop)

        # Clone the selected individuals
        offspring = list(map(toolbox.clone, parents))
        print len(offspring)

        # new individuals of the population
        new = []

        # crossover
        i = 0
        # for child1, child2 in zip(offspring[::2], offspring[1::2]):
        for child1 in offspring:
            for child2 in offspring:
                if i < Constants.population_size * 9 / 10 and "".join(child1) != "".join(child2):
                    child1_copy = toolbox.clone(child1)
                    child2_copy = toolbox.clone(child2)
                    a,b = toolbox.mate(child1_copy, child2_copy)
                    new.append(a)
                    new.append(b)
                    i = i + 2

        # mutation
        for mutant in new:
            if random.random() < Constants.MUTPB:
                toolbox.mutate(mutant)
                del mutant.fitness.values
        # create the new offspring with old population and new individuals
        pop = parents  + new

    for ind in pop:
        # print fitness_function
        ind.fitness.values = fitness_function(ind, pop, toolbox, repertoirePath)
        # print ind, ind.fitness.values
        if ind.fitness.values[0] > Constants.threshold_f_min:
            count_individuals = count_individuals + 1

    print_pop(pop)

    if evaluation_method == 2:
        if fitness_function == calculate_fitnesses:
            return toolbox.selectTournament(pop)
        else:
            return toolbox.select(pop)
    elif evaluation_method == 1:
        return toolbox.select(pop)
    else:
        return toolbox.selectTournament(pop)