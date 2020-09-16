from GeneticAlgorithm.Evaluation import Evaluation


def calculate_ratio(x, y):
    return len(x) / len(y)


def calculate_AV(function, x):
    sum = 0
    for element in x:
        sum = sum + function(element)
    return sum / len(x)


def calculate_typicality(results, repertoire):
    results_string = Evaluation.create_string_results(results)
    repertoire_string = Evaluation.create_string_repertoire(repertoire)
    ncd = Evaluation.compute_ncd(results_string, repertoire_string)
    return ncd


def criterion1(results, repertoire, theta):
    typ = calculate_typicality(results=results,
                               repertoire=repertoire)
    return