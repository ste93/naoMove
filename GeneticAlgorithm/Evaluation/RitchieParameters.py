from GeneticAlgorithm.Evaluation import Evaluation


def calculate_ratio(x, y):
    return len(x) / len(y)


def calculate_AV_typ(x, repertoire):
    sum = 0
    for element in x:
        sum = sum + calculate_typicality(element, repertoire)
    return sum / len(x)


def calculate_typicality(results, repertoire):
    results_string = Evaluation.create_string_results(results)
    repertoire_string = Evaluation.create_string_repertoire(repertoire)
    ncd = Evaluation.compute_ncd(results_string, repertoire_string)
    return ncd


def criterion1(results, repertoire, theta):
    typ = calculate_AV_typ(results, repertoire)
    return typ > theta


def criterion2(alfa, results, repertoire, theta):
    n = 0
    for element in results:
        if calculate_typicality(element, repertoire) > alfa:
            n = n + 1
    return n / len(results) > theta


