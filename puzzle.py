class Puzzle():

	def __init__(self, puzzle):
		self.puzzle = puzzle.replace(", ", "").split("\n")
		self.rows = 1
		self.cols = len(self.puzzle[0])