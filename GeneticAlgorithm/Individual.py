import random
import Constants
from JsonEditor import jsonEditor

class Choreography(object):
    # This class does not require the fitness attribute
    # it will be  added later by the creator
    def __init__(self, attributes):
        # initialisation
        # print "asdfasdgahgarea"
        self.movesList = attributes[0]
        

def init_individual():
    # ind_class will receive a class inheriting from MyContainer
    moves_list = []
    # for _ in range(random.randint(Constants.min_number_of_moves, Constants.max_number_of_moves)):
    for _ in range(Constants.number_of_moves):
            move = random.choice(Constants.list_of_moves.keys())
            moves_list.append(move)
    return moves_list



# def init_individual():
#     # ind_class will receive a class inheriting from MyContainer
#     moves_list = []
#     for _ in range(random.randint(Constants.min_number_of_moves, Constants.max_number_of_moves)):
#         try:
#             move = random.choice(Constants.list_of_moves)
#             dict = jsonEditor.readDict(move)
#             dict["time"] = random.randint(1, 15)
#             moves_list.append(dict)
#             # print dict
#         except:
#             print "move not found: " + move
#     print moves_list
#     return moves_list
