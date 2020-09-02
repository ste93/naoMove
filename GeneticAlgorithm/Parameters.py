from GeneticAlgorithm.CalculateThreshold import calculate_fitness_threshold_max, calculate_fitness_threshold


class Parameters:
    # the thresholds considered when need to add a choreography to the archive
    def __init__(self,
                 repertoire_path,
                 dissim_threshold,
                 number_of_generations,
                 evaluation_method_index,
                 random_seed,
                 multi_objective_selection):
        self.random_seed = random_seed  # type: int
        self.evaluation_method_index = evaluation_method_index  # type: int
        self.number_of_generations = number_of_generations  # type: int
        self.fitness_threshold = calculate_fitness_threshold_max(repertoire_path)  # type: float
        self.dissim_threshold = dissim_threshold  # type: float
        self.repertoire_path = repertoire_path  # type: basestring
        self.multi_objective_selection = multi_objective_selection  # type: basestring


    def set_path(self, full_name):
        self.full_name = full_name  # type: basestring