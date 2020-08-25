from GeneticAlgorithm.GeneticInit import init


if __name__ == "__main__":
    # execute only if run as a script

    try:
        # for repertoire_index in [0, 1, 2, 3, 4]:
        #     for generations in [60, 100, 200, 500]:
        for algorithm in ["nsga2", "spea2"]:
                init(number_of_generations=200,  # generations,
                     repertoireIndex=0,  # repertoire_index,
                     evaluation_method_index=2,
                     random_seed=10,
                     multi_objective_selection=algorithm)
        # for index in range(6):
        #     for generations in [60, 100, 200, 500]:
        #         for evaluation_method in [0,1,2]:
        #             for repertoire_path in [0,1,2,3,4]:
        #                 init("prova_alg_2", index, generations, repertoire_path, evaluation_method)

    except Exception as e:
        print "exception", e