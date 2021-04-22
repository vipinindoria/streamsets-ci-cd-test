import pytest

@pytest.fixture
def numbers():
    a=5
    b=10
    c=15
    return [a,b,c]

@pytest.mark.skip
def test_mul(numbers):
    assert numbers[2] == numbers[0]*numbers[1]

def test_add(numbers):
    assert numbers[2] == numbers[0]+numbers[1]
    
if __name__=="__main__":
    def check():
        return "v" in "vipin"
    check()

