class Puzzle():

	def __init__(self, puzzle):
		self.puzzle = puzzle.replace(", ", "").split("\n")
		self.rows = len(self.puzzle)
		self.cols = len(self.puzzle[0])

	def find_word_horizontal(self, word):
		return [(0, 0)]