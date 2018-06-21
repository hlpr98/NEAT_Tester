from __future__ import print_function

import copy
import warnings

import graphviz
import matplotlib.pyplot as plt
import numpy as np

# plt.title("Comparision between different Algorithms")
# plt.xlabel("Number of Test Cases generated")
# plt.ylabel("Coverage achieved")
# plt.grid()
#
# x_values = [5, 18, 5]
# y_values = [33, 80, 85]
#
# # plt.plot(x_values, y_values, 'b-')
# plt.plot([5, ], [33, ], 'ro', label='Naive Generator', markersize=10)
# plt.plot([18, ], [80, ], 'bH', label='EvoSuite(Genetic Algorithm based generator', markersize=10)
# plt.plot([5, ], [85, ], 'g^', label='NEAT Generator', markersize=10)
# plt.plot(x_values, y_values, 'c', linestyle='dashed')


plt.title("Time taken vs Coverage achieved")
plt.xlabel("Time taken(in seconds)")
plt.ylabel("Coverage Achieved(in %)")

x_values = [0, 1, 20, 60, 80, 120, 150, 300, 480]
y_values = [33, 71, 71, 83, 83, 83, 96, 96, 96]
plt.grid()
plt.plot(x_values, y_values, 'c-', marker='^', markerfacecolor='green', markersize=10)
# plt.plot(linestyle='dashed')
# plt.legend(loc='best')
plt.show()