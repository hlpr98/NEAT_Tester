"""
    TriangleApp
"""
ans = 'Not Sure'  # pragma: no cover
is_triangle = False  # pragma: no cover


def TriangleTester(x, y, z):
    global ans, is_triangle

    if (x + y == z or z + y == x or x + z == y) or (x <= 0 or y <= 0 or z <= 0):
        ans = 'Not Triangle'
        is_triangle = False
    else:
        if x * x == (y * y + z * z) or y * y == (z * z + x * x) or z * z == (y * y + x * x):
            ans = 'RightTriangle'
            is_triangle = True
        else:
            if x != y and x != z and y != z:
                ans = 'ScaleneTriangle'
                is_triangle = True
            elif (x == y and y != z) or (z == y and x != z) or (x == z and y != z):
                ans = 'IsoscelesTriangle'
                is_triangle = True
            elif x == y == z:
                ans = 'EquilateralTriangle'
                is_triangle = True

    print("The triangle is ", ans)  # pragma: no cover
    return is_triangle, ans     # pragma: no cover


### Metadata

state = ('ans', 'is_triangle')  # pragma: no cover

actions = (TriangleTester,)  # pragma: no cover

domains = {TriangleTester: {'x': range(1, 10), 'y': range(1, 10), 'z': range(1, 10)}}  # pragma: no cover
