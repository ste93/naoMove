# the thresholds considered when need to add a choreography to the archive
# the threshold considered to calculate feasible individuals
# threshold_f_min = 0.3
from JsonEditor import jsonEditor
# min_number_of_moves = 5
# max_number_of_moves = 16
number_of_moves = 16
# parameter used to switch to fitness
t_min = 65
# parameter used to switch to hybrid
t_max = 80
# max number of archive entries considered
max_arch = 5

max_number_of_mutations = 4
population_size = 100


archive_path = "json/archive/archive"
repertoire_paths = [

    "json/archive/repertoire1",
    "json/archive/repertoire2",
    "json/archive/repertoire3_priest",
    "json/archive/repertoire3_warrior",
    "json/archive/repertoire4",
    "json/archive/repertoire6",
    "json/archive/repertoire5",
    "json/archive/repertoire10"
]

# results_path = "json/archive/results"
random_path = "json/archive/random"
# list_of_moves_path = "json/archive/list_of_moves"

# MUTPB is the probability for mutating an individual
MUTPB = 0.35


list_of_moves = jsonEditor.readDict("./json/archive/list_of_moves")

# {
#     "a": "json/finiti/armsdown",
#     "b": "json/finiti/swordright",
#     "c": "json/finiti/swordrightleftrequest",
#     "d": "json/finiti/openarms",
#     "e": "json/finiti/rightopen",
#     "f": "json/finiti/rightup45",
#     "g": "json/finiti/extremelysadchest",
#     "h": "json/finiti/swordleft",
#     "i": "json/finiti/arms45",
#     "j": "json/finiti/rightsadchest",
#     "k": "json/finiti/requestright",
#     "l": "json/finiti/request",
#     "m": "json/finiti/offering",
#     "n": "json/finiti/armsforward",
#     "o": "json/finiti/sadleft",
#     "p": "json/finiti/extremelysad",
#     "q": "json/finiti/sadright",
#     "r": "json/finiti/openarmsextended",
#     "s": "json/finiti/armsinit",
#     "t": "json/finiti/armsuppraying",
#     "u": "json/finiti/shieldleft",
#     "v": "json/finiti/shieldright",
#     "w": "right",
#     "x": "left",
#     "y": "backward",
#     "z": "forward"
#
# }

