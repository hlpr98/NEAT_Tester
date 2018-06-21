import os
import pickle
import sys
import neat

sys.path.append(os.getcwd())
from TestingApp import Testing_App
import visualize


# from tmp import testing
# from TestingApp import TriangleApp
# from TestingApp import Coverage


def evolutionary_driver(n=5):
    # Load configuration.
    config = neat.Config(neat.DefaultGenome, neat.DefaultReproduction,
                         neat.DefaultSpeciesSet, neat.DefaultStagnation,
                         'config')

    # Create the population, which is the top-level object for a NEAT run.
    p = neat.Population(config)

    # Add a stdout reporter to show progress in the terminal.
    p.add_reporter(neat.StdOutReporter(True))

    stats = neat.StatisticsReporter()
    p.add_reporter(stats)

    # Run until we achive n.
    winner = p.run(eval_genomes, n=n)

    visualize.plot_stats(stats, ylog=False, view=True)
    visualize.plot_species(stats, view=True)

    # winner_nn = neat.nn.RecurrentNetwork.create(winner, config)
    #
    # test_suite = testing.testSuite[0]
    # test_suite_to_coverage = []
    #
    # for test_case in test_suite:
    #     input = (
    #         int(test_case[1][0]),
    #         int(test_case[1][1]),
    #         int(test_case[1][2]),
    #         (int(test_case[1][0]) * int(test_case[1][0])),
    #         (int(test_case[1][1]) * int(test_case[1][1])),
    #         (int(test_case[1][2]) * int(test_case[1][2])),
    #         (int(test_case[1][0]) * int(test_case[1][1])),
    #         (int(test_case[1][1]) * int(test_case[1][2])),
    #         (int(test_case[1][2]) * int(test_case[1][0])),
    #     )
    #     output_from_nn = winner_nn.activate(input)
    #     output = TriangleApp.TriangleTester(int(output_from_nn[0]), int(output_from_nn[1]), int(output_from_nn[2]))
    #
    #     output_from_nn = ['TriangleTester', (int(output_from_nn[0]), int(output_from_nn[1]), int(output_from_nn[2])),
    #                       output]
    #     test_suite_to_coverage.append(output_from_nn)
    #
    # print(test_suite_to_coverage)
    # result = Coverage.report(test_suite_to_coverage)
    # print(result)

    # dump winning genome
    pickle.dump(winner, open('winner.pkl', 'wb'))


def eval_genomes(genomes, config):
    idx, genomes = zip(*genomes)
    f = open('./tmp/graph_metadata.csv', 'a')
    results = Testing_App.TestingApp(genomes, config)
    max = -9999999999999
    sm = 0
    bm = 0
    tm = 0
    for result, genomes in results:
        stmt_coverage = (result['stmt'] - result['miss']) / result['stmt']
        branch_coverage = (result['branch'] - result['br_not_cover']) / result['branch']
        tot_coverage = result['cover'] / 100

        fitness = stmt_coverage * 2 + branch_coverage * 3 + tot_coverage * 5 - (1 - branch_coverage) * 5
        if fitness > max:
            max = fitness
            sm = stmt_coverage
            bm = branch_coverage
            tm = tot_coverage
        genomes.fitness = -1 if fitness <= 0 else fitness

    temp = str(sm) + ',' + str(bm) + ',' + str(tm) + ',' + str(max) + ',' + str(max / 9.675) + '\n'
    f.write(temp)

    # print score
    print('The fitness score was:', fitness)


def main():
    open('./tmp/graph_metadata.csv', 'w')

    if len(sys.argv) > 1:
        evolutionary_driver(int(sys.argv[1]))
    else:
        evolutionary_driver()


if __name__ == "__main__":
    main()
