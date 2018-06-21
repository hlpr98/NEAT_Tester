import os
import sys
from coverage import Coverage

sys.path.append(os.getcwd())
from TestingApp import TriangleApp
# from tmp import testing


def report(testSuite):
    cov = Coverage(branch=True)
    cov.start()
    for test_case in testSuite:
        TriangleApp.TriangleTester(test_case[1][0], test_case[1][1], test_case[1][2])
    cov.stop()
    cov.report(file=open('./tmp/results.txt', 'w'), show_missing=True)

    f = open('./tmp/results.txt', 'r')
    lines = f.readlines()
    imp_elm = []
    br_not_cover = 0
    elements = lines[2].split(' ')
    for e in elements:
        if e != '' and e[0].isdigit():
            e = e.strip(',')
            e = e.strip('\n')
            e = e.strip('%')
            imp_elm.append(e)

    for i in range(5, len(imp_elm)):
        if imp_elm[i].find('->') != -1:
            br_not_cover = br_not_cover + 1

    coverage_report = {'stmt': int(imp_elm[0]), 'miss': int(imp_elm[1]), 'branch': int(imp_elm[2]),
                       'br_par': int(imp_elm[3]), 'cover': int(imp_elm[4]), 'br_not_cover': br_not_cover}

    return coverage_report


# print(report(testing.testSuite[0]))
