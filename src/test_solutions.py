import pytest
from queens import get_all_possible_solutions

@pytest.mark.parametrize("n, output",[(8,92),(9,352),(10,724)])
def test_size(n, output):
    solutions = get_all_possible_solutions(n) 
    assert len(solutions) == output