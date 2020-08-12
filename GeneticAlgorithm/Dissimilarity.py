from GeneticAlgorithm import Constants
from GeneticAlgorithm.FileManagement import Archive
from GeneticAlgorithm.StringOperations import string_similarity

#correct
def dissim(individual):
    archive = Archive.getArchive()["archive"]
    values = []
    for x in archive:
        values.append(string_similarity("".join(x), "".join(individual)))
    values.sort(reverse=True)
    max_len = min(Constants.max_arch, len(archive))
    dissimilarity = 0
    for i in range(0, max_len):
        dissimilarity = dissimilarity + values[i]
    if max_len > 0:
        dissimilarity = dissimilarity / max_len
    return dissimilarity
