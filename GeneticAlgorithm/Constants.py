# the thresholds considered when need to add a choreography to the archive
fitness_threshold = 0.37
novelty_threshold = 0.3
# the threshold considered to calculate feasible individuals
threshold_f_min = 0.3

min_number_of_moves = 5
max_number_of_moves = 16
number_of_moves = 16
t_min = 10
t_max = 10
max_arch = 7

# min_exec_time = 1
# max_exec_time = 16

max_number_of_mutations = 4
population_size = 100


archive_path = "json/archive/archive"
repertoire_path = "json/archive/repertoire"
results_path = "json/archive/results"
random_path = "json/archive/random"
list_of_moves_path = "json/archive/list_of_moves"
# CXPB  is the probability with which two individuals are crossed
CXPB = 0.5
# MUTPB is the probability for mutating an individual
MUTPB = 0.2


# repertoire = {
#     "choreo1" : "abcdabef",
#     "choreo2" : "abcgbfea",
#     "choreo3" : "hibebajk",
#     "choreo3_2" : "ldaebmda",
#     "choreo4" : "bldanoba"
# }

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