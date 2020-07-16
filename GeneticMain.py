import time
from GeneticAlgorithm import DEAP_algorithm as DEAP_algorithm, Constants

# from GeneticAlgorithm import DEAP_algorithm, Constants
from GeneticAlgorithm.FileManagement import Archive
from JsonEditor import jsonEditor
import winsound


def init():
    pop = DEAP_algorithm.create_choreography()


    # Gather all the fitnesses in one list and print the stats
    fits = [ind.fitness.values[0] for ind in pop]

    for i in range(10):
        print pop[i], ind.fitness.values
        # Archive.addToResults({"choreo" : str("".join(pop[i])), "value": fits[i]})
        # with open(Constants.results_path, "a") as myfile:
        #     myfile.write("\n"  + str("".join(pop[i])))


    # jsonEditor.dumpDict("json/results", {"results":a})
    #sendToRobot.send_robot_multiple_movements(pop[0])
    length = len(pop)
    mean = sum(fits) / length
    sum2 = sum(x * x for x in fits)
    std = abs(sum2 / length - mean ** 2) ** 0.5

    print("  Min %s" % min(fits))
    print("  Max %s" % max(fits))
    print("  Avg %s" % mean)
    print("  Std %s" % std)
    # frequency = 2500  # Set Frequency To 2500 Hertz
    # duration = 3000  # Set Duration To 1000 ms == 1 second
    # winsound.Beep(frequency, duration)

try:
    for i in range(1):
        start_time = time.time()
        init()
        print("--- %s seconds ---" % (time.time() - start_time))

except Exception as e:
    print "exception", e

# frequency = 2500  # Set Frequency To 2500 Hertz
# duration = 1000  # Set Duration To 1000 ms == 1 second
# winsound.Beep(frequency, duration)
# time.sleep(1)
# winsound.Beep(frequency, duration)
# time.sleep(1)
# winsound.Beep(frequency, duration)
# time.sleep(1)
# winsound.Beep(frequency, duration)