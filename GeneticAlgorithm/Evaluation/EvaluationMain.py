import os
from GeneticAlgorithm.Evaluation.Evaluation import *
from pandas import DataFrame
from numpy import average

from JsonEditor import jsonEditor

alpha = 0.5

root = "../../json/archive/risultati genetico/full"
ncd_full = []
avg_typ = []
min_typ = []
crit_2 = []
index1 = []
index2 = []
single_res_avg = []
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
            # print repertoire
            eval = {}
            evaluation_single_result = []
            avg_eval = 0
            n = 0
            count = 0
            string_rep = concatenate_items_to_string(repertoire)
            for x in results:
                if x != "": # avoid empty strings
                    res = compute_ncd(x, string_rep)
                    # evaluation_single_result[x] =
                    evaluation_single_result.append(res)
                    avg_eval = avg_eval + res # evaluation_single_result[x]
                    # if (evaluation_single_result [x] > alpha):
                    if res > alpha:
                        count = count + 1
                    n = n + 1
            string_res = create_string_results(results)
            eval[string_res] = compute_ncd(string_res, string_rep)
            ncd_full.append(eval[string_res])
            eval["average_typicality Criterion1"] = avg_eval / n
            avg_typ.append(avg_eval / n)
            eval["single_results"] = evaluation_single_result
            single_res_avg.append(average(evaluation_single_result))
            eval["min_typicality"] = calculate_typicality_with_min_distance_from_files(results=results, repertoire=repertoire)
            min_typ.append(average(eval["min_typicality"]))
            eval["criterion2"] = (count*1.0) / n
            crit_2.append((count*1.0) / n)
            index1.append(path.split("\\")[-3:-1:][0])
            index2.append(path.split("\\")[-3:-1:][1])
            jsonEditor.dumpDict(os.path.join(path, "evaluation_new"), eval)
            # here I have all the directories with results

df = DataFrame({'aapath': index1,
                "aapath2": index2,
                "ncd_full": ncd_full,
                'average_typicality with ncd (crit 1)': avg_typ,
                'average min_typicality' : min_typ,
                'criterion 2 with ncd' : crit_2
                # "single_results average ncd": single_res_avg
                })

df.to_excel('../../json/archive/evaluation.xlsx', sheet_name='sheet1', index=False)