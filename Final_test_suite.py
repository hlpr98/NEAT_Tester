def TriangleTester(): pass

action = (TriangleTester, )

testSuite = [
  [
    (TriangleTester, (1, 1, 1), (True, 'EquilateralTriangle')),
    (TriangleTester, (3, 2, 2), (True, 'IsoscelesTriangle')),
    (TriangleTester, (5, 4, 3), (True, 'RightTriangle')),
    (TriangleTester, (7, 8, 4), (True, 'ScaleneTriangle')),
    (TriangleTester, (9, 13, 4), (False, 'Not Triangle')),
  ]
]