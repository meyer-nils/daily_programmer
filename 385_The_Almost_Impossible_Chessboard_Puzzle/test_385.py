#!/usr/bin/env python3
"""Testing the solution."""
import pytest
import numpy as np


def gen_random_tuple():
    """Generate a random board and key position."""
    bits = list(np.random.choice(a=[False, True], size=64))
    X = np.random.randint(0, 63)
    return (bits, X)


@pytest.mark.parametrize("S, X", [gen_random_tuple() for i in range(10)])
def test_solution(S, X):
    """Test the correct solution."""
    from main_385 import prisoner1, prisoner2, flip

    Y = prisoner1(S, X)
    T = flip(S, Y)
    assert prisoner2(T) == X
