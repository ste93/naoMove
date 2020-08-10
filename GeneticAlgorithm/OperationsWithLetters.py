import random
import Constants
from GeneticAlgorithm import TSelNovelty
from GeneticAlgorithm.FileManagement import Archive
from GeneticAlgorithm.StringOperations import string_similarity
from Dissimilarity import dissim


def novelty(choreography, population):
    archive = Archive.getArchive()["archive"]
    if len(archive) == 0:
        return 0
    pop_selected = TSelNovelty.select(population, choreography, archive)
    value = 0
    for x in pop_selected:
        value = value + string_similarity("".join(choreography), "".join(x))
    value = value / len(pop_selected)
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
        evaluation = evaluation + string_similarity("".join(x["choreo"]), "".join(movesList))
    evaluation = evaluation / (r)
    if evaluation > Constants.fitness_threshold:
        if arch_len == 0 or 0 < dissim(movesList) < Constants.dissim_threshold:
            Archive.addToArchive("".join(movesList))
    return evaluation


def calculate_fitness(movesList, repertoirePath):
    return (fitness(movesList, repertoirePath),0)


def calculate_fitness_and_novelty(choreography, population, repertoirePath):
    fitness_value = fitness(choreography, repertoirePath)
    novelty_value = novelty(choreography, population)
    return (fitness_value,novelty_value)


def mutation(movesList):
    for _ in range(random.randint(1,Constants.max_number_of_mutations)):
        movesList[random.randint(0,len(movesList)-1)] = random.choice(Constants.list_of_moves.keys())
    return (movesList,)
