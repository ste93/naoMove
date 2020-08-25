import numpy as np
import matplotlib.pyplot as plt


def plot2d(data, data2, path):
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