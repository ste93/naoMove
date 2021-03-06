from datetime import datetime
from GeneticAlgorithm import Constants
from GeneticAlgorithm.GeneticInit import init
from GeneticAlgorithm.CalculateThreshold import calculate_fitness_threshold_max, calculate_fitness_threshold

if __name__ == "__main__":
    # execute only if run as a script
        # for repertoire_index in [0, 1, 2, 3, 4]:
        #     for generations in [60, 100, 200, 500]:
        # for algorithm in ["nsga2", "spea2"]:
        #         init(number_of_generations=60,  # generations,
        #              repertoireIndex=0,  # repertoire_index,
        #              evaluation_method_index=0,
        #              random_seed=150,
        #              multi_objective_selection=
        now = datetime.now()
        timenow = now.strftime("%Y%m%d-%H.%M")
        for random_seed in [100]:
        # for random_seed in [100, 330, 42]:
            for generations in [ 1000]:
            # for generations in [1000,2000]:
                for evaluation_method in [1]:
                    for repertoireIndex in [3]:
                    # for repertoireIndex in [5]:
                        init(number_of_generations=generations,  # generations,
                             repertoireIndex=repertoireIndex,  # repertoire_index,
                             evaluation_method_index=evaluation_method,
                             random_seed=random_seed,
                             multi_objective_selection="spea2",
                             dissim_threshold=0.55,
                             fitness_threshold=0.6,
                             timenow=timenow)
                        init(number_of_generations=generations,  # generations,
                             repertoireIndex=repertoireIndex,  # repertoire_index,
                             evaluation_method_index=evaluation_method,
                             random_seed=random_seed,
                             multi_objective_selection="spea2",
                             dissim_threshold=0.62,
                             fitness_threshold=0.5,
                             timenow=timenow)
                        # winsound.Beep(500, 1000)

