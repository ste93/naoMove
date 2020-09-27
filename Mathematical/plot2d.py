import numpy as np
import matplotlib.pyplot as plt

from JsonEditor import jsonEditor


def plot2d_2_series_from_path(path):
    data_read = jsonEditor.readDict(path + "values")
    data  = data_read["fitness"]
    data2 = data_read["novelty"]
    if (len(data2.keys()) == 0):
        plot2d_2_series(data, data2, path + "values_graph", "generations", "fitness")
    else:
        plot2d_2_series(data, data2, path + "values_graph", "generations", "fitness and novelty")

    data_read2 = jsonEditor.readDict(path + "ncd_full")
    plot2d(data_read2, path + "ncd_full", "generations", "ncd_full")
    data_read3 = jsonEditor.readDict(path + "criterion_1")
    plot2d(data_read3, path + "criterion_1", "generations", "criterion 1")
    data_read4 = jsonEditor.readDict(path + "criterion_2")
    plot2d(data_read4, path + "criterion_2", "generations", "criterion 2")



def plot2d_2_series(data, data2, path, x_label, y_label):
    ax = plt.axes()
    ax.set_ylim(0,1)
    for i in data.keys():
        ax.plot([i], [data[i]],  marker='o', markersize=2, alpha=0.6,
            color="red")
    for i in data2.keys():
        ax.plot([i], [data2[i]],  marker='o', markersize=2, alpha=0.6,
            color="blue")

    ax.set_xlabel(x_label)
    ax.set_ylabel(y_label)
    plt.savefig(path)
    plt.clf()
    plt.close()


def plot2d(data, path, x_label, y_label):
    ax = plt.axes()
    ax.set_ylim(0,1)

    for i in data.keys():
        ax.plot([i], [data[i]],  marker='o', markersize=2, alpha=0.6,
                color="red")
    ax.set_xlabel(x_label)
    ax.set_ylabel(y_label)
    plt.savefig(path)
    plt.clf()
    plt.close()


def plot2d_fit_nov(data, data2, path):
    ax = plt.axes()
    for i in data:
        print
        ax.plot([i.fitness.values[0]], [i.fitness.values[1]],  marker='o', markersize=5, alpha=0.6,
                color="black")
    for i in data2:
        ax.plot([i.fitness.values[0]], [i.fitness.values[1]],  marker='o', markersize=5, alpha=0.6,
                color="yellow")
    ax.set_xlabel('fitness')
    ax.set_ylabel('novelty')
    plt.axis('equal')

    plt.savefig(path + "plot.png")
    plt.clf()
    plt.close()
