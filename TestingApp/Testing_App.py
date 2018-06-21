import os
import sys
import neat

sys.path.append(os.getcwd())
from tmp import testing
from TestingApp import TriangleApp
from TestingApp import Coverage


def TestingApp(genomes, config):
    pop_fitness = []

    for genome in genomes:
        result = Test(genome, config)
        pop_fitness.append((result, genome))

    return pop_fitness


def Test(genome, config):
    neural_network = neat.nn.RecurrentNetwork.create(genome, config)

    test_suite_to_coverage = []
    test_suite = testing.testSuite[0]

    for test_case in test_suite:

        input = (
            int(test_case[1][0]),
            int(test_case[1][1]),
            int(test_case[1][2]),
            (int(test_case[1][0]) * int(test_case[1][0])),
            (int(test_case[1][1]) * int(test_case[1][1])),
            (int(test_case[1][2]) * int(test_case[1][2])),
            (int(test_case[1][0]) * int(test_case[1][1])),
            (int(test_case[1][1]) * int(test_case[1][2])),
            (int(test_case[1][2]) * int(test_case[1][0])),
        )
        output_from_nn = neural_network.activate(input)
        output = TriangleApp.TriangleTester(int(output_from_nn[0]), int(output_from_nn[1]), int(output_from_nn[2]))

        output_from_nn = ['TriangleTester', (int(output_from_nn[0]), int(output_from_nn[1]), int(output_from_nn[2])), output]
        test_suite_to_coverage.append(output_from_nn)

    print(test_suite_to_coverage)
    result = Coverage.report(test_suite_to_coverage)

    return result
