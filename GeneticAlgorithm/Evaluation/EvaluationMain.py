import os
from GeneticAlgorithm.Evaluation.Evaluation import *
from JsonEditor import jsonEditor

root = "../../json/archive/risultati genetico"
for path, subdirs, files in os.walk(root):
    for name in files:
        if "results_serialized" in name:
            results = []
            with open(os.path.join(path, name)) as fp:
                for line in fp:
                    results.append(line[:-1])
            fp.close()
            repertoire = []
            with open(os.path.join(path, "repertoire_serialized")) as fp:
                for line in fp:
                    repertoire.append(line[:-1])
            fp.close()
            print repertoire
            eval = {}
            evaluation_single_result = {}
            avg_eval = 0
            n = 0
            string_rep = concatenate_items_to_string(repertoire)
            for x in results:
                if x != "": # avoid empty strings
                    evaluation_single_result[x] = compute_ncd(x, string_rep)
                    avg_eval = avg_eval + eval[x]
                    n = n + 1
            string_res = create_string_results(results)
            eval[string_res] = compute_ncd(string_res, string_rep)
            eval["average_typicality"] = avg_eval / n
            eval["single_results"] = evaluation_single_result
            eval["min_typicality"] = calculate_typicality_with_min_distance_from_files(results=results, repertoire=repertoire)
            jsonEditor.dumpDict(os.path.join(path, "evaluation"), eval)
            # here I have all the directories with results