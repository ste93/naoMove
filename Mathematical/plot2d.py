import numpy as np
import matplotlib.pyplot as plt


def plot2d(data, path, x_label, y_label):
    fig = plt.figure()
    ax = plt.axes()
    for i in data.keys():
        ax.plot([i], [data[i]],  marker='o', markersize=2, alpha=0.6,
                color="red")
    ax.set_xlabel(x_label)
    ax.set_ylabel(y_label)
    plt.savefig(path)


def plot2d_fit_nov(data, data2, path):
    fig = plt.figure()
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