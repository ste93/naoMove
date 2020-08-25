from JsonEditor import jsonEditor
import GeneticAlgorithm.Constants

# todo refactor here
def getArchive():
    try:
        dict = jsonEditor.readDict(GeneticAlgorithm.Constants.archive_path)
        return dict
    except Exception, e:
        print "error", Exception, e


def saveArchive(archive):
    jsonEditor.dumpDict(GeneticAlgorithm.Constants.archive_path, archive)


def addToArchive(choreography):
    # print "adding to archive"
    archive = getArchive()
    archive["archive"].append(choreography)
    saveArchive(archive)


def clearArchive():
    saveArchive({"archive": []})


def loadListOfMoves():
    return jsonEditor.readDict(GeneticAlgorithm.Constants.list_of_moves_path)


def saveListOfMoves(list_of_moves):
    return jsonEditor.dumpDict(GeneticAlgorithm.Constants.list_of_moves_path, list_of_moves)


def getRepertoire():
    try:
        dict = jsonEditor.readDict(GeneticAlgorithm.Constants.repertoire_paths[0])
        return dict
    except Exception, e:
        print "error", e

def getRepertoireWithPath(path):
    try:
        dict = jsonEditor.readDict(path)
        return dict
    except Exception, e:
        print "error", Exception, e


def saveRepertoire(archive):
    jsonEditor.dumpDict(GeneticAlgorithm.Constants.repertoire_paths[0], archive)


def addToRepertoire(choreography):
    archive = getRepertoire()
    archive["repertoire"].append(choreography)
    saveArchive(archive)

def getResults():
    try:
        dict = jsonEditor.readDict(GeneticAlgorithm.Constants.results_path)
        return dict
    except Exception, e:
        print "error", Exception, e

def saveResults(archive):
    saveResultsToPath(GeneticAlgorithm.Constants.results_path, archive)

def saveResultsToPath(archive, path):
    jsonEditor.dumpDict(path, archive)

# def addToResults(choreography):
#     archive = getResults()
#     archive["results"].append(choreography)
#     saveResults(archive)

