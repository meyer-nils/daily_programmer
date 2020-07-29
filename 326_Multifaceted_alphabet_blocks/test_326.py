#!/usr/bin/env python3
"""Testing the solution."""
import pytest
import os


@pytest.mark.parametrize("input", ["simple.txt", "real_words.txt", "dictionary.txt"])
def test_solution(input):
    """Test  solution."""
    from main import run

    dir = os.path.dirname(__file__)

    run(os.path.join(dir, input))

    os.popen("gcc -o %s/checker %s/checker.c" % (dir, dir)).read()
    stream = os.popen("%s/checker %s/%s < %s/solution.txt" % (dir, dir, input, dir))
    output = stream.read()
    desired_output = "Testing Code...\nRead file."

    os.remove("%s/checker" % dir)

    assert output == desired_output
