# Create math_utils module for import

RED = 0
BLUE = 2
GREEN = 4

def square(x):
    return x * x

def cube(x):
    return x * x * x


def test_square():
    print("testing square()...")
    assert square(2) == 4
    assert square(-3) == 9
    print("testing square() finished")

def test_cube():
    print("testing cube()...")
    assert cube(2) == 8
    assert cube(-3) == -27
    print("testing cube() finished")


if __name__ == '__main__':
    print("testing math_utils")
    test_square()
    test_cube()
    print("done!")
