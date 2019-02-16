import pytest
import os
from puzzle import Puzzle


def read_file(file_name):
    file_location = os.path.dirname(os.path.abspath(__file__)) + "/test_Puzzles/" + file_name
    with open(file_location, "r") as file:
        puzzle_string = file.read()
    return puzzle_string


@pytest.mark.parametrize(("file_name",          "rows", "cols", "expected_puzzle"),
                        [("point_puzzle.txt",   1,      1,      ["A"]),                      # test that constructor works for simplest puzzle
                         ("1D_puzzle.txt",      1,      5,      ["ABCDE"]),                  # test that constructor works with mutliple columns
                         ("1D_puzzle_rows.txt", 5,      1,      ["A", "B", "C", "D", "E"]),  # test that constructor works with multiple rows
                         ("2D_puzzle.txt",      3,      3,      ["ABC", "DEF", "GHI"])       # test that constructor works for 2d puzzles
                        ])
def test_puzzle_constructor(file_name, rows, cols, expected_puzzle):
    puzzle_string = read_file(file_name)
    puzzle = Puzzle(puzzle_string)
    assert puzzle.puzzle_matrix == expected_puzzle
    assert puzzle.rows == rows
    assert puzzle.cols == cols


@pytest.mark.parametrize(("file_name",          "word", "location"),
                        [("point_puzzle.txt",   "A",    [(0, 0)]),                   # test that the function can return the coordanites of a substring
                         ("1D_puzzle.txt",      "B",    [(0, 1)]),                   # test that the function works with multiple substrings
                         ("1D_puzzle.txt",      "AB",   [(0, 0), (0, 1)]),           # test that the function works with larger substrings
                         ("2D_puzzle.txt",      "E",    [(1, 1)]),                   # test that the function works with 2d puzzles
                         ("2D_puzzle.txt",      "GHI",  [(2, 0), (2, 1), (2, 2)]),   # test that the function works with larger substrings with 2d puzzles
                         ("2D_puzzle.txt",      "AC",   []),                         # test that the function wnorks with substrings that are not in the puzzle
                         ("2D_puzzle.txt",      "BA",   [(0, 1), (0, 0)])            # test that the function wnorks with substrings that are not in the puzzle
                        ])
def test_find_word_horizontal(file_name, word, location):
    puzzle = Puzzle(read_file(file_name))
    assert puzzle.find_word_horizontal(word) == location


@pytest.mark.parametrize(("file_name",          "word", "location"),
                        [("point_puzzle.txt",   "A",    [(0, 0)]),                   # test that the function can return the coordanites of a substring
                         ("1D_puzzle_rows.txt", "B",    [(1, 0)]),                   # test that the function works with multiple substrings
                         ("1D_puzzle_rows.txt", "AB",   [(0, 0), (1, 0)]),           # test that the function works with larger substrings
                         ("2D_puzzle.txt",      "E",    [(1, 1)]),                   # test that the function works with 2d puzzles
                         ("2D_puzzle.txt",      "CFI",  [(0, 2), (1, 2), (2, 2)]),   # test that the function works with larger substrings with 2d puzzles
                         ("2D_puzzle.txt",      "AC",   []),                         # test that the function wnorks with substrings that are not in the puzzle
                         ("2D_puzzle.txt",      "DA",   [(1, 0), (0, 0)])            # test that the function wnorks with substrings that are not in the puzzle
                        ])
def test_find_word_vertical(file_name, word, location):
    puzzle = Puzzle(read_file(file_name))
    assert puzzle.find_word_vertical(word) == location


@pytest.mark.parametrize(("file_name",          "word", "location"),
                        [("point_puzzle.txt",   "A",    [(0, 0)]),                   # test that the function can return the coordanites of a substring

                        ])
def test_find_word_diagnal_desending(file_name, word, location):
    puzzle = Puzzle(read_file(file_name))
    assert puzzle.find_word_diagnal_desending(word) == location