#!/usr/bin/local/python

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

def test_cube():
    print("testing cube()...")
    assert cube(2) == 8
    assert cube(-3) == -27

if __name__ == "__main__":
    print("testing math_utils")
    test_square()
    test_cube()
    print("done.")


