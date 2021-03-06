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
    assert puzzle.matrix == expected_puzzle
    assert puzzle.rows == rows
    assert puzzle.cols == cols


@pytest.mark.parametrize(("file_name",          "word", "location"),
                        [("point_puzzle.txt",   "A",    [(0, 0)]),                   # test that the function can return the coordinates of a substring
                         ("1D_puzzle.txt",      "B",    [(0, 1)]),                   # test that the function works with multiple substrings
                         ("1D_puzzle.txt",      "AB",   [(0, 0), (0, 1)]),           # test that the function works with larger substrings
                         ("2D_puzzle.txt",      "E",    [(1, 1)]),                   # test that the function works with 2d puzzles
                         ("2D_puzzle.txt",      "GHI",  [(2, 0), (2, 1), (2, 2)]),   # test that the function works with larger substrings with 2d puzzles
                         ("2D_puzzle.txt",      "AC",   []),                         # test that the function works with substrings that are not in the puzzle
                         ("2D_puzzle.txt",      "BA",   [(0, 1), (0, 0)])            # test that the function works with substrings that are not in the puzzle
                        ])
def test_find_word_horizontal(file_name, word, location):
    puzzle = Puzzle(read_file(file_name))
    assert puzzle.find_word_horizontal(word) == location


@pytest.mark.parametrize(("file_name",          "word", "location"),
                        [("point_puzzle.txt",   "A",    [(0, 0)]),                   # test that the function can return the coordinates of a substring
                         ("1D_puzzle_rows.txt", "B",    [(1, 0)]),                   # test that the function works with multiple substrings
                         ("1D_puzzle_rows.txt", "AB",   [(0, 0), (1, 0)]),           # test that the function works with larger substrings
                         ("2D_puzzle.txt",      "E",    [(1, 1)]),                   # test that the function works with 2d puzzles
                         ("2D_puzzle.txt",      "CFI",  [(0, 2), (1, 2), (2, 2)]),   # test that the function works with larger substrings with 2d puzzles
                         ("2D_puzzle.txt",      "AC",   []),                         # test that the function works with substrings that are not in the puzzle
                         ("2D_puzzle.txt",      "DA",   [(1, 0), (0, 0)])            # test that the function works with substrings that are not in the puzzle
                        ])
def test_find_word_vertical(file_name, word, location):
    puzzle = Puzzle(read_file(file_name))
    assert puzzle.find_word_vertical(word) == location


@pytest.mark.parametrize(("file_name",          "word", "location"),
                        [("point_puzzle.txt",   "A",    [(0, 0)]),          # test that the function can return the coordinates of a substring
                         ("2D_puzzle.txt",      "E",    [(1, 1)]),          # test that the function works with multiple substrings
                         ("2D_puzzle.txt",      "AE",   [(0, 0), (1, 1)]),  # test that the function works with multichar substrings
                         ("2D_puzzle.txt",      "C",    [(0, 2)]),          # test that the function works outside the matrices diagonal
                         ("2D_puzzle.txt",      "G",    [(2, 0)]),          # test that the function works outside the matrices diagonal
                         ("uneven_puzzle.txt",  "C",    [(0, 2)]),          # test that the function works with other matrix shapes
                        ])
def test_find_word_diagonal_descending(file_name, word, location):
    puzzle = Puzzle(read_file(file_name))
    assert puzzle.find_word_diagonal_descending(word) == location


@pytest.mark.parametrize(("file_name",              "word", "location"),
                        [("point_puzzle.txt",       "A",    [(0, 0)]),          # test that the function can return the coordinates of a substring
                         ("2D_puzzle.txt",          "E",    [(1, 1)]),          # test that the function works with multiple substrings
                         ("2D_puzzle.txt",          "CE",   [(0, 2), (1, 1)]),  # test that the function works with multichar substrings
                         ("2D_puzzle.txt",          "I",    [(2, 2)]),          # test that the function works outside the matrices diagonal
                         ("2D_puzzle.txt",          "A",    [(0, 0)]),          # test that the function works outside the matrices diagonal
                         ("uneven_puzzle.txt",      "F",    [(1, 2)]),          # test that the function works with other matrix shapes
                        ])
def test_find_word_diagonal_ascending(file_name, word, location):
    puzzle = Puzzle(read_file(file_name))
    assert puzzle.find_word_diagonal_ascending(word) == location

@pytest.mark.parametrize(("file_name",              "word", "location"),
                        [("2D_puzzle.txt",          "ABC",    [(0, 0), (0, 1), (0, 2)]),  # test that the function works horizontally
                         ("2D_puzzle.txt",          "DEF",    [(1, 0), (1, 1), (1, 2)]),  # test that the function works horizontally
                         ("2D_puzzle.txt",          "GHI",    [(2, 0), (2, 1), (2, 2)]),  # test that the function works horizontally
                         ("2D_puzzle.txt",          "ADG",    [(0, 0), (1, 0), (2, 0)]),  # test that the function works vertically
                         ("2D_puzzle.txt",          "BEH",    [(0, 1), (1, 1), (2, 1)]),  # test that the function works vertically
                         ("2D_puzzle.txt",          "CFI",    [(0, 2), (1, 2), (2, 2)]),  # test that the function works vertically
                         ("2D_puzzle.txt",          "HD",     [(2, 1), (1, 0)]),          # test that the function works diagonally descending
                         ("2D_puzzle.txt",          "AEI",    [(0, 0), (1, 1), (2, 2)]),  # test that the function works diagonally descending
                         ("2D_puzzle.txt",          "BF",     [(0, 1), (1, 2)]),          # test that the function works diagonally descending
                         ("2D_puzzle.txt",          "DB",     [(1, 0), (0, 1)]),          # test that the function works diagonally ascending
                         ("2D_puzzle.txt",          "GEC",    [(2, 0), (1, 1), (0, 2)]),  # test that the function works diagonally ascending
                         ("2D_puzzle.txt",          "HF",     [(2, 1), (1, 2)]),          # test that the function works diagonally ascending
                         ("2D_puzzle.txt",          "E",      [(1, 1)]),                  # test that the function works diagonally descending
                         ("uneven_puzzle.txt",      "DEF",    [(1, 0), (1, 1), (1, 2)]),  # test that the function works on non-square matrices
                         ("uneven_puzzle.txt",      "BE",     [(0, 1), (1, 1)]),          # test that the function works on non-square matrices
                         ("uneven_puzzle.txt",      "BF",     [(0, 1), (1, 2)]),          # test that the function works on non-square matrices
                         ("uneven_puzzle.txt",      "BD",     [(0, 1), (1, 0)]),          # test that the function works on non-square matrices
                         ("uneven_puzzle_2.txt",    "BDF",    [(0, 1), (1, 1), (2, 1)]),  # test that the function works on non-square matrices
                         ("uneven_puzzle_2.txt",    "CD",     [(1, 0), (1, 1)]),          # test that the function works on non-square matrices
                         ("uneven_puzzle_2.txt",    "CB",     [(1, 0), (0, 1)]),          # test that the function works on non-square matrices                    
                         ("uneven_puzzle_2.txt",    "CF",     [(1, 0), (2, 1)]),          # test that the function works on non-square matrices                    
                        ])
def test_find_word(file_name, word, location):
    puzzle = Puzzle(read_file(file_name))
    assert puzzle.find_word(word) == location
