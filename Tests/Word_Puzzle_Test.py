import pytest
import os
from puzzle import Puzzle


@pytest.mark.parametrize(("file_name",		"rows",	"cols"),
						[("1D_puzzle.txt",	1,		1)])
def test_puzzle_constructor(file_name, rows, cols):
	file_location = os.path.dirname(os.path.abspath(__file__)) + "/test_Puzzles/" + file_name
	with open(file_location, "r") as file:
		puzzle_string = file.read()
	puzzle = Puzzle(puzzle_string)
	assert puzzle.rows == rows
	assert puzzle.cols == cols
	assert puzzle.puzzle == puzzle_string.replace(",", "").split("\n")
