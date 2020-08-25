from GeneticAlgorithm.FileManagement import FileManagement
from StringOperations import string_similarity


def calculate_fitness_threshold(repertoire_path):
    sim_min = 1
    if len(FileManagement.getRepertoireWithPath(repertoire_path)["repertoire"]) == 1:
        return 0.5
    for choreo1 in FileManagement.getRepertoireWithPath(repertoire_path)["repertoire"]:
        similarity = 0
        n = 0
        for choreo2 in FileManagement.getRepertoireWithPath(repertoire_path)["repertoire"]:
            if "".join(choreo1["choreo"]) != "".join(choreo2["choreo"]):
                similarity = similarity + string_similarity("".join(choreo1["choreo"]), "".join(choreo2["choreo"]))
                n = n + 1
        similarity = similarity / n
        sim_min = min(sim_min, similarity)
    return sim_min
