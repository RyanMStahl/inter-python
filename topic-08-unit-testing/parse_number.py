import pytest
from pytest import approx

def parse(s):
    sign = 1.0
    assert len(s) > 0
    if s[0] == "-":
        sign = -1.0
        s = s[1:]
    n = 0.0
    factor = 1.0
    decimal = False
    for c in s:
        if c == ".":
            assert not decimal, "Multiple decimal points encountered"
            decimal = True
            continue
        assert c in "01234567889"
        if not decimal:
            n = n * 10 + ord(c) - ord("0")
            continue
        if decimal:
            factor = factor / 10.0
            n = float(n + (ord(c) - ord("0")) * factor)

    return float(n) * sign


def test_parse_exists():
    "test that parse() can be called with a string and returns a float"
    n = parse("1")
    assert type(n) == float

def test_parse_exists_again():
    "test that parse() can be called with a string and returns a float, again"
    n = parse("1")
    assert type(n) == float

def test_parse_single_digit():
    assert parse("0") == 0
    assert parse("9") == 9

def test_parse_multiple_digits():
    assert parse("123") == 123

def test_parse_floating_point():
    assert parse("123.456") == approx(123.456)
    print("floating point passed")

def test_unary_negation():
    assert parse("-123.456") == approx(-123.456)

if __name__ == "__main__":
    test_parse_exists()
    test_parse_exists_again()
    print("done.")
