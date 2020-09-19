import bz2

from GeneticAlgorithm.FileManagement import FileManagement
from GeneticAlgorithm.StringOperations import string_similarity


def compute_ncd(a, b):
         ca = float(len(bz2.compress(a)))
         cb = float(len(bz2.compress(b)))
         cab = float(len(bz2.compress(a+b)))
         return (cab - min(ca,cb))/max(ca,cb)


def create_string_repertoire(vector):
    result = ""
    for x in vector:
        print x["choreo"]
        result = result + "".join(x["choreo"])
    return result


def concatenate_items_to_string(vector):
    result = ""
    for x in vector:
        print x
        result = result + "".join(x)
    return result


def create_string_results(vector):
    result = ""
    for x in vector:
        print x
        result = result + "".join(x)
    return result


def calculate_typicality_with_min_distance_from_files(repertoire, results):
    values = []
    for choreo in results:
        sim_min = 1
        if choreo != "":
            for choreo_repertoire in repertoire:
                if choreo_repertoire != "":
                    sim_min = min(sim_min, string_similarity("".join(choreo), "".join(choreo_repertoire)))
            values.append(sim_min)
    return values


def calculate_typicality_with_min_distance(repertoire_path, results):
    values = []
    for choreo in results:
        sim_min = 1
        for choreo_repertoire in FileManagement.getRepertoireWithPath(repertoire_path)["repertoire"]:
            sim_min = min(sim_min, string_similarity("".join(choreo), "".join(choreo_repertoire["choreo"])))
        values.append(sim_min)
    return values