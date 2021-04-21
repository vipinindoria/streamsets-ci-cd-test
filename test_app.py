import pytest

@pytest.fixture
def numbers():
    a=5
    b=10
    c=15
    return [a,b,c]

@pytest.mark.xfail
def test_mul(numbers):
    assert numbers[2] == numbers[0]*numbers[1]

def test_add(numbers):
    assert numbers[2] == numbers[0]+numbers[1]

