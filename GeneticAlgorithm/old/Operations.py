import json
import random

import GeneticAlgorithm.Constants
from JsonEditor import jsonEditor


def evaluate_reparation(individual):
    return individual


def evaluate_duplicates(choreography):
    seen = set()
    for x in choreography:
        item = json.dumps(x)
        if item not in seen:
            seen.add(item)

    # uniq = [x for x in movesList if x not in seen and not seen.add(x)]
    # print "evaluated duplicates"
    return len(choreography) - len(seen)


def evaluate_distance_between_moves(choreography):
    total_distance = 0
    print choreography
    for x in range(len(choreography)-1):
        for joint in choreography[x]["angles"]:
            total_distance = abs(choreography[x + 1]["angles"].get(joint) - choreography[x]["angles"].get(joint))
    return total_distance


# the return should be between parenthesis because needs to return a list
def fitness(movesList):
    evaluation = evaluate_distance_between_moves(movesList) + evaluate_duplicates(movesList)
    return (evaluation,)


def mutation(movesList):
    for _ in range(random.randint(1, GeneticAlgorithm.Constants.max_number_of_mutations)):
        movesList[random.randint(0,len(movesList)-1)] = jsonEditor.readDict(random.choice(
            GeneticAlgorithm.Constants.list_of_moves))
    return (movesList,)
