import os
from datetime import datetime
import time

import GeneticAlgorithm.Evaluation
from GeneticAlgorithm import DEAP_algorithm as DEAP_algorithm, Constants, CalculateTypicality, Evaluation
from GeneticAlgorithm.FileManagement import FileManagement
from GeneticAlgorithm.Parameters import Parameters


# repertoire index is the index of the corresponding path in constants
def init(number_of_generations, repertoireIndex, evaluation_method_index, random_seed, multi_objective_selection, dissim_threshold, fitness_threshold, timenow):
    try:
        now = datetime.now()  # current date and time
        evaluation_method = "fitness"
        if evaluation_method_index == 1:
            evaluation_method = "novelty"
        elif evaluation_method_index == 2:
            evaluation_method = "fitness and novelty"

        parameters = Parameters(number_of_generations=number_of_generations,
                                repertoire_path=Constants.repertoire_paths[repertoireIndex],
                                evaluation_method_index=evaluation_method_index,
                                random_seed=random_seed,
                                dissim_threshold=dissim_threshold,
                                multi_objective_selection=multi_objective_selection,
                                fitness_threshold=fitness_threshold)
        full_name = "json/archive/risultati genetico/" + timenow + "/" \
                    + str(Constants.number_of_moves)  + "_" \
                    + str(Constants.max_arch) + "_"\
                    + str(Constants.MUTPB) + "_"\
                    + str(Constants.t_min) + "_"\
                    + str(Constants.t_max) + "_"\
                    + str(Constants.max_number_of_mutations) + "_"\
                    + str(Constants.population_size) + "_"\
                    + str(repertoireIndex) + "_"\
                    + str(number_of_generations) + "_"\
                    + str(random_seed) + "_"\
                    + str(parameters.fitness_threshold)+ "_"\
                    + str(parameters.dissim_threshold)+ "_"\
                    + multi_objective_selection\
                    + "/" + evaluation_method + "/" + now.strftime("%Y%m%d-%H.%M.%S") + "/"



                    # + str(evaluation_method) +\
                    # "/" + "fit " + str(Constants.fitness_threshold) + " dissim " + str(Constants.dissim_threshold) + "/"\
                    # + name + "_" + str(index) + "_" + str(ngen) + "_" + \
                    # str(repertoireIndex) + "_"+ str(evaluation_method)+ "_" + \
                    # now.strftime("%Y%m%d-%H.%M.%S") + "/"
        if not os.path.exists(full_name):
            try:
                os.makedirs(full_name)
            except Exception as e:
                print e

        parameters.set_path(full_name)
        start_time = time.time()
        pop, generations = DEAP_algorithm.create_choreography(parameters)
        # print "ending"


        # Gather all the fitnesses in one list and print the stats
        fits = [ind.fitness.values[0] for ind in pop]
        time_elapsed  =(time.time() - start_time)
        print("--- %s seconds ---" % time_elapsed)

        results_string = Evaluation.create_string_results(pop)
        repertoire_string = Evaluation.create_string_repertoire(FileManagement.getRepertoireWithPath(parameters.repertoire_path)["repertoire"])
        ncd = Evaluation.compute_ncd(results_string, repertoire_string)

        length = len(pop)
        mean = sum(fits) / length
        sum2 = sum(x * x for x in fits)
        std = abs(sum2 / length - mean ** 2) ** 0.5
        statistics = {"min": min(fits), "max": max(fits),"mean": mean, "std": std}
        parameters_to_serialize = {
                   "generations": number_of_generations,
                   "fitness_threshold": parameters.fitness_threshold,
                   "dissim_threshold": parameters.dissim_threshold,
                   "number_of_moves": Constants.number_of_moves,
                   "t_min ": Constants.t_min,
                   "t_max": Constants.t_max,
                   "max_arch": Constants.max_arch,
                   "max_number_of_mutations": Constants.max_number_of_mutations,
                   "population_size": Constants.population_size,
                   # "CXPB": Constants.CXPB,
                   "MUTPB": Constants.MUTPB,
                   "evaluation_method": evaluation_method,
                    "multi_objective_selection": multi_objective_selection
                   }
        print("  Min %s" % min(fits))
        print("  Max %s" % max(fits))
        print("  Avg %s" % mean)
        print("  Std %s" % std)
        results = []
        for ind in pop:
            print "".join(ind), ind.fitness.values
            results.append({"ind": "".join(ind), "value": ind.fitness.values })
            with open(full_name + "results_serialized", "a") as myfile:
                myfile.write("\n" + str("".join(ind)))
            myfile.close()
        for element in FileManagement.getArchive()["archive"]:
            with open(full_name + "archive_serialized", "a") as myfile:
                myfile.write("\n" + str("".join(element)))
            myfile.close()
        for element in FileManagement.getRepertoireWithPath(parameters.repertoire_path)["repertoire"]:
            with open(full_name + "repertoire_serialized", "a") as myfile:
                myfile.write("\n" + str("".join(element["choreo"])))
            myfile.close()

        for element in generations:
            with open(full_name + "generations_serialized", "a") as myfile:
                myfile.write("\n" + str("".join(element)))
            myfile.close()


        FileManagement.saveResultsToPath({"time elapsed": time_elapsed,
                                   "statistics": statistics,
                                   "ncd": ncd,
                                   "min_distance": GeneticAlgorithm.Evaluation.calculate_typicality(parameters.repertoire_path, pop),
                                   "archive" : FileManagement.getArchive()["archive"],
                                   "list_of_moves" : Constants.list_of_moves,
                                   "repertoire": FileManagement.getRepertoire(),
                                   "parameters": parameters_to_serialize,
                                   "results": results,
                                   # "strings" : [results_string, repertoire_string]
                                   }, full_name + "results")
        print "end reached"

    except Exception as e:
        print "error in genetic init " + e