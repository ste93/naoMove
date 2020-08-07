import random

from GeneticAlgorithm import Constants


def init_individual():
    # ind_class will receive a class inheriting from MyContainer
    moves_list = []
    # for _ in range(random.randint(Constants.min_number_of_moves, Constants.max_number_of_moves)):
    for _ in range(Constants.number_of_moves):
            move = random.choice(Constants.list_of_moves.keys())
            moves_list.append(move)
    return moves_list


for x in range(100):
    with open(Constants.random_path, "a") as myfile:
        myfile.write("\n"  + str("".join(init_individual())))