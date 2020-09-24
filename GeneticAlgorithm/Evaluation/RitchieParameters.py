from GeneticAlgorithm.Evaluation import Evaluation
from GeneticAlgorithm.Evaluation.Evaluation import compute_ncd


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


def compute_criterion_1(results, string_repertoire):
    n = 0
    avg_eval = 0
    for x in results:
        if x != "":  # avoid empty strings
            res = compute_ncd("".join(x), string_repertoire)
            avg_eval = avg_eval + res
            n = n + 1
    return avg_eval / n


def compute_criterion_2(results, string_repertoire, alpha):
    n = 0
    count = 0
    for x in results:
        if x != "":  # avoid empty strings
            res = compute_ncd("".join(x), string_repertoire)
            if res > alpha:
                count = count + 1
            n = n + 1
    return count / n

