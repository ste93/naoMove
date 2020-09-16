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
    print result
    print "ababa"
    return result


def create_string_results(vector):
    result = ""
    for x in vector:
        print x
        result = result + "".join(x)
        # for y in x:
        #     print y
        #     result = result.join(y)
    print result
    print "asdgwa"
    return result


def calculate_typicality(repertoire_path, results):
    values = []
    for choreo in results:
        sim_min = 1
        for choreo_repertoire in FileManagement.getRepertoireWithPath(repertoire_path)["repertoire"]:
            sim_min = min(sim_min, string_similarity("".join(choreo), "".join(choreo_repertoire["choreo"])))
        values.append(sim_min)
    return values