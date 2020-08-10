import os
from datetime import datetime
import time
from GeneticAlgorithm import DEAP_algorithm as DEAP_algorithm, Constants
from GeneticAlgorithm.FileManagement import Archive


# repertoire index is the index of the corresponding path in constants
def init(name, index, ngen, repertoireIndex, evaluation_method):
    now = datetime.now()  # current date and time
    dir = "json/archive/risultati genetico/"+ str(evaluation_method) +"/"
    if not os.path.exists(dir):
        os.mkdir(dir)
    full_name = "json/archive/risultati genetico/"+ str(evaluation_method) +"/" + name + "_" + str(index) + "_" + str(ngen) + "_" + str(repertoireIndex) + "_"+ str(evaluation_method) + now.strftime("%Y%m%d-%H:%M")
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
               "dissim_threshold": Constants.dissim_threshold,
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
    for ind in pop:
        print "".join(ind), ind.fitness.values
        results.append({"ind": "".join(ind), "value": ind.fitness.values })
        with open(full_name, "a") as myfile:
            myfile.write("\n" + str("".join(ind)))
    for element in Archive.getArchive()["archive"]:
        with open(full_name + "archive", "a") as myfile:
            myfile.write("\n" + str("".join(element)))


    Archive.saveResultsToPath({"time elapsed": time_elapsed,
                               "statistics": statistics,
                               "archive" : Archive.getArchive()["archive"],
                               "list_of_moves" : Constants.list_of_moves,
                               "repertoire": Archive.getRepertoire(),
                               "parameters": parameters,
                               "results": results
                               }, full_name)

try:

    init("prova_alg_2",1, 100,  0, 2)
    # for index in range(6):
    #     for generations in [60, 100, 200, 500]:
    #         for evaluation_method in [0,1,2]:
    #             for repertoire_path in [0,1,2,3,4]:
    #                 init("prova_alg_2", index, generations, repertoire_path, evaluation_method)

except Exception as e:
    print "exception", e