from GeneticAlgorithm.FileManagement import FileManagement
from StringOperations import string_similarity


def calculate_typicality(repertoire_path, results):
    values = []
    for choreo in results:
        sim_min = 1
        for choreo_repertoire in FileManagement.getRepertoireWithPath(repertoire_path)["repertoire"]:
            sim_min = min(sim_min, string_similarity("".join(choreo), "".join(choreo_repertoire["choreo"])))
        values.append(sim_min)
    return values


