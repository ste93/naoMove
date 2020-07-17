import time
from GeneticAlgorithm import DEAP_algorithm as DEAP_algorithm, Constants

# from GeneticAlgorithm import DEAP_algorithm, Constants
from GeneticAlgorithm.FileManagement import Archive
from JsonEditor import jsonEditor
# import winsound


def init(name, index, ngen, repertoireIndex, evaluation_method):
    full_name = "json/archive/" + name + "_" + str(index) + "_" + str(ngen) + "_" + str(repertoireIndex) + "_"+ str(evaluation_method)
    start_time = time.time()
    repertoirePath = Constants.repertoire_path[repertoireIndex]
    pop = DEAP_algorithm.create_choreography(ngen, evaluation_method, repertoirePath)

    # Gather all the fitnesses in one list and print the stats
    fits = [ind.fitness.values[0] for ind in pop]
    time_elapsed  =(time.time() - start_time)
    print("--- %s seconds ---" % time_elapsed)

    length = len(pop)
    mean = sum(fits) / length
    sum2 = sum(x * x for x in fits)
    std = abs(sum2 / length - mean ** 2) ** 0.5
    statistics = {"min": min(fits), "max": max(fits),"mean": mean, "std": std}
    parameters = {
               "generations": ngen,
               "fitness_threshold": Constants.fitness_threshold,
               "novelty_threshold": Constants.novelty_threshold,
               "threshold_f_min": Constants.threshold_f_min,
               "number_of_moves": Constants.number_of_moves,
               "t_min ": Constants.t_min,
               "t_max": Constants.t_max,
               "max_arch": Constants.max_arch,
               "max_number_of_mutations": Constants.max_number_of_mutations,
               "population_size": Constants.population_size,
               "CXPB": Constants.CXPB,
               "MUTPB": Constants.MUTPB,
               "evaluation_method": evaluation_method
                                   }
    print("  Min %s" % min(fits))
    print("  Max %s" % max(fits))
    print("  Avg %s" % mean)
    print("  Std %s" % std)
    results = []
    print pop
    for ind in pop:
        print ind, ind.fitness.values
        results.append({"ind": ind, "value": ind.fitness.values })
        with open(full_name, "a") as myfile:
            myfile.write("\n" + str("".join(pop[i])))

    Archive.saveResultsToPath({"time elapsed": time_elapsed,
                               "statistics": statistics,
                               "archive" : Archive.getArchive()["archive"],
                               "list_of_moves" : Constants.list_of_moves,
                               "repertoire": Archive.getRepertoire(),
                               "parameters": parameters,
                               "results": results
                               }, full_name)
    # frequency = 2500  # Set Frequency To 2500 Hertz
    # duration = 3000  # Set Duration To 1000 ms == 1 second
    # winsound.Beep(frequency, duration)

try:
    for i in range(6):
        for j in [60, 100, 200, 500]:
            for k in [0,1,2]:
                for l in [0,1,2,3,4]:
                    init("prova", i, j, l, k)

except Exception as e:
    print "exception", e

# frequency = 2500  # Set Frequency To 2500 Hertz
# duration = 1000  # Set Duration To 1000 ms == 1 second
# winsound.Beep(frequency, duration)
# time.sleep(1)
# winsound.Beep(frequency, duration)
# time.sleep(1)
# winsound.Beep(frequency, duration)
# time.sleep(1)
# winsound.Beep(frequency, duration)