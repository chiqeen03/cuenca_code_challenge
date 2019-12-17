import pytest
from queens import get_all_possible_solutions

def test_testing():
    solutions = get_all_possible_solutions(8) 
    assert len(solutions) == 92