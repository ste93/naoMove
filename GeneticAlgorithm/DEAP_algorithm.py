import random

import bcolors
from deap import base, creator, tools
from GeneticAlgorithm import OperationsWithLetters as Operations , Constants
from GeneticAlgorithm.Evaluation.Evaluation import compute_ncd
from GeneticAlgorithm.Evaluation.RitchieParameters import compute_criterion_1,compute_criterion_2
from GeneticAlgorithm.FileManagement import FileManagement
from JsonEditor import jsonEditor
from Mathematical.plot2d import plot2d_fit_nov, plot2d, plot2d_2_series, plot2d_no_lim


def calculate_fitnesses(ind, pop, toolbox, parameters):
    try:
        return toolbox.evaluate(ind, parameters)
    except Exception as e:
        print "fitness"
        print e


def calculate_novelty(ind, pop, toolbox, parameters):
    try:
        return toolbox.evaluate_hybrid(ind, pop, parameters)
    except Exception as e:
        print "novelty"
        print e


def print_pop(pop):
    for x in pop:
        print "".join(x), x.fitness.values


# evaluation_method: 0 fitness, 1 novelty, 2 both
# def create_choreography(number_of_generations):
# def create_choreography(parameters, number_of_generations, evaluation_method, repertoirePath):
def create_choreography(parameters):
    random.seed(parameters.random_seed)
    FileManagement.clearArchive()
    FileManagement.initres(parameters.full_name)

    # initialization
    fitness_function = calculate_fitnesses
    if parameters.evaluation_method_index == 1:
        fitness_function = calculate_novelty
    creator.create("FitnessMax2", base.Fitness, weights=(1.0,))
    creator.create("Individual2", list, fitness=creator.FitnessMax2)
    creator.create("FitnessMax", base.Fitness, weights=(1.0, 1.0))
    creator.create("Individual", list, fitness=creator.FitnessMax)
    toolbox = base.Toolbox()
    toolbox.register("individual", tools.initIterate, creator.Individual, Operations.init_individual)
    toolbox.register("population", tools.initRepeat, list, toolbox.individual)
    toolbox.register("evaluate", Operations.calculate_fitness)
    toolbox.register("evaluate_hybrid", Operations.calculate_fitness_and_novelty)
    toolbox.register("mutate", Operations.mutation)
    toolbox.register("mate", tools.cxTwoPoint)
    toolbox.register("selectnsga2", tools.selNSGA2, k=Constants.population_size / 10)
    toolbox.register("selectspea2", tools.selSPEA2, k=Constants.population_size / 10)
    toolbox.register("selectTournament", tools.selTournament, k=Constants.population_size / 10, tournsize = 5)
    # begins the counter of individuals with fitness over threshold over to 0
    count_individuals = 0
    repertoire_string = ""
    for x in FileManagement.getRepertoireWithPath(parameters.repertoire_path)["repertoire"]:
        repertoire_string = repertoire_string + "".join(x["choreo"])
    print repertoire_string

    full_ncd_results = {}
    criterion_1 = {}
    criterion_2 = {}
    fitnesses_avg = {}
    novelty_avg = {}
    archive_size = {}

    # create the population
    pop = toolbox.population(n=Constants.population_size)
    print "population done"


    # Begin the evolution
    g = 0
    # print(bcolors.BLUE + "initialization" + bcolors.ENDC)
    print "initialisation"
    generations = []
    for g in range(parameters.number_of_generations):
    # while g < parameters.number_of_generations or (fitness_function == calculate_fitnesses and not parameters.evaluation_method_index == 0):
        # A new generation
        g = g + 1
        print "generation", g

        # switch function for evaluation
        if parameters.evaluation_method_index == 2:
            if count_individuals >= Constants.t_max and fitness_function == calculate_fitnesses:
                fitness_function = calculate_novelty
            elif count_individuals <= Constants.t_min and fitness_function == calculate_novelty:
                fitness_function = calculate_fitnesses
        if fitness_function == calculate_novelty:
            # print "novelty"
            print bcolors.OKMSG + "novelty" + bcolors.ENDC
            generations.append("novelty")
        else:
            # print "fitness"
            print bcolors.ERRMSG + "fitness" + bcolors.ENDC
            generations.append("fitness")

        # evaluate the offspring
        count_individuals = 0
        for ind in pop:
            ind.fitness.values = fitness_function(ind, pop, toolbox, parameters)
            if ind.fitness.values[0] > parameters.fitness_threshold:
                count_individuals = count_individuals + 1
        print count_individuals
        archive_size[g] = len(FileManagement.getArchive()["archive"])
        # selection
        if parameters.evaluation_method_index == 2:
            if fitness_function == calculate_fitnesses:
                parents = toolbox.selectTournament(pop)
            else:
                if parameters.multi_objective_selection == "spea2":
                    parents = toolbox.selectspea2(pop)
                else:
                    parents = toolbox.selectnsga2(pop)
        elif parameters.evaluation_method_index == 1:
            if parameters.multi_objective_selection == "spea2":
                parents = toolbox.selectspea2(pop)
            else:
                parents = toolbox.selectnsga2(pop)
        else:
            parents = toolbox.selectTournament(pop)


        results_full = ""
        avg_nov_local = 0
        avg_fit_local = 0
        for x in parents:
            results_full = results_full + "".join(x)
            if fitness_function == calculate_novelty:
                avg_nov_local = avg_nov_local + x.fitness.values[1]
            avg_fit_local = avg_fit_local + x.fitness.values[0]
        avg_fit_local = avg_fit_local / 10
        avg_nov_local = avg_nov_local / 10
        if fitness_function == calculate_novelty:
            novelty_avg[g] = avg_nov_local
        fitnesses_avg[g] = avg_fit_local

        full_ncd_results[g] = compute_ncd(results_full, repertoire_string)
        criterion_1[g] = compute_criterion_1(list(map(toolbox.clone, parents)), repertoire_string)
        criterion_2[g] = compute_criterion_2(list(map(toolbox.clone, parents)), repertoire_string, 0.5)

        # Clone the selected individuals
        offspring = list(map(toolbox.clone, parents))

        # new individuals of the population
        new = []

        # crossover
        i = 0
        for child1 in offspring:
            for child2 in offspring:
                if i < Constants.population_size * 9 / 10:
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

    # last evaluation
    for ind in pop:
        ind.fitness.values = fitness_function(ind, pop, toolbox, parameters)

    # last selection

    if parameters.evaluation_method_index == 2:
        if fitness_function == calculate_fitnesses:
            final = toolbox.selectTournament(pop)
        else:
            if parameters.multi_objective_selection == "spea2":
                final = toolbox.selectspea2(pop)
            else:
                final = toolbox.selectnsga2(pop)
    elif parameters.evaluation_method_index == 1:
        if parameters.multi_objective_selection == "spea2":
            final = toolbox.selectspea2(pop)
        else:
            final = toolbox.selectnsga2(pop)
    else:
        final = toolbox.selectTournament(pop)
    results_full = ""

    avg_nov_local = 0
    avg_fit_local = 0
    for x in final:
        results_full = results_full + "".join(x)
        if fitness_function == calculate_novelty:
            avg_nov_local = avg_nov_local + x.fitness.values[1]
        avg_fit_local = avg_fit_local + x.fitness.values[0]
    avg_fit_local = avg_fit_local / 10
    avg_nov_local = avg_nov_local / 10
    if fitness_function == calculate_novelty:
        novelty_avg[g] = avg_nov_local
    fitnesses_avg[g] = avg_fit_local
    if fitness_function == calculate_novelty:
        plot2d_2_series(data=fitnesses_avg,data2 = novelty_avg,  x_label="generation", y_label="fitness and novelty", path=parameters.full_name + "values")
    else:
        plot2d(data=fitnesses_avg, x_label="generation", y_label="fitness", path=parameters.full_name + "values")
    archive_size[g] = len(FileManagement.getArchive()["archive"])
    plot2d_no_lim(data=archive_size, x_label="generation", y_label="archive size", path=parameters.full_name + "archivesize")

    full_ncd_results[g] = compute_ncd(results_full, repertoire_string)
    criterion_1[g] = compute_criterion_1(list(map(toolbox.clone, final)), repertoire_string)
    criterion_2[g] = compute_criterion_2(list(map(toolbox.clone, final)), repertoire_string, 0.5)
    plot2d(data=full_ncd_results, x_label="generation", y_label="ncd_full", path=parameters.full_name + "ncd_full")
    plot2d(data=criterion_1, x_label="generation", y_label="criterion_1", path=parameters.full_name + "criterion_1")
    plot2d(data=criterion_2, x_label="generation", y_label="criterion_2", path=parameters.full_name + "criterion_2")
    jsonEditor.dumpDict(filename=parameters.full_name + "ncd_full", dict=full_ncd_results)
    jsonEditor.dumpDict(filename=parameters.full_name + "criterion_1", dict=criterion_1)
    jsonEditor.dumpDict(filename=parameters.full_name + "criterion_2", dict=criterion_2)
    jsonEditor.dumpDict(filename=parameters.full_name + "criterion_2", dict=criterion_2)
    jsonEditor.dumpDict(filename=parameters.full_name + "archivesize", dict=archive_size)
    jsonEditor.dumpDict(filename=parameters.full_name + "values", dict={"fitness": fitnesses_avg, "novelty": novelty_avg})
    # plot2d_fit_nov(pop,final, parameters.full_name)
    return final, generations