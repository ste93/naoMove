import json
import random
import Constants
from distance import jaccard
from strsimpy.jaro_winkler import JaroWinkler
from GeneticAlgorithm.FileManagement import Archive


def evaluate_duplicates(choreography):
    seen = set()
    for x in choreography:
        item = json.dumps(x)
        if item not in seen:
            seen.add(item)

    # uniq = [x for x in movesList if x not in seen and not seen.add(x)]
    # print "evaluated duplicates"
    return len(seen)/len(choreography)


# def add_to_archive(choreography, fitness, novelty):
#     archive = Archive.getRepertoire()["archive"]
#     r = len(archive)




def novelty(choreography, population, tools, toolbox):
    archive = Archive.getArchive()["archive"]
    if len(archive) == 0:
        return 0
    pop = []
    for x in population:
        a = toolbox.individual()
        a.movesList = x
        pop.append(a)
    for x in pop:
        x.fitness.values = (0,string_distance(str(choreography), str(x.movesList)))
    pop_selected = tools.selTournament(population, k=4, tournsize=5)
    arch = []
    for x in archive:
        a = toolbox.individual()
        a.movesList = x
        arch.append(a)
    for x in arch:
        x.fitness.values = (0,string_distance(str(choreography), str(x.movesList)))
    pop_resulting = pop_selected + arch
    # print pop_resulting
    r = min(len(archive), Constants.max_arch)
    ind_to_compare = tools.selBest(pop_resulting, k=r)
    value = 0
    for x in ind_to_compare:
        value = value + string_distance(str(choreography), str(x))
    value = value / r
    return value


def string_distance(a,b):
    jarowinkler = JaroWinkler()
    return jarowinkler.similarity(a,b) + jaccard(a,b)


# the return should be between parenthesis because needs to return a list
# correct
def fitness(movesList):
    evaluation = 0
    repertoire = Archive.getRepertoire()["repertoire"]
    r = len(repertoire)
    archive = Archive.getArchive()["archive"]
    arch_len = len(archive)

    for x in repertoire:
        evaluation = evaluation + string_distance(x["choreo"],movesList)
    evaluation = evaluation / (2*r)
    # evaluation = (evaluation + evaluate_duplicates(movesList))/2
    if arch_len == 0 and evaluation > Constants.fitness_threshold: #case 1
        Archive.addToArchive(movesList)
    return evaluation


def calculate_fitness(movesList):
    # print "fitness"
    return (fitness(movesList),0)


def calculate_fitness_and_novelty(choreography, population, tools, toolbox):
    # print "calculate_novelty"
    fitness_value = fitness(choreography)
    novelty_value = novelty(choreography, population, tools, toolbox)
    archive = Archive.getArchive()["archive"]
    if len(archive) > 0 and fitness_value > Constants.fitness_threshold and novelty_value > Constants.novelty_threshold:
        Archive.addToArchive(choreography)
    return (fitness_value,novelty_value)


def mutation(movesList):
    for _ in range(random.randint(1,Constants.max_number_of_mutations)):
        movesList[random.randint(0,len(movesList)-1)] = random.choice(Constants.list_of_moves.keys())
    return (movesList,)
