import random
import Constants
from GeneticAlgorithm import TSelNovelty
from GeneticAlgorithm.FileManagement import FileManagement
from GeneticAlgorithm.StringOperations import string_dissimilarity, string_similarity
from Dissimilarity import dissim


def novelty(choreography, population):
    archive = FileManagement.getArchive()["archive"]
    # if len(archive) == 0:
    #     return 0
    # here selects the novelty individuals
    pop_selected = TSelNovelty.select(population, choreography, archive)
    value = 0
    for x in pop_selected:
        value = value + string_dissimilarity("".join(choreography), "".join(x))
    value = value / len(pop_selected)
    return value


# the return should be between parenthesis because needs to return a list
# correct
def fitness(movesList, parameters):
    evaluation = 0
    repertoire = FileManagement.getRepertoireWithPath(parameters.repertoire_path)["repertoire"]
    repertoire_size = len(repertoire)
    archive = FileManagement.getArchive()["archive"]
    arch_len = len(archive)
    for x in repertoire:
        evaluation = evaluation + string_similarity("".join(x["choreo"]), "".join(movesList))
    evaluation = evaluation / repertoire_size
    # conditions needed to add the choreography to the archive
    if evaluation > parameters.fitness_threshold:
        # if the archive has no entries or if the dissimilarity between the
        # element and the choreographies in the archive is higher than a threshold
        diss = dissim(movesList)
        if arch_len == 0 or dissim(movesList) > parameters.dissim_threshold:
            ml = "".join(movesList)
            FileManagement.addToArchive(ml)
            FileManagement.addres(x={"choreo": ml, "fitness": evaluation, "dissim": diss}, path=parameters.full_name + "res_arch", index = arch_len)
    return evaluation


def calculate_fitness(movesList, parameters):
    return (fitness(movesList, parameters), 0)


def calculate_fitness_and_novelty(choreography, population, parameters):
    fitness_value = fitness(choreography, parameters)
    novelty_value = novelty(choreography, population)
    return (fitness_value,novelty_value)


def mutation(movesList):
    for _ in range(random.randint(1,Constants.max_number_of_mutations)):
        movesList[random.randint(0,len(movesList)-1)] = random.choice(Constants.list_of_moves.keys())
    return (movesList,)


def init_individual():
    moves_list = []
    for _ in range(Constants.number_of_moves):
            move = random.choice(Constants.list_of_moves.keys())
            moves_list.append(move)
    return moves_list