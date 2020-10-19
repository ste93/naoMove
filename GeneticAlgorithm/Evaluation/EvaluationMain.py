import os

from GeneticAlgorithm.Evaluation import RitchieParameters
from GeneticAlgorithm.Evaluation.Evaluation import *
from pandas import DataFrame
import randomIndividuals
from numpy import average

from JsonEditor import jsonEditor

alpha = 0.5
# filename = "fitness"
filename = "7 oct"
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
fit_thres_ful = []
diss_thres_ful = []
len_res_full = []
gen_fitness_total = []
string_res_total = []

fitness_archive_total = []
full_ncd_archive_total = []
criterion1_archive_total = []
criterion2_archive_total = []
len_Arch_full = []
average_min_typicality_archive_total = []
min_typ_total = {}
full_ncd_total = {}
all_results = {}
nov_total = {}


def calculate_fitness_generations(path):
    gen_fitness = 0
    with open(os.path.join(path, "generations_serialized")) as fp:
        for line in fp:
            if ("fitness" in line):
                gen_fitness = gen_fitness + 1
    fp.close()
    return gen_fitness






for path, subdirs, files in os.walk(root):
    for name in files:
        if "results_serialized" in name:

            # results part
            results_serialized = []
            results_length = 0
            # if "and" not in path:
            #     name_results = "results_serialized"

            # collect all the results
            with open(os.path.join(path, name)) as fp:
                for line in fp:
                    if (line != "\n"):
                        results_length = results_length + 1
                    results_serialized.append(line[:-1])
            # print results
            len_res_full.append(results_length)
            fp.close()

            eval = {}
            evaluation_single_result = []
            avg_eval = 0
            n = 0
            count = 0
            avg_fit_results = 0
            avg_nov = 0
            results_complete = []


            repertoire = []
            repertoire_length = 0
            # calculate fitness generations
            gen_fitness = calculate_fitness_generations(path=path)
            gen_fitness_total.append(gen_fitness)

            # open the repertoire
            with open(os.path.join(path, "repertoire_serialized")) as fp:
                for line in fp:
                    if (line != "\n"):
                        repertoire_length = repertoire_length + 1
                        repertoire.append(line[:-1])
            fp.close()

            results_fitness_and_novelty = jsonEditor.readDict(os.path.join(path, "results"))
            fit = []
            ncd_local= []
            string_rep = concatenate_items_to_string(repertoire)
            nov_local = []
            for x in results_fitness_and_novelty["results"]:
                results_complete.append(x["ind"])
                avg_fit_results = avg_fit_results + x["value"][0]
                fit.append(x["value"][0])
                ncd_local.append(compute_ncd("".join(x["ind"]), string_rep))
                if "and" in path:
                    avg_nov = avg_nov + x["value"][1]
                    nov_local.append(x["value"][1])
            all_results["alg"] =fit
            full_ncd_total["alg"] = ncd_local
            avg_fit_results = avg_fit_results / results_length
            avg_nov = avg_nov / results_length
            nov_total["full"] = nov_local


            avg_fit_total.append(avg_fit_results)
            avg_nov_total.append(avg_nov)
            crit1 = RitchieParameters.compute_criterion_1(results=results_complete, string_repertoire=string_rep)
            crit2 = RitchieParameters.compute_criterion_2(results=results_complete, string_repertoire=string_rep, alpha=0.5)
            string_res = create_string_results(results_complete)
            string_res_total.append(string_res)
            eval[string_res] = compute_ncd(string_res, string_rep)
            ncd_full.append(eval[string_res])
            len_repertoire.append(repertoire_length)
            ngen.append(results_fitness_and_novelty["parameters"]["generations"])
            tmin.append(results_fitness_and_novelty["parameters"]["t_min "])
            fit_thres_ful.append(results_fitness_and_novelty["parameters"]["fitness_threshold"])
            diss_thres_ful.append(results_fitness_and_novelty["parameters"]["dissim_threshold"])
            eval["average_typicality Criterion1"] = crit1
            avg_typ.append(crit1)
            eval["single_results"] = evaluation_single_result
            single_res_avg.append(average(evaluation_single_result))
            eval["min_typicality"] = calculate_typicality_with_min_distance_from_files(results=results_complete, repertoire=repertoire)
            min_typ_total["alg"] = calculate_typicality_with_min_distance_from_files(results=results_complete, repertoire=repertoire)
            min_typ.append(average(eval["min_typicality"]))
            eval["criterion2"] = crit2

            crit_2_total.append(crit2)
            index1.append(path.split("\\")[-3:-1:][0])
            index2.append(path.split("\\")[-3:-1:][1])
            # jsonEditor.dumpDict(os.path.join(path, filename), eval)
            # here I have all the directories with results


            # archive part
            if "and" in path:

                results_archive = []
                avg_fit_archive = 0
                archive_string_complete = ""
                results_complete_archive = jsonEditor.readDict(os.path.join(path, "res_arch"))
                fitness_Arch = []
                ncd_local = []
                nov_local = []

                for x in results_complete_archive.values():
                    results_archive.append(x["choreo"])
                    archive_string_complete = archive_string_complete + "".join(x["choreo"])
                    avg_fit_archive = avg_fit_archive + x["fitness"]
                    fitness_Arch.append(x["fitness"])
                    ncd_local.append(compute_ncd("".join(x["choreo"]), string_rep))
                    nov_local.append(x["dissim"])
                nov_total["arch"] = nov_local

                full_ncd_total["archive"] = ncd_local
                all_results["archive"] =fitness_Arch
                min_typ_total["archive"] = calculate_typicality_with_min_distance_from_files(results=results_archive, repertoire=repertoire)
                avg_fit_archive = avg_fit_archive / len(results_complete_archive.values())
                fitness_archive_total.append(avg_fit_archive)
                average_min_typicality_archive_total.append(average(calculate_typicality_with_min_distance_from_files(results=results_archive, repertoire=repertoire)))
                full_ncd_archive_total.append(RitchieParameters.compute_criterion_1(results=results_archive, string_repertoire=string_rep))
                criterion1_archive_total.append(RitchieParameters.compute_criterion_2(results=results_archive, string_repertoire=string_rep, alpha=0.5))
                criterion2_archive_total.append(compute_ncd(archive_string_complete, string_rep))
                len_Arch_full.append(len(results_complete_archive.values()))

            else:
                fitness_archive_total.append("")
                full_ncd_archive_total.append("")
                criterion1_archive_total.append("")
                criterion2_archive_total.append("")
                average_min_typicality_archive_total.append("")
                len_Arch_full.append("")

            # random
            rand_ind = ""
            rand_ind_list = []
            ncd_local= []
            for x in range(results_length) :
                ind = randomIndividuals.init_individual()
                rand_ind = rand_ind + "".join(ind)
                rand_ind_list.append(ind)
                ncd_local.append(compute_ncd("".join(ind), string_rep))
            index1.append(path.split("\\")[-3:-1:][0])
            full_ncd_total["random"] = ncd_local
            index2.append("random")
            ncd_full.append(compute_ncd(rand_ind, string_rep))
            min_typ_total["random"] = calculate_typicality_with_min_distance_from_files(results=rand_ind_list, repertoire=repertoire)
            min_typ.append(average(calculate_typicality_with_min_distance_from_files(results=rand_ind_list, repertoire=repertoire)))
            crit1rand = RitchieParameters.compute_criterion_1(results=rand_ind_list, string_repertoire=string_rep)
            crit2rand = RitchieParameters.compute_criterion_2(results=rand_ind_list, string_repertoire=string_rep, alpha=0.5)
            evaluation_random_average = 0
            fit = []
            for ind in rand_ind_list:
                evaluation_rand= 0
                for x in repertoire:
                    print "".join(ind), "".join(x)
                    evaluation_rand = evaluation_rand + string_similarity("".join(ind), "".join(x))
                evaluation_rand = evaluation_rand / repertoire_length
                evaluation_random_average  =evaluation_random_average + evaluation_rand
                fit.append(evaluation_rand)
            all_results["random"] = fit
            evaluation_random_average = evaluation_random_average/ len(rand_ind)
            avg_typ.append(crit1rand)
            crit_2_total.append(crit2rand)
            avg_fit_total.append(evaluation_random_average)
            len_res_full.append(results_length)
            tmin.append("")
            len_repertoire.append(repertoire_length)
            ngen.append("")
            gen_fitness_total.append("")
            fit_thres_ful.append("")
            diss_thres_ful.append("")
            string_res_total.append(rand_ind)
            fitness_archive_total.append("")
            full_ncd_archive_total.append("")
            criterion1_archive_total.append("")
            criterion2_archive_total.append("")
            average_min_typicality_archive_total.append("")
            avg_nov_total.append("")
            len_Arch_full.append("")


df = DataFrame({'aapath': index1,
                "aapath2": index2,
                "ncd_full": ncd_full,
                'criterion 1': avg_typ,
                'average min_typicality' : min_typ,
                'criterion 2 with ncd' : crit_2_total,
                "avg_fit" : avg_fit_total,
                "average novelty" : avg_nov_total,
                "len_res": len_res_full,
                "len_Arch" : len_Arch_full,
                "tmin": tmin,
                "lenrep": len_repertoire,
                "ngen": ngen,
                "gen_fitness": gen_fitness_total,
                "fit thresh": fit_thres_ful,
                "diss thresh": diss_thres_ful,
                "string_res": string_res_total,
                "fitness archive average": fitness_archive_total,
                "full ncd archive": full_ncd_archive_total,
                "criterion 1 archive":   criterion1_archive_total,
                "criterion 2 archive":  criterion2_archive_total,
                "average min typicality archive": average_min_typicality_archive_total
                # "single_results average ncd": single_res_avg
                })
df.to_excel("../../json/archive/risultati genetico/" + filename + "last.xlsx", sheet_name='sheet1', index=False)