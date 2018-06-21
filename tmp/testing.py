
# pmt.py -n 5 -s 2 TriangleApp -o ./tmp/testing

# actions here are just labels, but must be symbols with __name__ attribute

def TriangleTester(): pass

# action symbols
actions = (TriangleTester)

testSuite = [
  [
    (TriangleTester, (10, 8, 7), (True, 'ScaleneTriangle')),
    (TriangleTester, (6, 9, 8), (True, 'ScaleneTriangle')),
    (TriangleTester, (7, 8, 4), (True, 'ScaleneTriangle')),
    (TriangleTester, (8, 1, 6), (True, 'ScaleneTriangle')),
    (TriangleTester, (9, 7, 8), (True, 'ScaleneTriangle')),

  ],
]