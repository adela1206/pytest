import pytest

def fizzbuzz(arg):
    if arg % 3 == 0 and arg % 5 == 0:
        return "fizzbuzz"
    if arg == 0:
        return "fizzbuzz"
    if arg % 3 == 0:
        return "fizz"
    if arg % 5 == 0:
        return "buzz"
    return str(arg)

@pytest.mark.parametrize("number", [15, 30, 45])
def test_fizzbuzz_number_returns_fizzbuzz(number):
    assert fizzbuzz(number) == "fizzbuzz"

@pytest.mark.parametrize("number", [1, 2, 4, 7, 11])
def test_fizzbuzz_number_returns_number(number):
    assert fizzbuzz(number) == str(number)

@pytest.mark.parametrize("number", [3, 33, 27, 99])
def test_fizzbuzz_number_returns_fizz(number):
    assert fizzbuzz(number) == "fizz"

@pytest.mark.parametrize("number", [5, 2600, 20])
def test_fizzbuzz_number_returns_buzz(number):
    assert fizzbuzz(number) == "buzz"

def test_fizzbuzz_exists():
    fizzbuzz

def test_fizzbuzz_can_be_called_with_arg():
    fizzbuzz(0)

def test_fizzbuzz_returns_something():
    assert fizzbuzz(0) is not None

def test_fizzbuzz_returns_str():
    assert isinstance(fizzbuzz(0),str)

def test_fizzbuzz_zero_returns_fizzbuzz():
    assert fizzbuzz(0) == "fizzbuzz"



def test_fizzbuzz_3_returns_fizz():
    assert fizzbuzz(3) == "fizz"


