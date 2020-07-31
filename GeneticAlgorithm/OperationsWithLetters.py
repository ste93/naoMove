import random
import Constants
from GeneticAlgorithm import TSelNovelty
from GeneticAlgorithm.FileManagement import Archive
from GeneticAlgorithm.StringOperations import string_similarity




def novelty(choreography, population):
    archive = Archive.getArchive()["archive"]
    if len(archive) == 0:
        return 0

    pop_selected = TSelNovelty.select(population, choreography, archive)
    # pop_selected = tools.selTournament(population, k=4, tournsize=5)
    value = 0
    for x in pop_selected:
        value = value + string_similarity(str(choreography), str(x))
    value = value / len(pop_selected)
    # print "novelty value", value
    return value


# the return should be between parenthesis because needs to return a list
# correct
def fitness(movesList, repertoirePath):
    evaluation = 0
    repertoire = Archive.getRepertoireWithPath(repertoirePath)["repertoire"]
    r = len(repertoire)
    archive = Archive.getArchive()["archive"]
    arch_len = len(archive)

    for x in repertoire:
        evaluation = evaluation + string_similarity(x["choreo"], movesList)
    evaluation = evaluation / (r)
    # evaluation = (evaluation + evaluate_duplicates(movesList))/2
    if arch_len == 0 and evaluation > Constants.fitness_threshold: #case 1
        Archive.addToArchive(movesList)
    return evaluation


def calculate_fitness(movesList, repertoirePath):
    # print "fitness"
    return (fitness(movesList, repertoirePath),0)


def calculate_fitness_and_novelty(choreography, population, repertoirePath):
    # print "calculate_novelty"
    fitness_value = 0 # fitness(choreography, repertoirePath)
    novelty_value = novelty(choreography, population)
    archive = Archive.getArchive()["archive"]
    # if len(archive) > 0 and fitness_value > Constants.fitness_threshold and novelty_value > Constants.novelty_threshold:
    #     Archive.addToArchive(choreography)
    if len(archive) == 0 or (0 < novelty_value < Constants.novelty_threshold):
        Archive.addToArchive(choreography)
    return (fitness_value,novelty_value)


def mutation(movesList):
    for _ in range(random.randint(1,Constants.max_number_of_mutations)):
        movesList[random.randint(0,len(movesList)-1)] = random.choice(Constants.list_of_moves.keys())
    return (movesList,)
