import winsound
import random

from GeneticAlgorithm.GeneticInit import init


if __name__ == "__main__":
    # execute only if run as a script

    try:
        # for repertoire_index in [0, 1, 2, 3, 4]:
        #     for generations in [60, 100, 200, 500]:
        # for algorithm in ["nsga2", "spea2"]:
        #         init(number_of_generations=60,  # generations,
        #              repertoireIndex=0,  # repertoire_index,
        #              evaluation_method_index=0,
        #              random_seed=150,
        #              multi_objective_selection="spea2")
        for random_seed in [100]:
            for generations in [200]:
                for evaluation_method in [2]:
                    for repertoire_path in [1]:
                        init(number_of_generations=generations,  # generations,
                             repertoireIndex=repertoire_path,  # repertoire_index,
                             evaluation_method_index=evaluation_method,
                             random_seed=random_seed,
                             multi_objective_selection="spea2")
                        winsound.Beep(500, 1000)

        winsound.Beep(1000, 4000)
    except Exception as e:
        print "exception", e