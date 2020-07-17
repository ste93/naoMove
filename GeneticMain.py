import time
from GeneticAlgorithm import DEAP_algorithm as DEAP_algorithm, Constants

# from GeneticAlgorithm import DEAP_algorithm, Constants
from GeneticAlgorithm.FileManagement import Archive
from JsonEditor import jsonEditor
# import winsound


def init(index, name):
    start_time = time.time()
    ngen = 100
    pop = DEAP_algorithm.create_choreography(ngen)


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
               "algorithm": "as paper"
                                   }
    print("  Min %s" % min(fits))
    print("  Max %s" % max(fits))
    print("  Avg %s" % mean)
    print("  Std %s" % std)
    filename = name + str(index)
    for ind in pop:
        print ind, ind.fitness.values
        Archive.saveResultsToPath({"choreo": str("".join(pop[i])),
                                   "value": fits[i],
                                   "time elapsed": time_elapsed,
                                   "statistics": statistics,
                                   "archive" : Archive.getArchive()["archive"],
                                   "list_of_moves" : Constants.list_of_moves,
                                   "repertoire": Archive.getRepertoire(),
                                   "parameters": parameters
                                   }, filename)
        with open(filename, "a") as myfile:
            myfile.write("\n" + str("".join(pop[i])))
    # frequency = 2500  # Set Frequency To 2500 Hertz
    # duration = 3000  # Set Duration To 1000 ms == 1 second
    # winsound.Beep(frequency, duration)

try:
    for i in range(1):
        init("prova100_",i)

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