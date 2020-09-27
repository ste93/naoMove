import os

from GeneticAlgorithm.Evaluation import RitchieParameters
from GeneticAlgorithm.Evaluation.Evaluation import *
from pandas import DataFrame
from numpy import average

from JsonEditor import jsonEditor

alpha = 0.5
filename = "last"
root = "../../json/archive/risultati genetico/" + filename
ncd_full = []
avg_typ = []
min_typ = []
crit_2_total = []
crit_2_edited_total = []
index1 = []
index2 = []
std = []
max=[]
min = []
mean = []
single_res_avg = []
avg_fit_total = []
avg_nov_total = []
len_repertoire = []
tmin = []
ngen = []
for path, subdirs, files in os.walk(root):
    for name in files:
        if "results_serialized" in name:
            results = []
            with open(os.path.join(path, name)) as fp:
                for line in fp:
                    results.append(line[:-1])
            fp.close()
            repertoire = []
            len = 0
            with open(os.path.join(path, "repertoire_serialized")) as fp:
                for line in fp:
                    if (line != "\n"):
                        len = len + 1
                    repertoire.append(line[:-1])
            fp.close()
            # print repertoire
            eval = {}
            evaluation_single_result = []
            avg_eval = 0
            n = 0
            count = 0
            results_fitness_and_novelty = jsonEditor.readDict(os.path.join(path, "results"))
            avg_fit = 0
            avg_nov = 0
            for x in results_fitness_and_novelty["results"]:
                avg_fit = avg_fit + x["value"][0]
                avg_nov = avg_nov  + x["value"][1]
            avg_fit = avg_fit / 10
            avg_nov = avg_nov / 10
            avg_fit_total.append(avg_fit)
            avg_nov_total.append(avg_nov)
            string_rep = concatenate_items_to_string(repertoire)
            # for x in results:
            #     if x != "": # avoid empty strings
            #         res = compute_ncd(x, string_rep)
            #         # evaluation_single_result[x] =
            #         evaluation_single_result.append(res)
            #         avg_eval = avg_eval + res # evaluation_single_result[x]
            #         # if (evaluation_single_result [x] > alpha):
            #         if res > alpha:
            #             count = count + 1
            #         n = n + 1
            crit1 = RitchieParameters.compute_criterion_1(results=results, string_repertoire=string_rep)
            crit2 = RitchieParameters.compute_criterion_2(results=results, string_repertoire=string_rep, alpha=crit1 - 0.05)
            std.append(results_fitness_and_novelty["statistics"]["std"])
            min.append(results_fitness_and_novelty["statistics"]["min"])
            max.append(results_fitness_and_novelty["statistics"]["max"])
            mean.append(results_fitness_and_novelty["statistics"]["mean"])
            string_res = create_string_results(results)
            eval[string_res] = compute_ncd(string_res, string_rep)
            ncd_full.append(eval[string_res])
            len_repertoire.append(len)
            ngen.append(results_fitness_and_novelty["parameters"]["generations"])
            tmin.append(results_fitness_and_novelty["parameters"]["t_min "])
            eval["average_typicality Criterion1"] = crit1
            avg_typ.append(crit1)
            eval["single_results"] = evaluation_single_result
            single_res_avg.append(average(evaluation_single_result))
            eval["min_typicality"] = calculate_typicality_with_min_distance_from_files(results=results, repertoire=repertoire)
            min_typ.append(average(eval["min_typicality"]))
            eval["criterion2"] = crit2
            crit_2_total.append(crit2)
            index1.append(path.split("\\")[-3:-1:][0])
            index2.append(path.split("\\")[-3:-1:][1])
            jsonEditor.dumpDict(os.path.join(path, filename), eval)
            # here I have all the directories with results

df = DataFrame({'aapath': index1,
                "aapath2": index2,
                "ncd_full": ncd_full,
                'average_typicality with ncd (crit 1)': avg_typ,
                'average min_typicality' : min_typ,
                'criterion 2 with ncd' : crit_2_total,
                "avg_fit" : avg_fit_total,
                "avg_nov": avg_nov_total,
                "mean": mean,
                "max": max,
                "min" : min,
                "std":std,
                "tmin": tmin,
                "lenrep": len_repertoire,
                "ngen": ngen
                # "single_results average ncd": single_res_avg
                })

df.to_excel("../../json/archive/risultati genetico/" + filename + "4.xlsx", sheet_name='sheet1', index=False)