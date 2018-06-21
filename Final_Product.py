import os
import pickle
import sys
import neat
import visualize

sys.path.append(os.getcwd())
from tmp import testing
from TestingApp import TriangleApp
from TestingApp import Coverage

winner = pickle.load(open('winner.pkl', 'rb'))

config = neat.Config(neat.DefaultGenome, neat.DefaultReproduction,
                     neat.DefaultSpeciesSet, neat.DefaultStagnation,
                     'config')
node_names = {-1: 'Input-1', -2: 'Input-2', -3: 'Input-3', -4: 'Input-4', -5: 'Input-5', -6: 'Input-6', -7: 'Input-7',
              -8: 'Input-8', -9: 'Input-9',
              0: 'Output-1', 1: 'Output-2', 2: 'Output-3', }

visualize.draw_net(config, winner, view=True, filename='final_network', node_names=node_names)

print('\n****************** Winner report *********************\n')
winner_nn = neat.nn.RecurrentNetwork.create(winner, config)

test_suite = testing.testSuite[0]
test_suite_to_coverage = []

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
    output_from_nn = winner_nn.activate(input)
    output = TriangleApp.TriangleTester(int(output_from_nn[0]), int(output_from_nn[1]), int(output_from_nn[2]))

    output_from_nn = ['TriangleTester', (int(output_from_nn[0]), int(output_from_nn[1]), int(output_from_nn[2])),
                      output]
    test_suite_to_coverage.append(output_from_nn)

print(test_suite_to_coverage)
file = open('Final_test_suite.py', 'w')
file.write('def TriangleTester(): pass\n\naction = (TriangleTester, )\n\ntestSuite = [\n  [\n')
for each in test_suite_to_coverage:
    file.write('    (%s, %s, %s),\n' % (each[0],each[1],each[2]))
file.write('  ]\n]')
result = Coverage.report(test_suite_to_coverage)
print(result)
