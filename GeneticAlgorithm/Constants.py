# the thresholds considered when need to add a choreography to the archive
fitness_threshold = 0.3
dissim_threshold = 0.8
# the threshold considered to calculate feasible individuals
# threshold_f_min = 0.3

# min_number_of_moves = 5
# max_number_of_moves = 16
number_of_moves = 16
# parameter used to switch to fitness
t_min = 2
# parameter used to switch to hybrid
t_max = 13
# max number of archive entries considered
max_arch = 5

max_number_of_mutations = 4
population_size = 100


archive_path = "json/archive/archive"
repertoire_path = [
    "json/archive/repertoire",
    "json/archive/repertoire1",
    "json/archive/repertoire3",
    "json/archive/repertoire4",
    "json/archive/repertoire5"
]
results_path = "json/archive/results"
random_path = "json/archive/random"
list_of_moves_path = "json/archive/list_of_moves"
# CXPB  is the probability with which two individuals are crossed
CXPB = 0.5
# MUTPB is the probability for mutating an individual
MUTPB = 0.35


list_of_moves = {
    "a": "json/finiti/armsdown",
    "b": "json/finiti/swordright",
    "c": "json/finiti/swordrightleftrequest",
    "d": "json/finiti/openarms",
    "e": "json/finiti/rightopen",
    "f": "json/finiti/rightup45",
    "g": "json/finiti/extremelysadchest",
    "h": "json/finiti/swordleft",
    "i": "json/finiti/arms45",
    "j": "json/finiti/rightsadchest",
    "k": "json/finiti/requestright",
    "l": "json/finiti/request",
    "m": "json/finiti/offering",
    "n": "json/finiti/armsforward",
    "o": "json/finiti/sadleft",
    "p": "json/finiti/extremelysad",
    "q": "json/finiti/sadright",
    "r": "json/finiti/openarmsextended",
    "s": "json/finiti/armsinit",
    # "t": "json/finiti/swordrightleftrequestwithlegs"
}
              # "json/finiti/armsdown",
              # "json/finiti/armsforward",
              # "json/finiti/sadleft",
              # "json/finiti/armsinit",
              # "json/finiti/extremelysad",
              # "json/finiti/openarms",
              # "json/finiti/openarmsextended",
              # "json/finiti/request",
              # "json/finiti/swordleft",
              # "json/finiti/swordright",
              # "json/finiti/sadright"}


movesdict = {}

list_of_keys = []