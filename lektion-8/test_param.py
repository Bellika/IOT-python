import pytest
from main import add

# parametrize
@pytest.mark.parametrize("a,b,expected", [
    (1, 2, 3),
    (2, 5, 7),
    (10, -2, 8),
])
def test_add(a, b, expected):
    assert add(a, b) == expected

# ids
@pytest.mark.parametrize("a,b,expected", [
    pytest.param(1, 2, 3, id="1+2"),
    pytest.param(2, 5, 7, id="2+5"),
    pytest.param(1, 1, 3, id="known-bug", marks=pytest.mark.xfail(reason="off-by-1")),
])
def test_add_with_ids(a, b, expected):
    assert add(a, b) == expected

# stacking parametrize
# generates combination: (1,10), (1,20), (2,10), (2,20)
@pytest.mark.parametrize("x", [1, 2])        
@pytest.mark.parametrize("y", [10, 20])      
def test_cartesian(x, y):
    assert x * y in {10, 20, 40}

# fixture with params
@pytest.fixture(params=[2, 4, 6])
def number(request):
    return request.param

def test_is_even(number):
    assert number % 2 == 0