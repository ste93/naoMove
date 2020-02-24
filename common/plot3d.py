import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure()
ax = plt.axes(projection='3d')

ax.plot([1.], [1.], [1.], markerfacecolor='k', markeredgecolor='k', marker='o', markersize=5, alpha=0.6)
ax.plot([2.], [2.], [1.], markerfacecolor='k', markeredgecolor='k', marker='o', markersize=5, alpha=0.6)
ax.plot([1.], [1.], [2.], markerfacecolor='k', markeredgecolor='k', marker='o', markersize=5, alpha=0.6)
ax.plot([2.], [2.], [2.], markerfacecolor='k', markeredgecolor='k', marker='o', markersize=5, alpha=0.6)
ax.plot([1.], [2.], [1.], markerfacecolor='k', markeredgecolor='k', marker='o', markersize=5, alpha=0.6)
ax.plot([1.], [2.], [2.], markerfacecolor='k', markeredgecolor='k', marker='o', markersize=5, alpha=0.6)
ax.plot([2.], [1.], [2.], markerfacecolor='k', markeredgecolor='k', marker='o', markersize=5, alpha=0.6)


ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_zlabel('Z Label')

plt.show()
