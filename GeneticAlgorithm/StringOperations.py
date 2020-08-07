from distance import jaccard
from strsimpy.jaro_winkler import JaroWinkler


# similar is 1
# dissimilar is 0
def string_similarity(a, b):
    a = "".join(a)
    b = "".join(b)
    jarowinkler = JaroWinkler()
    return (jarowinkler.similarity(a,b) + 1 - jaccard(a,b))/2